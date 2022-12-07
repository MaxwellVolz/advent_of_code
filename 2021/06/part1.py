"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
fish_data = test_input.split(',')

initial_state = [int(x) for x in fish_data]

print(initial_state)

for day in range(80):
    new_state = []
    new_fish = 0

    for fish in initial_state:
        if fish == 0:
            new_state.append(6)
            new_fish += 1
        else:
            new_state.append(fish-1)

    new_state.extend([8]*new_fish)

    initial_state = new_state
    # print(day+1, new_state)
    print('Day:', day+1)

print('Total lanternfish:', len(initial_state))