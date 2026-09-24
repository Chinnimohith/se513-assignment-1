"""Test suite for src/registration.py.

This file is intentionally left for you to implement. See the assignment
handout for the required test-design work:

  - Section 4: Equivalence partitioning
  - Section 5: Boundary-value analysis
  - Section 6: Positive and negative testing with pytest
  - Section 7: Parametrization and fixtures
  - Section 8: Organize and demonstrate the test suite (markers, README)

`registration` is importable directly (see pyproject.toml's `pythonpath`
setting), e.g.:

    from registration import can_register, calculate_registration_fee
"""

# TODO: implement your tests here.
import pytest

from registration import can_register, calculate_registration_fee


@pytest.mark.unit
@pytest.mark.positive
def test_registration_allowed_with_valid_inputs():
    assert can_register(10, 3, True) is True


@pytest.mark.negative
def test_registration_rejected_when_prerequisite_not_met():
    assert can_register(10, 3, False) is False


@pytest.mark.negative
def test_registration_rejected_when_total_credits_exceed_18():
    assert can_register(15, 4, True) is False
@pytest.mark.boundary
@pytest.mark.parametrize(
    "current_credits, course_credits, prerequisite_met, expected",
    [
        (0, 1, True, True),
        (14, 4, True, True),
        (15, 3, True, True),
        (15, 4, True, False),
        (-1, 3, True, False),
        (16, 1, True, False),
        (10, 0, True, False),
        (10, 5, True, False),
    ],
)
def test_registration_boundaries(
    current_credits, course_credits, prerequisite_met, expected
):
    assert can_register(
        current_credits,
        course_credits,
        prerequisite_met
    ) is expected
@pytest.mark.positive
@pytest.mark.parametrize(
    "credits, expected_fee",
    [
        (0, 0.0),
        (1, 100.0),
        (11, 1100.0),
        (12, 1200.0),
        (13, 1275.0),
        (18, 1650.0),
    ],
)
def test_registration_fee_valid_values(credits, expected_fee):
    assert calculate_registration_fee(credits) == expected_fee


@pytest.mark.negative
@pytest.mark.boundary
@pytest.mark.parametrize("credits", [-1, 19])
def test_registration_fee_invalid_values(credits):
    with pytest.raises(ValueError):
        calculate_registration_fee(credits)
@pytest.mark.unit
def test_valid_student_can_register(valid_student):
    assert can_register(
        valid_student["current_credits"],
        valid_student["course_credits"],
        valid_student["prerequisite_met"],
    ) is True


@pytest.mark.unit
def test_valid_student_fee(valid_student):
    total_credits = (
        valid_student["current_credits"]
        + valid_student["course_credits"]
    )
    assert calculate_registration_fee(total_credits) == 1275.0


@pytest.mark.unit
def test_temporary_resource_is_active(temporary_resource):
    assert temporary_resource["active"] is True

   