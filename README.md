# py_opensdbrussels2026

`py_opensdbrussels2026` is a tiny example package for the OpenSD 2026 Brussels summer school. It is intentionally small so it can be used to demonstrate how a Git repository is structured and how open source contributions work.

## What it does

The package ships with a small CSV file of participants and exposes one public function:

- `attendee_was_present(first_name, family_name) -> bool`

It returns `True` when the provided participant name exists in the packaged CSV file and `False` otherwise.

## Installation

```bash
pip install py_opensdbrussels2026
```

For local development:

```bash
pip install -e .[dev]
```

## Usage

```python
from py_opensdbrussels2026 import attendee_was_present

attendee_was_present("Ada", "Lovelace")
```

## Tests

The test suite contains:

- a normal boolean check for an invalid attendee name
- a positive check for a known attendee
- a joke test that reads the packaged CSV, validates countries via `pycountry`, and confirms that `Belgium` is the only intentionally invalid country

Run the tests with:

```bash
pytest
```

## GitHub Actions

Two workflows are included:

- CI workflow for running `pytest` on pushes and pull requests
- Publish workflow for building and publishing the package to PyPI when a GitHub release is published

To use the publish workflow, configure PyPI trusted publishing for this repository.
