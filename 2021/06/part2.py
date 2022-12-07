"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
fish_data = test_input.split(',')

initial_state = [int(x) for x in fish_data]


print(initial_state.count(0))
print(initial_state.count(1))

current_state = {
    0: initial_state.count(0),
    1: initial_state.count(1),
    2: initial_state.count(2),
    3: initial_state.count(3),
    4: initial_state.count(4),
    5: initial_state.count(5),
    6: initial_state.count(6),
    7: initial_state.count(7),
    8: initial_state.count(8),
}

next_state = {}

for _ in range(256):
    next_state = {
        0: current_state[1],
        1: current_state[2],
        2: current_state[3],
        3: current_state[4],
        4: current_state[5],
        5: current_state[6],
        6: current_state[7],
        7: current_state[8],
        8: current_state[0]
    }

    if current_state[0] > 0:
        next_state[6] += current_state[0]

    current_state = next_state
    next_state = {}

total = 0
for fish in current_state:
    total += current_state[fish]

print(total)
