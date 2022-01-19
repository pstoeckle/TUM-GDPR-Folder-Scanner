"""
Script to find students.
"""
from itertools import chain
from logging import INFO, basicConfig, getLogger
from pathlib import Path
from re import compile as re_compile
from sys import stdout
from typing import AbstractSet, MutableSet, Optional

from tqdm import tqdm

from scan_svn import __version__
from tika import parser
from typer import Exit, Option, Typer, echo

basicConfig(
    format="%(levelname)s: %(asctime)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=INFO,
    stream=stdout,
)
_LOGGER = getLogger(__name__)
app = Typer()

_WHITESPACE = re_compile(r"\s")


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
    directory: Path = Option(
        ".",
        "--directory",
        "-s",
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
    tum_name: str = Option(
        None, "--tum-name", "-t", prompt=True, help="The TUM name, e.g., ga12acb."
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
    Scans all relevant files (CSV, TXT, PDF) for the given name, TUM name, and matriculation number.
    """
    name_variations = _create_name_variants(name_to_search)
    matriculation_no_normalized = _normalize(matriculation_no)
    tum_name_normalized = _normalize(tum_name)

    files_with_name: MutableSet[Path] = set()
    files_with_matriculation_no: MutableSet[Path] = set()
    files_with_tum_name: MutableSet[Path] = set()
    echo("Starting the PDF scan...")
    for t in tqdm(list(directory.glob("**/*.pdf"))):
        text = parser.from_file(str(t))
        if text["content"] is None:
            _LOGGER.debug(f"Could not extract text from {t}")
            continue
        normalized_text = _normalize(text["content"])
        if matriculation_no_normalized in normalized_text:
            files_with_matriculation_no.add(t)
        if tum_name_normalized in normalized_text:
            files_with_tum_name.add(t)
        if any(n in normalized_text for n in name_variations):
            files_with_name.add(t)
    echo("PDF scan: done!")
    echo("Starting the CSV and TXT scan ...")
    for t in tqdm(list(chain(directory.glob("**/*.csv"), directory.glob("**/*.txt")))):
        try:
            text = t.read_text()
        except UnicodeDecodeError:
            _LOGGER.debug(f"Encoding problem with {t}")
            continue
        except FileNotFoundError:
            _LOGGER.debug(f"File {t} could not be opened.")
            continue
        normalized_text = _normalize(text)

        if matriculation_no_normalized in normalized_text:
            files_with_matriculation_no.add(t)
        if tum_name_normalized in normalized_text:
            files_with_tum_name.add(t)
        if any(n in normalized_text for n in name_variations):
            files_with_name.add(t)
    echo("CSV and TXT scan: Done!")

    echo("The following files contain the TUM Name")
    for f in files_with_tum_name:
        echo(f)
    echo("The following files contain the matriculation number")
    for f in files_with_matriculation_no:
        echo(f)
    echo("The following files contain the name in any order")
    for f in files_with_name:
        echo(f)


def _normalize(s: str) -> str:
    """

    :param s:
    :return:
    """
    return _WHITESPACE.sub("", s.casefold())


def _create_name_variants(name: str) -> AbstractSet[str]:
    firstname, lastname = name.casefold().split(" ", maxsplit=1)
    return frozenset(
        [
            firstname + lastname,
            lastname + firstname,
            firstname + "," + lastname,
            lastname + "," + firstname,
        ]
    )


if __name__ == "__main__":
    app()
