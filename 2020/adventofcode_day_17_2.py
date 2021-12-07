from copy import deepcopy

f = open("data/day_17_part_1.txt")
test_data_part_1 = "".join(f.readlines())

cube_grid = [test_data_part_1.split("\n")]


def run_cycle(current_state):
    print(current_state)
    new_state = current_state

    # Expand x-axis to include potential neighbors
    for z_index, z_slice in enumerate(current_state):
        new_state[z_index] = ['.'+c+'.' for c in z_slice]

    # Expand z-axis to include potential neighbors
    empty_z = "." * len(new_state[0][0])
    new_state.insert(0, [empty_z] * len(new_state[0]))
    new_state.append([empty_z] * len(new_state[0]))

    print(new_state)

    # Use deepcopy to keep reference to original values
    future_state = deepcopy(new_state)

    # Loop through each value
    for z, layer in enumerate(new_state):
        for y, single_row in enumerate(layer):
            # print(single_row)
            for x, cube in enumerate(single_row):

                neighbor_count = check_neighbors(x, y, z, cube, new_state)

                if cube == '#':
                    if neighbor_count == 2 or neighbor_count == 3:
                        pass
                    else:
                        temp_str = list(future_state[z][y])
                        temp_str[x] = '.'
                        future_state[z][y] = ''.join(temp_str)
                else:
                    if neighbor_count == 3:
                        temp_str = list(future_state[z][y])
                        temp_str[x] = '#'
                        future_state[z][y] = ''.join(temp_str)

    print(future_state)

    for a_slice in future_state:
        print('\n'.join(a_slice))
        print('')

    return new_state


def check_neighbors(x, y, z, state, all_cubes):
    # print("x:", x, " y:", y, " z:", z, " state:", state)

    neighbor_counter = 0

    for other_z, layer in enumerate(all_cubes):
        for other_y, single_row in enumerate(layer):
            # print(single_row)
            for other_x, single_point in enumerate(single_row):
                # print("x:", other_x, " y:", other_y, " z:", other_z, " state:", state)
                if [x, y, z] == [other_x, other_y, other_z]:
                    pass
                elif (
                    other_x in range(x - 1, x + 2)
                    and other_y in range(y - 1, y + 2)
                    and other_z in range(z - 1, z + 2)
                ):
                    print(
                        [x, y, z],
                        " has a ",
                        single_point,
                        "neighbor at:",
                        [other_x, other_y, other_z],
                    )
                    if single_point == "#":
                        neighbor_counter += 1
                else:
                    pass

    # print([x, y, z], " has [", neighbor_counter, "] neighbors active.")

    return neighbor_counter
    # If a cube is active and exactly 2 or 3
    # of its neighbors are also active,
    # the cube remains active. Otherwise, the cube becomes inactive.
    #
    # If a cube is inactive but exactly 3
    # of its neighbors are active, the cube becomes active.
    # Otherwise, the cube remains inactive.


next_state = run_cycle(cube_grid)
# run_cycle(next_state)
# run_cycle(next_state)
# The frame of view follows the active cells in each cycle

# TODO: def - increase frame of view in all directions at start of test
# TODO: def - decrease frame of view to only active cells in each cycle
