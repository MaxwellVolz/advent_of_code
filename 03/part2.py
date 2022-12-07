"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
mule = test_input.split('\n')

def get_priority(item_letter):
    prio = ord(item_letter)

    # Uppercase letters
    if prio < 97:
        return prio - 38

    # Lowercase letters
    else:
        return prio - 96

total_sum = 0

elf_groups = zip(*(iter(mule),) * 3)


for group in list(elf_groups):

    first_intersect = set(group[0]).intersection(set(group[1]))
    badge_item = first_intersect.intersection(set(group[2]))

    total_sum += get_priority(badge_item.pop())

print(total_sum)
