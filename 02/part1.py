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
# X -   rock      - 1
# Y -   paper     - 2
# Z -   scissors  - 3

def outcome_machine(n):

    # A is rock
    if n == 'A X':
        return 4
    elif n == 'A Y':
        return 8
    elif n == 'A Z':
        return 3

    # B is paper
    elif n == 'B X':
        return 1
    elif n == 'B Y':
        return 5
    elif n == 'B Z':
        return 9

    # C is Scissors
    elif n == 'C X':
        return 7
    elif n == 'C Y':
        return 2
    elif n == 'C Z':
        return 6


print(sum(list(map(outcome_machine, strategy_guide))))


