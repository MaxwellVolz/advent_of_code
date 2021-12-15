"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_data = ''.join(f.readlines())
bingo_data = test_data.split('\n')


chosen_numbers = bingo_data[0].split(',')

bingo_board_amount = len(bingo_data)-2
print(bingo_board_amount)


bingo_boards = []
for starting_point in range(2, bingo_board_amount, 6):
    bingo_boards.append([row.split() for row in bingo_data[starting_point:starting_point+5]])
# ≈

print('bingo_boards')
print(bingo_boards)
print(len(bingo_boards))


def dot_the_boards(all_boards, chosen_number):
    for board_index, bingo_board in enumerate(all_boards):
        for row_index, row in enumerate(bingo_board):
            for bingo_num_index, bingo_num in enumerate(row):
                if bingo_num == chosen_number:
                    bingo_board[row_index][bingo_num_index] = 'x'


def did_someone_win(all_boards):
    for bingo_index, bingo_board in enumerate(all_boards):
        # check rows
        for row in bingo_board:
            if ''.join(row) == 'xxxxx':
                return bingo_board

        # check columns by rotating list of lists
        rotated_list = [list(row) for row in zip(*reversed(bingo_board))]

        for column in rotated_list:
            if ''.join(column) == 'xxxxx':
                return bingo_board

    return None


for money_ball in chosen_numbers:
    print(money_ball)
    dot_the_boards(bingo_boards, money_ball)

    winning_board = did_someone_win(bingo_boards)

    if winning_board:

        print('Winner!')
        print(winning_board)
        sum_of_unmarked = sum([int(item) for sublist in winning_board for item in sublist if item != 'x'])
        sum_times_moneyball = sum_of_unmarked * int(money_ball)
        print(sum_of_unmarked, '*', money_ball,'=',sum_times_moneyball)

        break


# print(chosen_numbers)
# print('')

