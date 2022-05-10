import click
import logging
from dbt_markdoc.main import main


@click.command()
@click.option("--path", default="target/manifest.json", help="Path to dbt manifest")
def make_docs(path) -> None:
    _setup_logger("INFO")

    main(path)


def _setup_logger(log_level="INFO"):
    log_format = (
        "%(asctime)s - %(message)s"
        if log_level == "INFO"
        else "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    formatter = logging.Formatter(log_format, datefmt="%H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # Manually call logger dbt-markdoc so settings cascade
    logger = logging.getLogger("druid")
    logger.setLevel(log_level)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    make_docs()
