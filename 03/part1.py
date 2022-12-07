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
        
for rucksack in mule:

    front_pack  = rucksack[:len(rucksack)//2]
    back_pack = rucksack[len(rucksack)//2:]

    priority = 0

    for item in front_pack:
        if item in back_pack:
            priority = get_priority(item)
            total_sum += int(priority)
            break

    print(f"""{front_pack} - {back_pack} - {priority} - {total_sum}""")

print(total_sum)
