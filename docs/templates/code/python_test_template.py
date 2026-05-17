"""
Test module: tests/unit/test_<module_name>.py
Scope:       Unit — no I/O, no external services, no network
Covers:      <package>.<module_name> — <FunctionUnderTest>
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from <package>.<module_name> import <FunctionUnderTest>
from <package>.exceptions import <RelevantError>


# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def mock_<dependency>() -> MagicMock:
    """Isolated mock of <DependencyClass>. Resets between tests automatically."""
    return MagicMock(spec=<DependencyClass>)


# ---------------------------------------------------------------------------
# <FunctionUnderTest> — happy paths
# ---------------------------------------------------------------------------


def test_<function_name>_returns_expected_result_given_valid_input(
    mock_<dependency>: MagicMock,
) -> None:
    # Arrange
    mock_<dependency>.<method>.return_value = <stub_value>
    expected = <expected_result>

    # Act
    result = <FunctionUnderTest>(<valid_arg>, dependency=mock_<dependency>)

    # Assert
    assert result == expected
    mock_<dependency>.<method>.assert_called_once_with(<expected_arg>)


# ---------------------------------------------------------------------------
# <FunctionUnderTest> — error paths
# ---------------------------------------------------------------------------


def test_<function_name>_raises_<error>_when_<condition>(
    mock_<dependency>: MagicMock,
) -> None:
    # Arrange
    mock_<dependency>.<method>.return_value = None

    # Act / Assert
    with pytest.raises(<RelevantError>):
        <FunctionUnderTest>(<invalid_arg>, dependency=mock_<dependency>)


def test_<function_name>_raises_<error>_when_dependency_fails(
    mock_<dependency>: MagicMock,
) -> None:
    # Arrange
    mock_<dependency>.<method>.side_effect = RuntimeError("downstream failure")

    # Act / Assert
    with pytest.raises(<RelevantError>):
        <FunctionUnderTest>(<valid_arg>, dependency=mock_<dependency>)


# ---------------------------------------------------------------------------
# Parameterised cases
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("input_value", "expected"),
    [
        (<case_a_input>, <case_a_expected>),
        (<case_b_input>, <case_b_expected>),
        (<edge_case_input>, <edge_case_expected>),
    ],
)
def test_<function_name>_handles_input_variants(
    input_value: <InputType>,
    expected: <OutputType>,
    mock_<dependency>: MagicMock,
) -> None:
    # Arrange
    mock_<dependency>.<method>.return_value = expected

    # Act
    result = <FunctionUnderTest>(input_value, dependency=mock_<dependency>)

    # Assert
    assert result == expected


# ---------------------------------------------------------------------------
# Integration tests (require real services — excluded from default pytest run)
# ---------------------------------------------------------------------------


@pytest.mark.integration
def test_<function_name>_end_to_end_with_real_<service>() -> None:
    """Full round-trip against a real (containerised or local) <service>."""
    # Arrange — connect to real service, seed test data
    # Act
    # Assert
    # Teardown is handled by fixture scope or explicit cleanup below
    pytest.skip("Scaffold only — implement when integration harness is available")
