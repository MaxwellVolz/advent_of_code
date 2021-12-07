f = open("data/day_17_part_1.txt")
test_data_part_1 = "".join(f.readlines())


cube_grid = test_data_part_1.split("\n")

next_pocket_dimension = cube_grid
next_pocket_dimension = [list(x) for x in next_pocket_dimension]


def check_neighbors(x, y, z, state, all_cubes):

    # print("x:", x, "| y:", y, "| z:", z, "| state:", state)
    neighbors_active = 0
    neighbors_total = 0

    for n_y_pos, n_cube_line in enumerate(cube_grid):

        for n_x_pos, n_state in enumerate(cube_line):
            # Reset counter
            # Check if neighbor is self, then within 1 position for x and y
            if [n_x_pos, n_y_pos] != [x,y] and n_x_pos in [x-1, x, x+1] and n_y_pos in [y-1, y, y+1]:
                # print('Neighbor!:', n_x_pos, n_y_pos)
                if cube_grid[n_x_pos][n_y_pos] == '#':
                    neighbors_active += 1
                neighbors_total += 1

            # print('Total active:', neighbors_active)

            # If a cube is active and exactly 2 or 3
            # of its neighbors are also active,
            # the cube remains active. Otherwise, the cube becomes inactive.
            #
            # If a cube is inactive but exactly 3
            # of its neighbors are active, the cube becomes active.
            # Otherwise, the cube remains inactive.

            curr_state = cube_grid[n_x_pos][n_y_pos]

            if curr_state == '#':
                if neighbors_active == 2 or neighbors_active == 3:
                    # print("Stay Active!")
                    pass
                else:
                    curr_state = '.'
            else:
                if neighbors_active == 3:
                    curr_state = '#'


            next_pocket_dimension[y][x] = curr_state

    print('Total neighbors:', neighbors_total)
    # next_pocket_dimension[y][x] = neighbors_total
    # print(next_pocket_dimension[y][x])


print(test_data_part_1)
print(next_pocket_dimension)
for y_pos, cube_line in enumerate(cube_grid):
    for x_pos, state in enumerate(cube_line):
        check_neighbors(x_pos, y_pos, 0, state, cube_grid)

for line in next_pocket_dimension:
    print(line)
# print(next_pocket_dimension)


# The frame of view follows the active cells in each cycle

# TODO: def - increase frame of view in all directions at start of test
# TODO: def - decrease frame of view to only active cells in each cycle
