# Advent of Code Solutions

Clean, modern Python project architecture optimized for fast iteration, clean testing, and Advent of Code-style puzzle solving. It is minimal, structured, and built to avoid friction when jumping between daily problems.

## Architecture

- **core.py** - Reusable infrastructure
  - Input loading from YAML files
  - Timing utilities
  - Solution runner with validation
- **data/** - Input files organized by day
  - `day_XX_example.yaml` - Example inputs from problem descriptions
  - `day_XX_data.yaml` - Your actual puzzle inputs
- **tests/** - Solution implementations
  - `test_DD_PP.py` - Day DD, Part PP solutions
  - Each file is both a runnable script and pytest test
- **pyproject.toml** - Modern Python packaging configuration
- **pytest.ini** - Test runner configuration

## Quick Start

### 1. Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -e .

# Optional: Install dev tools
pip install -e ".[dev]"
```

### 2. Add Your Puzzle Input
Copy your puzzle input from [adventofcode.com](https://adventofcode.com) into the appropriate YAML file:

```yaml
# data/day_01_data.yaml
input: |
  Your puzzle input here
  Line by line
  Preserves formatting
```

### 3. Solve the Problem
Edit the test file (e.g., `tests/test_01_01.py`) and implement your solution in the `solve()` function.

### 4. Run Your Solution

**Run directly:**
```bash
python tests/test_01_01.py
```

**Run with pytest:**
```bash
# Run all tests
pytest

# Run specific day
pytest tests/test_01_*.py

# Run specific part
pytest tests/test_01_01.py

# Run with parallel execution
pytest -n auto
```

## Project Structure

```
advent_of_code/
├── core.py              # Core infrastructure
├── pyproject.toml       # Project configuration
├── pytest.ini          # Test configuration
├── requirements.txt    # Dependencies
├── data/               # Puzzle inputs
│   ├── day_01_example.yaml
│   ├── day_01_data.yaml
│   └── ...
└── tests/             # Solutions
    ├── test_01_01.py
    ├── test_01_02.py
    └── ...
```

## Example Workflow

For Day 1, Part 1:

1. **Read the problem** on adventofcode.com
2. **Add example input** to `data/day_01_example.yaml`
3. **Add your input** to `data/day_01_data.yaml`
4. **Implement solution** in `tests/test_01_01.py`:

```python
from core import load_input, run_solution

def solve(input_data: str) -> int:
    # Your solution here
    return result

def test_example():
    input_data = load_input(1, example=True)
    result = solve(input_data)
    assert result == expected_value

def test_solution():
    result = run_solution(day=1, part=1, solver=solve)
    print(f"\nDay 1 Part 1 answer: {result}")

if __name__ == "__main__":
    run_solution(day=1, part=1, solver=solve, expected_example=11, example=True)
    run_solution(day=1, part=1, solver=solve)
```

5. **Run it:**
```bash
python tests/test_01_01.py
```

## Features

- **Fast iteration** - Run solutions directly or through pytest
- **Automatic timing** - See how fast your solutions run
- **Example validation** - Test against example data first
- **Parallel testing** - Run multiple tests simultaneously
- **Clean separation** - Logic, data, and infrastructure are separate
- **Type hints** - Modern Python with type annotations
- **YAML inputs** - Clean, structured input files

## Tips

- Start with the example data to validate your logic
- Use `run_solution()` for automatic timing and validation
- Run tests in parallel with `pytest -n auto` to save time
- Keep actual puzzle inputs private by uncommenting the gitignore entry