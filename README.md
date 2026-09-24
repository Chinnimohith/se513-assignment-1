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

### Equivalence Partitioning

| Input / Condition | Valid Class | Invalid Class | Representative Values | Expected Behavior |
|---|---|---|---|---|
| current_credits | 0–15 | < 0 or > 15 | 0, 10, 15, -1, 16 | Valid values may allow registration; invalid values reject registration |
| course_credits | 1–4 | < 1 or > 4 | 1, 3, 4, 0, 5 | Valid values may allow registration; invalid values reject registration |
| prerequisite_met | True | False | True, False | True may allow registration; False rejects registration |
| resulting credit load | <= 18 | > 18 | 18, 19 | 18 is allowed; above 18 is rejected |
| total_credits for fee | 0–18 | < 0 or > 18 | 0, 11, 12, 13, 18, -1, 19 | Valid values return a fee; invalid values raise ValueError |

These representative values cover each important valid and invalid
equivalence class without testing every possible input.

### Boundary-Value Analysis

| Boundary | Neighboring Values | Expected Behavior |
|---|---|---|
| current_credits lower boundary | -1, 0 | -1 rejected; 0 valid |
| current_credits upper boundary | 15, 16 | 15 valid; 16 rejected |
| course_credits lower boundary | 0, 1 | 0 rejected; 1 valid |
| course_credits upper boundary | 4, 5 | 4 valid; 5 rejected |
| resulting credit load | 18, 19 | 18 allowed; 19 rejected |
| fee transition | 11, 12, 13 | Correct fee is calculated on both sides of the 12-credit transition |
| fee valid range | -1, 0, 18, 19 | 0 and 18 valid; -1 and 19 raise ValueError |

Boundary testing is important because an incorrect comparison operator
such as `<` instead of `<=`, or `>` instead of `>=`, could incorrectly
accept or reject values exactly at the allowed limits.

### Positive and Negative Testing

Positive tests verify valid registration scenarios and correct fee
calculations. Negative tests verify prerequisite failures, invalid credit
loads, and invalid fee inputs using `pytest.raises(ValueError)`.

### Parametrization and Fixtures

The test suite uses `@pytest.mark.parametrize` for groups of similar
input and expected-output cases, especially boundary cases.

A reusable `valid_student` fixture provides representative student data
and is used by multiple tests.

A yield-based `temporary_resource` fixture demonstrates setup and cleanup
of a temporary resource. The cleanup executes after the test completes.

Tests are independent and do not depend on execution order or leftover
state from other tests.

### Markers

The test suite uses the following pytest markers:

- `unit` — unit tests for individual functions.
- `positive` — valid inputs and expected successful behavior.
- `negative` — invalid inputs or rejected registration.
- `boundary` — tests focused on boundary values.

### Running the Test Suite

Run the complete test suite:

    pytest

Run selected groups:

    pytest -m positive
    pytest -m negative
    pytest -m boundary
    pytest -m unit