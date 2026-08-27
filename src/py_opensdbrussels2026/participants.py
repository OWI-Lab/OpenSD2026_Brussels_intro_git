"""Participant lookup helpers."""

from __future__ import annotations

import csv
from functools import lru_cache
from importlib.resources import files


def _normalize(value: str) -> str:
    return value.strip().casefold()


@lru_cache(maxsize=1)
def _participant_names() -> frozenset[tuple[str, str]]:
    csv_path = files("py_opensdbrussels2026.data").joinpath("participants.csv")
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return frozenset(
            (_normalize(row["first_name"]), _normalize(row["family_name"]))
            for row in reader
        )


def attendee_was_present(first_name: str, family_name: str) -> bool:
    """Return whether a participant appears in the packaged attendee list."""

    return (_normalize(first_name), _normalize(family_name)) in _participant_names()

