"""
"""

f = open("02_data.txt")
# f = open("02_example_data.txt")
test_data_part_1 = ''.join(f.readlines())
planned_course = test_data_part_1.split('\n')

horizontal_pos = 0
depth = 0

for movement in planned_course:
    print(movement)
    direction, move_amount = movement.split(' ')
    move_amount = int(move_amount)

    if direction == 'forward':
        horizontal_pos += move_amount
    elif direction == 'down':
        depth += move_amount
    else:
        depth -= move_amount

print(horizontal_pos, depth)
print(horizontal_pos * depth)
