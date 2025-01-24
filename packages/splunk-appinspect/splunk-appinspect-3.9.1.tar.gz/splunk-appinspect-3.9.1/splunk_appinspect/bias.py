# Copyright 2020 Splunk Inc. All rights reserved.

"""
A naive bias language scanner.
It flags any words contained in bias_wordlist.txt, optionally with prefixes and suffixes "_ . /".
"""
from __future__ import annotations

import os.path
import re
from pathlib import Path

import magic

exceptions = [""]
prefixes = ["", "_", ".", "/"]
suffixes = ["", "_", ".", "/"]

with open(Path(os.path.abspath(__file__)).parent / "bias_wordlist.txt") as _file:
    words_array = []
    for _line in _file:
        bias_word = _line.strip().lower()
        for prefix in prefixes:
            words_array.append((prefix + bias_word, bias_word))
        for suffix in suffixes:
            words_array.append((bias_word + suffix, bias_word))
    words = dict(words_array)


def get_mime_type(file: Path):
    """
    Call out to the OS to determine whether this file is text or binary (we
    don't want to scan binary files).
    Notice: This method should only be used in Unix environment.
    """
    output = magic.from_file(str(file), mime=True)
    parts = output.split(";")
    return parts[0]


def word_is_bias(word: str) -> tuple[str, str] | None:
    """
    Match a single word against the bias_wordlist
    """
    lc_word = word.lower()
    if lc_word in exceptions:
        return None
    if lc_word in words:
        return word, words[lc_word]

    return None


def scan_file_for_bias(filename: str) -> set[tuple[int, str, str, str]]:
    """
    Tokenize into single words, and match each against the bias word list.
    Notice: The get_mime_type method should only be used in Unix environment.
    """
    results = set()
    if get_mime_type(filename).find("text") == -1:
        # Skip binary files
        return results

    with open(filename, "r", errors="ignore") as file:
        line_number = 0
        for line in file:
            line_number += 1
            for word in re.split(r"\W+", line):
                match = word_is_bias(word)
                if match:
                    results.add((line_number, line.strip(), match[0], match[1]))
    return results
