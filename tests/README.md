# Tests Directory

Solution implementations organized as pytest test files.

## File naming convention:
- `test_DD_PP.py` where DD is day (01-25) and PP is part (01-02)
- Examples: `test_01_01.py`, `test_01_02.py`, `test_25_01.py`

## Structure:
Each test file contains:
- `solve()` - Main solution function
- `test_example()` - Validates against example data
- `test_solution()` - Runs actual puzzle solution
- `if __name__ == "__main__"` - Allows direct execution

## Running tests:

### Run all tests:
```bash
pytest
```

### Run specific day:
```bash
pytest tests/test_01_*.py
```

### Run specific part:
```bash
pytest tests/test_01_01.py
```

### Run directly:
```bash
python tests/test_01_01.py
```

### Parallel execution:
```bash
pytest -n auto
```
