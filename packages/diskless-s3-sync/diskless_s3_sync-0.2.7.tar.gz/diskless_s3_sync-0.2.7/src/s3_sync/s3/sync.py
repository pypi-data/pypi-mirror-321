import os
from typing import Callable
from typing import Optional

import boto3
from boto3.s3.transfer import TransferConfig
from pydantic import AnyHttpUrl
from pydantic import ByteSize
from pydantic import ValidationError

from ..util import logger
from ..util import settings
from .model import S3Path
from .model import S3Sync


def sync(
    src: Optional[S3Path] = None,
    dest: Optional[S3Path] = None,
    src_endpoint: Optional[AnyHttpUrl] = None,
    dest_endpoint: Optional[AnyHttpUrl] = None,
    src_region: Optional[str] = settings.src.region,
    dest_region: Optional[str] = settings.dest.region,
    src_validate: bool = settings.src.validate_tls,
    dest_validate: bool = settings.dest.validate_tls,
    max_threads_per_file: int = settings.transfer_config.max_threads_per_file,
    max_files: int = settings.transfer_config.max_threads_per_file,
    chunk_size: str = settings.transfer_config.chunk_size,
    printer: Callable = print,
) -> None:
    try:
        chunk_size_int = ByteSize._validate(chunk_size, None)  # type: ignore
    except ValidationError:
        raise RuntimeError(f"Invalid chunk size: {chunk_size}. Please specify in bytes, KB, MiB, or similar.")

    if src_endpoint is None or src_endpoint == "":
        src_endpoint = (
            AnyHttpUrl(os.getenv("AWS_S3_ENDPOINT", "")) if os.getenv("AWS_S3_ENDPOINT") is not None else None
        )

    if src_region is None or src_region == "":
        src_region = os.getenv("AWS_S3_DEFAULT_REGION", None)

    src_access_key = settings.src.access_key
    if src_access_key is None or src_access_key == "":
        src_access_key = os.getenv("AWS_ACCESS_KEY_ID", None)
    logger.debug(f"Constructing src client using Access Key ID: {src_access_key}")

    src_secret_key = settings.src.secret_key
    if src_secret_key is None or src_secret_key == "":
        src_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY", None)

    src_client = boto3.client(
        "s3",
        endpoint_url=str(src_endpoint),
        region_name=src_region,
        verify=src_validate,
        aws_access_key_id=src_access_key,
        aws_secret_access_key=src_secret_key,
    )

    if dest_endpoint is None or dest_endpoint == "":
        dest_endpoint = (
            AnyHttpUrl(os.getenv("AWS_S3_ENDPOINT", "")) if os.getenv("AWS_S3_ENDPOINT") is not None else None
        )

    if dest_region is None or dest_region == "":
        dest_region = os.getenv("AWS_DEFAULT_REGION", None)

    dest_access_key = settings.src.access_key
    if dest_access_key is None or dest_access_key == "":
        dest_access_key = os.getenv("AWS_ACCESS_KEY_ID", None)
    logger.debug(f"Constructing dest client using Access Key ID: {dest_access_key}")

    dest_secret_key = settings.src.secret_key
    if dest_secret_key is None or dest_secret_key == "":
        dest_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY", None)

    dest_client = boto3.client(
        "s3",
        endpoint_url=str(dest_endpoint),
        region_name=dest_region,
        verify=dest_validate,
        aws_access_key_id=dest_access_key,
        aws_secret_access_key=dest_secret_key,
    )

    transfer_config = TransferConfig(
        multipart_chunksize=chunk_size_int,
        multipart_threshold=chunk_size_int,
        max_concurrency=max_threads_per_file,
        preferred_transfer_client="classic",
    )

    if src is None:
        try:
            src = S3Path(url=settings.src.path)
        except ValidationError:
            possible_bucket = os.getenv("AWS_S3_BUCKET", None)
            if possible_bucket is not None:
                src = S3Path(url=f"s3://{possible_bucket}/{settings.src.default_directory}/")
                logger.warning(
                    f"No source S3 path specified, but bucket was provided. Using inferred source: {src.url}"
                )
            else:
                raise RuntimeError("Unable to infer source bucket location")
    if dest is None:
        try:
            dest = S3Path(url=settings.dest.path)
        except ValidationError:
            possible_bucket = os.getenv("AWS_S3_BUCKET", None)
            if possible_bucket is not None:
                dest = S3Path(url=f"s3://{possible_bucket}/{settings.dest.default_directory}/")
                logger.warning(
                    f"No destination S3 path specified, but bucket was provided. Using inferred destination: {dest.url}"
                )
            else:
                raise RuntimeError("Unable to infer destination bucket location")

    sync = S3Sync(
        src=src,
        dest=dest,
        src_client=src_client,
        dest_client=dest_client,
        transfer_config=transfer_config,
        max_files=max_files,
    )
    logger.info(f"Synchronization plan: {sync.plans}")
    for line in sync.execute():
        printer(line)
