import click
import os
import pprint
import structlog
import sys

from exif import ExifData
from pathlib import Path
from structlog import get_logger

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso", utc=False),
        structlog.processors.add_log_level,
        structlog.dev.ConsoleRenderer(),
    ]
)
log = get_logger()

@click.group()
@click.version_option("0.1.0", prog_name="Exif Bergmann")
def cli():
    pass

@cli.command("inspect-image", help="Processes a sinle image")
@click.argument(
    "path", 
    type=click.Path(
        exists=True,
        file_okay=True,
        readable=True,
        path_type=Path,
    )
)
def process_single_image(path):
    # log.info("Hello, World!", path=path)
    tags = ExifData.extract_exif_data(path)
    if tags:
        log.info("tag information found", copyright=tags["Image Copyright"])
        pprint.pprint(tags)
    else:
        log.info("no tags found")


if __name__ == "__main__":
    log.info("starting")
    cli()
