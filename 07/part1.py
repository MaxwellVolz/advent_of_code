"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
crab_data = test_input.split(',')

initial_state = [int(x) for x in crab_data]

print(initial_state)

print(min(initial_state), sum(initial_state)/len(initial_state), max(initial_state))

best_fuel = 999999999999
best_pos = -1

def fuel_burn(distance):
    total_burn = 0
    while distance > 0:
        total_burn += distance
        distance -= 1
    return total_burn

for pos in range(min(initial_state),max(initial_state)+1):
    fuel_required = 0

    for crab_pos in initial_state:
        fuel_required += fuel_burn(abs(pos - crab_pos))

    print(pos, fuel_required)

    if fuel_required < best_fuel:
        best_fuel = fuel_required
        best_pos = pos

print(best_pos, best_fuel)


# 467 89791146

