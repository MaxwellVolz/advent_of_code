"""Day 1, Part 2: Secret Entrance"""

from core import load_input, run_solution


def solve(input_data: str) -> int:
    """Solve Day 1, Part 2.

    Count every time the dial points at 0, whether during or at end of rotation.
    - R (right/clockwise) adds to position
    - L (left/counter-clockwise) subtracts from position
    - Dial has positions 0-99 (wraps around)

    Args:
        input_data: Raw puzzle input

    Returns:
        Number of times dial points at 0
    """
    lines = input_data.strip().split("\n")
    curr_pos, result = 50, 0

    for line in lines:
        direction = line[0]
        value = int(line[1:])

        if direction == "R":
            # Going right (clockwise) - adding value
            total_crosses = (curr_pos + value) // 100
            new_pos = (curr_pos + value) % 100

            if new_pos == 0:
                # We ended at 0, one of the crosses is the ending position
                crossings_during = total_crosses - 1
                result += crossings_during + 1
            else:
                # All crosses are during the rotation
                result += total_crosses

        else:  # direction == "L"
            # Going left (counter-clockwise) - subtracting value
            if curr_pos == 0:
                # Starting at 0, we cross 0 every 100 steps
                total_crosses = value // 100
            else:
                if curr_pos <= value:
                    # We'll cross 0 at least once
                    total_crosses = (value - curr_pos) // 100 + 1
                else:
                    # We won't reach 0
                    total_crosses = 0

            new_pos = (curr_pos - value) % 100

            if new_pos == 0 and total_crosses > 0:
                # We ended at 0, the last cross is the ending
                crossings_during = total_crosses - 1
                result += crossings_during + 1
            else:
                result += total_crosses

        curr_pos = new_pos

    return result


def test_example():
    """Test with example data."""
    input_data = load_input(day=1, part=2, example=True)
    result = solve(input_data)
    assert result == 6, f"Expected 6, got {result}"


def test_solution():
    """Test with actual puzzle input."""
    result = run_solution(day=1, part=1, solver=solve)
    print(f"\nDay 1 Part 2 answer: {result}")


if __name__ == "__main__":
    # Run example first
    run_solution(day=1, part=1, solver=solve, expected_example=11, example=True)
    # Run actual solution
    run_solution(day=1, part=1, solver=solve)
