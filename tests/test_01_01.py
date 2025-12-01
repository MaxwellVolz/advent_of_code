"""Day 1, Part 1: Secret Entrance"""

from core import load_input, run_solution


def solve(input_data: str) -> int:
    """Solve Day 1, Part 1.

    Args:
        input_data: Raw puzzle input

    Returns:
        Solution result
    """
    lines = input_data.strip().split("\n")
    curr_pos, result = 50, 0

    print(f"\n\nStarting...\n")


    for line in lines:
        direction = line[0]
        value = int(line[1:])

        if direction == "L":
            curr_pos = (curr_pos - value) % 100
        elif direction == "R":
            curr_pos = (curr_pos + value) % 100
        
        # print(f"    Moving... {direction} by {value} -> {curr_pos}")

        if curr_pos == 0:
            result += 1
    
    print(f"\nComplete.")

    return result


def test_example():
    """Test with example data."""
    input_data = load_input(day=1, part=1, example=True)
    result = solve(input_data)
    assert result == 3, f"Expected 3, got {result}"


def test_solution():
    """Test with actual puzzle input."""
    result = run_solution(day=1, part=1, solver=solve)
    print(f"\nDay 1 Part 1 answer: {result}")


if __name__ == "__main__":
    # Run example first
    run_solution(day=1, part=1, solver=solve, expected_example=11, example=True)
    # Run actual solution
    run_solution(day=1, part=1, solver=solve)
