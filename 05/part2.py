"""
"""
import re

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
thermal_map = test_input.split('\n')

line_segments = [(re.split(r' -> |,', coords)) for coords in thermal_map]

ground_grid = []

max_x = max_y = 0


def draw_vertical(x, y1, y2):
    line_range = range(int(y1), int(y2)+1)
    for y in line_range:
        ground_grid[y][x] += 1

    line_range = range(int(y2), int(y1)+1)
    for y in line_range:
        ground_grid[y][x] += 1

    print('X:', x, ' Y1:', y1, ' Y2:', y2)
    # for row in ground_grid:
    #     print(row)


def draw_horizontal(y, x1, x2):
    line_range = range(int(x1), int(x2) + 1)
    for x in line_range:
        print('X:',x, ' Y:', y)
        ground_grid[y][x] += 1

    line_range = range(int(x2), int(x1) + 1)
    for x in line_range:
        print('X:',x, ' Y:', y)
        ground_grid[y][x] += 1

    print('Y:', y, ' X1:', x1, ' X2:', x2)


def draw_diagonal(x1, x2, y1, y2):
    x_range = range(int(x1), int(x2) + 1)
    if len(x_range) == 0:
        x_range = reversed(range(int(x2), int(x1) + 1))

    y_range = list(range(int(y1), int(y2)+1))
    if len(y_range) == 0:
        y_range = list(reversed(range(int(y2), int(y1) + 1)))

    for the_index, x in enumerate(x_range):
        print('the_index:', the_index)
        print('x:',[x],'y:',y_range[the_index])
        ground_grid[y_range[the_index]][x] += 1


# Make grid:
for vents in line_segments:
    x1, y1, x2, y2 = vents
    # Only consider horizontal or verticals
    if x1 == x2 or y1 == y2:
        new_max_x = int(max(x1, x2))
        new_max_y = int(max(y1, y2))
        if new_max_x > max_x:
            max_x = new_max_x
        if new_max_y > max_y:
            max_y = new_max_y


# Make grid based on largest passing values
x_grid = [0] * (max_x + 1)

# Hack to avoid list by reference
for iters in range(max_y+1):
    ground_grid.append(x_grid[:])

# print(ground_grid)
# for row in ground_grid:
#     print(row)


for vents in line_segments:
    x1, y1, x2, y2 = vents
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        # Vertical Line
        draw_vertical(x1, y1, y2)
    elif y1 == y2:
        # Horizontal Line
        draw_horizontal(y1, x1, x2)
    else:
        print('DIAGONAL:', x1, y1, x2, y2)
        draw_diagonal(x1, x2, y1, y2)

for row in ground_grid:
    print(row)



print(len([item for sublist in ground_grid for item in sublist if item>=2]))