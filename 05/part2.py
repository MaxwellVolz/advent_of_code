"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
elf_drawing = test_input.split('\n')

# get amount of crates and make empty stacks
amt_of_stacks = len(elf_drawing[0])//4 + 1
stacks = [[] for i in range(amt_of_stacks)]

# solution below causes issue with pass by reference
# stacks = [[]]*amt_of_stacks 

line_counter = 0

# get initial crate layout in list
for line in elf_drawing:

    crate_length = len(line)
    crates = list(line)[1:crate_length:4]

    for x, y in enumerate(crates):

        # ignore empty crates
        if y != ' ':
            stacks[x].insert(0, y)

    line_counter += 1

    if len(line) == 0:
        break

print(stacks)

# parse those moves!
for move in elf_drawing[line_counter:]:
    _,amt_to_move,_,start_pos,_,end_pos = move.split(' ')

    amt_to_move = int(amt_to_move)
    end_pos = int(end_pos) - 1
    start_pos = int(start_pos) - 1

    stacks[end_pos].extend(stacks[start_pos][-amt_to_move:])
    del stacks[start_pos][-amt_to_move:]


print(stacks)

output_string = ""

for stack in stacks:

    output_string += stack[-1]

print(output_string)

