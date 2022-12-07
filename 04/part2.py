"""
"""

# f = open("data.txt")
f = open("example_data.txt")

test_input = ''.join(f.readlines())
cleanup_assignments = test_input.split('\n')

# Tip: use {}.issubset({}) or {}.issuperset({})

overlapping = 0
for pairs in cleanup_assignments:

    elf_a, elf_b = pairs.split(",")

    # make sets from ranges to check if one contains other
    elf_a_areas = set(range(int(elf_a.split("-")[0]), int(elf_a.split("-")[1])+1))
    elf_b_areas = set(range(int(elf_b.split("-")[0]), int(elf_b.split("-")[1])+1))

    if len(elf_a_areas.intersection(elf_b_areas)) > 0:
        overlapping += 1


print(overlapping)