import csv
from importlib.resources import files

import pycountry

from py_opensdbrussels2026 import attendee_was_present


def test_invalid_name_returns_false() -> None:
    assert attendee_was_present("Grace", "Hopper") is False


def test_known_name_returns_true() -> None:
    assert attendee_was_present("Ada", "Lovelace") is True


def test_participant_countries_are_real() -> None:
    csv_path = files("py_opensdbrussels2026.data").joinpath("participants.csv")
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        countries = {row["country"] for row in reader}

    recognized_countries = {
        country_name
        for country in pycountry.countries
        for country_name in {
            country.name,
            getattr(country, "common_name", country.name),
            getattr(country, "official_name", country.name),
        }
    }
    invalid_countries = countries - recognized_countries

    assert invalid_countries == set()