# Assignment 1 — Course Registration System (Starter Code)

This is the starter code for SE 413/513 Assignment 1. The business logic in
`src/registration.py` is complete and **must not be modified** — your task
is to design and implement the test suite in `tests/`.

## Project layout

```
assignment-1/
|-- src/registration.py        (provided — do not modify)
|-- tests/test_registration.py (implement your tests here)
|-- tests/conftest.py          (implement your fixtures here)
|-- pyproject.toml
|-- README.md
```

## Setup

1. (Recommended) Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. Install pytest:

   ```
   pip install pytest
   ```

## Running the tests

From the project root:

```
pytest
```

`pyproject.toml` already registers four pytest markers you may use:
`unit`, `positive`, `negative`, and `boundary` (you may register additional
markers of your own if useful). Once you've applied markers to your tests
(Section 8 of the assignment), you can run subsets, e.g.:

```
pytest -m positive
pytest -m boundary
```

## Notes

- Do not modify `src/registration.py`. If you believe there is a defect in
  it, contact the instructor rather than changing it yourself.
- `registration` is importable directly in your tests (no `src.` prefix
  needed), e.g. `from registration import can_register`.

  ## Test Design

### Equivalence Partitions

The `can_register` function was tested using valid and invalid input partitions:

- `current_credits`: valid values are 0–15; invalid values are below 0 or above 15.
- `course_credits`: valid values are 1–4; invalid values are below 1 or above 4.
- `prerequisite_met`: both `True` and `False` were tested.
- Registration is allowed only when the prerequisite is met and the resulting total credits do not exceed 18.

The `calculate_registration_fee` function was tested with valid total credits from 0–18 and invalid values below 0 or above 18.

### Boundary-Value Analysis

Boundary tests include:

- `current_credits`: -1, 0, 15, and 16.
- `course_credits`: 0, 1, 4, and 5.
- Resulting credits at 18 and just above 18.
- Registration fee values around the 12-credit transition.
- Invalid fee values -1 and 19.

### Positive and Negative Testing

Positive tests verify valid registration and fee calculations. Negative tests verify failed registration conditions and confirm that invalid fee inputs raise `ValueError`.

### Pytest Features

The test suite uses `@pytest.mark.parametrize` to run multiple input combinations without duplicating test code.

A reusable `valid_student` fixture provides representative student data and is used by multiple tests.

A yield-based `temporary_resource` fixture demonstrates setup and cleanup behavior.

### Markers

The following pytest markers are used:

- `unit` — unit tests for individual functions.
- `positive` — tests with valid inputs and expected successful behavior.
- `negative` — tests for invalid inputs or rejected registration.
- `boundary` — tests focused on boundary values.

Marker subsets can be run with:

```bash
pytest -m positive
pytest -m negative
pytest -m boundary
pytest -m unit
