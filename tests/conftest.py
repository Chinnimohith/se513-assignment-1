"""Shared pytest fixtures for the registration test suite.

Add reusable fixtures here as needed for Section 7 of the assignment
(e.g., a fixture providing representative student data used by multiple
tests, and a yield-based fixture that sets up and cleans up a temporary
resource).
"""

# TODO: implement your fixtures here.
import pytest


@pytest.fixture
def valid_student():
    """Provide representative valid student registration data."""
    return {
        "current_credits": 10,
        "course_credits": 3,
        "prerequisite_met": True,
    }


@pytest.fixture
def temporary_resource():
    """Demonstrate setup and cleanup with a yield-based fixture."""
    resource = {"active": True}

    yield resource

    resource["active"] = False
