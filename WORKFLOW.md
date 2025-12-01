# How to Solve an Advent of Code Problem

## Step-by-Step Workflow

### 1. Get the Puzzle Input

Go to https://adventofcode.com/2025/day/1 (or whichever day) and:
- Copy the **example input** from the problem description
- Copy **your actual input** (you need to be logged in)

### 2. Add Inputs to YAML Files

**For problems where both parts use the same input:**

`data/day_01_example.yaml`:
```yaml
input: |
  3   4
  4   3
  2   5
  1   3
  3   9
  3   3
```

`data/day_01_data.yaml`:
```yaml
input: |
  12345   67890
  23456   78901
  ... (paste all your lines here)
```

**For problems where parts have different inputs (use part-specific files):**

`data/day_01_p1_example.yaml`:
```yaml
input: |
  L68
  L30
  R48
```

`data/day_01_p1_data.yaml`:
```yaml
input: |
  L6
  L41
  R25
  ... (your actual input)
```

`data/day_01_p2_example.yaml`:
```yaml
input: |
  L68
  L30
  R48
```

`data/day_01_p2_data.yaml`:
```yaml
input: |
  L6
  L41
  R25
  ... (your actual input)
```

### 3. Write Your Solution

Open `tests/test_01_01.py` and edit the `solve()` function:

```python
def solve(input_data: str) -> int:
    """
    input_data is a string containing your puzzle input

    For Day 1, it looks like:
    "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"
    """

    # Step 1: Parse the input
    lines = input_data.strip().split("\n")

    # Step 2: Process each line
    left_list = []
    right_list = []

    for line in lines:
        if line.strip():  # Skip empty lines
            left, right = line.split()  # Split on whitespace
            left_list.append(int(left))
            right_list.append(int(right))

    # Step 3: Solve the problem (this is where YOU implement the logic!)
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    # Step 4: Return the answer
    return total_distance
```

### 4. Run Your Solution

**Option A: Run directly (recommended for debugging)**
```bash
python tests/test_01_01.py
```
- Shows ALL print statements
- Shows timing
- Validates example first, then runs actual solution

**Option B: Run with pytest**
```bash
# Hide print statements (default)
pytest tests/test_01_01.py

# SHOW print statements (use -s flag)
pytest tests/test_01_01.py -s

# Run just the example test
pytest tests/test_01_01.py::test_example -s

# Run just the actual solution
pytest tests/test_01_01.py::test_solution -s
```

## Debugging Tips

### Print statements not showing?
- Use `python tests/test_01_01.py` (always shows prints)
- OR use `pytest -s` flag

### Want to see what the input looks like?
```python
def solve(input_data: str) -> int:
    print("Raw input:")
    print(repr(input_data))  # Shows \n and other special characters

    lines = input_data.strip().split("\n")
    print(f"Number of lines: {len(lines)}")
    print(f"First line: {lines[0]}")

    # ... rest of your code
```

### Test with just the example first
```python
if __name__ == "__main__":
    # Comment out the actual solution while debugging
    run_solution(day=1, part=1, solver=solve, expected_example=11, example=True)
    # run_solution(day=1, part=1, solver=solve)  # Commented out
```

## Common Patterns

### Parsing line-by-line
```python
lines = input_data.strip().split("\n")
for line in lines:
    # process each line
```

### Parsing into a grid
```python
grid = [list(line) for line in input_data.strip().split("\n")]
# grid[row][col]
```

### Parsing numbers
```python
numbers = [int(x) for x in input_data.strip().split()]
```

### Parsing groups separated by blank lines
```python
groups = input_data.strip().split("\n\n")
for group in groups:
    lines = group.split("\n")
    # process group
```

## What Each Function Does

### `solve(input_data: str) -> int`
- **You write this!** This is your solution logic
- Takes the raw input as a string
- Returns your answer

### `test_example()`
- Runs your `solve()` function on example data
- Uses `load_input(day=X, part=Y, example=True)` to load test data
- Checks if the answer matches the expected result
- Useful for validating your logic

### `test_solution()`
- Runs your `solve()` function on actual puzzle data
- Prints the answer
- This is what gets you your star!

### `if __name__ == "__main__":`
- Runs when you execute the file directly
- Runs example first to validate, then actual solution
- Great for development workflow
