"""
Module:       <module_name>
Package:      src.<package_name>.<module_name>
Purpose:      <One-line description of what this module does>
Prerequisites:
    - Python >= 3.12
    - <Environment variable or config file required before import, if any>
Dependencies:
    - structlog: structured logging
    - <library>: <why it is needed>
Usage:
    uv run python -m <package>.<module> [--option value]
    from <package>.<module> import <PublicClass>
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

import structlog

from <package>.exceptions import <ModuleError>
from <package>.models import <DomainModel>

if TYPE_CHECKING:
    pass

log = structlog.get_logger(__name__)


# ---------------------------------------------------------------------------
# Domain types
# ---------------------------------------------------------------------------

# Define dataclasses, Pydantic models, or TypedDicts local to this module here.
# Shared types belong in models.py.


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------


def <function_name>(arg: <ArgType>, *, option: bool = False) -> <ReturnType>:
    """<One-line docstring: what this function returns or does.>

    Args:
        arg: <Description>
        option: <Description>

    Returns:
        <Description of the return value>

    Raises:
        <ModuleError>: when <condition that causes the error>
    """
    if not arg:
        log.warning("<module>.<function>.invalid_input", arg=arg)
        raise <ModuleError>(f"<description>: {arg!r}")

    log.debug("<module>.<function>.called", arg=arg)
    result: <ReturnType> = ...  # implementation
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """CLI entry point. Parse arguments, call domain logic, handle output."""
    import argparse

    parser = argparse.ArgumentParser(description="<brief description>")
    parser.add_argument("--<option>", type=str, required=True, help="<description>")
    args = parser.parse_args()

    log.info("<module>.started", option=args.<option>)
    try:
        result = <function_name>(args.<option>)
        print(result)  # noqa: T201 — intentional CLI output
    except <ModuleError> as exc:
        log.error("<module>.failed", error=str(exc))
        sys.exit(1)


if __name__ == "__main__":
    main()
