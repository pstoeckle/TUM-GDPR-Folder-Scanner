"""
Script to find students.
"""
from logging import INFO, basicConfig, getLogger
from pathlib import Path
from typing import Optional

from tum_gdpr_folder_scanner import __version__
from tum_gdpr_folder_scanner.folder_scanner import FolderScanner
from typer import Exit, Option, Typer, echo, Argument

basicConfig(
    format="%(levelname)s: %(asctime)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=INFO,
    filename="scan-svn.log",
    filemode="w",
)
_LOGGER = getLogger(__name__)
app = Typer()


def _version_callback(value: bool) -> None:
    """

    :param value:
    :return:
    """
    if value:
        echo(f"scan-svn {__version__}")
        raise Exit()


@app.command()
def scan_directory(
    directory: Path = Argument(
        ".",
        help="The directory we want to analyze.",
        file_okay=False,
        resolve_path=True,
    ),
    name_to_search: str = Option(
        None,
        "--name-to-search",
        "-n",
        prompt=True,
        help="The name we are looking for. Please write the name in the form `Lastname Firstname` or `Firstname Lastname`.",
    ),
    matriculation_no: str = Option(
        None,
        "--matriculation-no",
        "-m",
        prompt=True,
        help="The matriculation number we are looking for.",
    ),
    tum_id: str = Option(
        None, "--tum-id", "-t", prompt=True, help="The TUM ID, e.g., ga12acb."
    ),
    skip_pdfs: bool = Option(
        False,
        "--skip-pdfs",
        "-S",
        is_flag=True,
        help="The PDF extraction takes some time. You can skip it for a first run.",
    ),
    skip_xlsx: bool = Option(
        False,
        "--skip-xlsx",
        "-X",
        is_flag=True,
        help="The XLSX extraction takes some time. You can skip it for a first run.",
    ),
    _: Optional[bool] = Option(
        None,
        "--version",
        "-v",
        callback=_version_callback,
        help="Shows the version and exits.",
    ),
) -> None:
    """
    Scans all relevant files (CSV, PDF, TXT, XLSX, XML) for the given name, TUM name, and matriculation number.
    """
    scanner = FolderScanner(tum_id, name_to_search, matriculation_no)
    scanner.scan(directory, skip_pdfs, skip_xlsx)


if __name__ == "__main__":
    app()
