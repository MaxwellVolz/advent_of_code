"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
strategy_guide = test_input.split('\n')

rock_value = 1
paper_value = 2
scissor_value = 3

# Key
#
# rock      - 1
# paper     - 2
# scissors  - 3

# X - lose
# Y - tie
# Z - win



def outcome_machine(n):

    # A is rock
    if n == 'A X':
        return 3
    elif n == 'A Y':
        return 4
    elif n == 'A Z':
        return 8

    # B is paper
    elif n == 'B X':
        return 1
    elif n == 'B Y':
        return 5
    elif n == 'B Z':
        return 9

    # C is Scissors
    elif n == 'C X':
        return 2
    elif n == 'C Y':
        return 6
    elif n == 'C Z':
        return 7


print(sum(list(map(outcome_machine, strategy_guide))))


