# This example code was pulled fromthe following link:
# https://stackoverflow.com/questions/51784232/how-do-i-convert-the-webvtt-format-to-plain-text

from pathlib import Path
from typing import Generator
import webvtt


def vtt_lines(src) -> Generator[str, None, None]:
    """
    Extracts all text lines from a vtt file which may contain duplicates

    :param src: File path or file like object
    :return: Generator for lines as strings
    """
    vtt = webvtt.read(src)

    for caption in vtt:  # type: webvtt.structures.Caption
        # A caption which may contain multiple lines
        for line in caption.text.strip().splitlines():  # type: str
            # Process each one of them
            yield line


def deduplicated_lines(lines) -> Generator[str, None, None]:
    """
    Filters all duplicated lines from list or generator

    :param lines: iterable or generator of stringsa
    :return: Generator for lines as strings without duplicates
    """
    last_line = ""
    for line in lines:
        if line == last_line:
            continue

        last_line = line
        yield line


def vtt_to_linear_text(src, savefile: Path, line_end="\n"):
    """
    Converts an vtt caption file to linear text.

    :param src: Path or path like object to an existing vtt file
    :param savefile: Path object to save content in
    :param line_end: Default to line break. May be set to a space for a single line output.
    """
    with savefile.open("w") as writer:
        for line in deduplicated_lines(vtt_lines(src)):
            writer.write(line.replace("&nbsp;", " ").strip() + line_end)

# Demo call
vtt_to_linear_text("../Streams/20240216 - EP._16_-_nearing_the_end_of_an_era/EP._16_-_nearing_the_end_of_an_era [Tz0xSdrEfTc].en.vtt", Path("output.txt"))