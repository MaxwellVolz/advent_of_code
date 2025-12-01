"""Core infrastructure for Advent of Code solutions.

Provides:
- Input loading from YAML files
- Timing utilities
- Test runner logic
"""

from pathlib import Path
from time import perf_counter
from typing import Any, Callable

import yaml


def load_input(day: int, part: int | None = None, example: bool = False) -> str:
    """Load puzzle input from data directory.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2), if None tries day-level file
        example: If True, load example_data instead of actual data

    Returns:
        Raw input string
    """
    data_type = "example" if example else "data"

    # Try part-specific file first (e.g., day_01_p1_example.yaml)
    if part is not None:
        filename = f"day_{day:02d}_p{part}_{data_type}.yaml"
        path = Path(__file__).parent / "data" / filename

        if path.exists():
            with open(path) as f:
                data = yaml.safe_load(f)
                return data.get("input", "")

    # Fall back to day-level file (e.g., day_01_example.yaml)
    filename = f"day_{day:02d}_{data_type}.yaml"
    path = Path(__file__).parent / "data" / filename

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with open(path) as f:
        data = yaml.safe_load(f)
        return data.get("input", "")


def time_solution(func: Callable[..., Any], *args: Any, **kwargs: Any) -> tuple[Any, float]:
    """Time a solution function.

    Args:
        func: Function to time
        *args: Positional arguments for func
        **kwargs: Keyword arguments for func

    Returns:
        Tuple of (result, elapsed_time_ms)
    """
    start = perf_counter()
    result = func(*args, **kwargs)
    elapsed = (perf_counter() - start) * 1000
    return result, elapsed


def run_solution(
    day: int,
    part: int,
    solver: Callable[[str], Any],
    expected_example: Any = None,
    example: bool = False,
) -> Any:
    """Run a solution with timing and optional validation.

    Args:
        day: Day number
        part: Part number (1 or 2)
        solver: Function that takes input string and returns answer
        expected_example: If provided, validate against example data
        example: If True, run against example data

    Returns:
        Solution result
    """
    input_data = load_input(day, part=part, example=example)

    # Check if input data is essentially empty (only comments/whitespace)
    has_real_data = any(
        line.strip() and not line.strip().startswith("#")
        for line in input_data.split("\n")
    )

    if not example and not has_real_data:
        print(f"Day {day:02d} Part {part} (actual)")
        print(f"  \u26a0 No puzzle data found!")
        print(f"  Add your input to: data/day_{day:02d}_data.yaml")
        print(f"  Get it from: https://adventofcode.com/2025/day/{day}")
        return None

    result, elapsed = time_solution(solver, input_data)

    print(f"Day {day:02d} Part {part} ({('actual', 'example')[example]})")
    print(f"  Result: {result}")
    print(f"  Time: {elapsed:.2f}ms")

    if expected_example is not None and example:
        assert result == expected_example, f"Expected {expected_example}, got {result}"
        print("  \u2713 Example validated")

    return result
