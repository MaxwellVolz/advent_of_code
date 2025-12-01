# Data Directory

Input files are stored as YAML for clean structure and easy parsing.

## File naming conventions:

### Part-specific files (recommended when parts have different inputs):
- `day_XX_p1_example.yaml` - Part 1 example input
- `day_XX_p1_data.yaml` - Part 1 actual puzzle input
- `day_XX_p2_example.yaml` - Part 2 example input
- `day_XX_p2_data.yaml` - Part 2 actual puzzle input

### Day-level files (fallback when both parts share same input):
- `day_XX_example.yaml` - Example input from problem description
- `day_XX_data.yaml` - Your actual puzzle input

The system tries part-specific files first, then falls back to day-level files.

## YAML structure:
```yaml
input: |
  Your puzzle input here
  Can be multiple lines
  Preserves formatting
```

## Getting your input:
1. Log in to https://adventofcode.com
2. Navigate to the day's puzzle
3. Copy your input
4. Paste into the corresponding YAML file(s)
