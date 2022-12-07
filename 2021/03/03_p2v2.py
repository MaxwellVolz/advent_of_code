"""
"""
from collections import Counter


f = open("03_data.txt")
# f = open("03_example_data.txt")

test_data = ''.join(f.readlines())
diagnostic_report = test_data.split('\n')

maximum_iterations = len(diagnostic_report[0])

oxygen_rating = diagnostic_report
scrubber_rating = diagnostic_report

print(diagnostic_report)


def new_oxygen_rating(oxygen_rating, current_iteration):
    if len(oxygen_rating) == 1:
        return oxygen_rating

    current_index_list = [bit[current_iteration] for bit in oxygen_rating]

    zero_bits = [bit for bit in current_index_list if bit == '0']
    one_bits = [bit for bit in current_index_list if bit == '1']

    amt_of_zeroes = len(zero_bits)
    amt_of_ones = len(one_bits)

    if amt_of_zeroes == amt_of_ones:
        return [bits for bits in oxygen_rating if bits[current_iteration] == '1']
    elif amt_of_zeroes > amt_of_ones:
        return [bits for bits in oxygen_rating if bits[current_iteration] == '0']
    else:
        return [bits for bits in oxygen_rating if bits[current_iteration] == '1']


def new_scrubber_rating(scrubber_rating, current_iteration):
    if len(scrubber_rating) == 1:
        return scrubber_rating

    current_index_list = [bit[current_iteration] for bit in scrubber_rating]

    zero_bits = [bit for bit in current_index_list if bit == '0']
    one_bits = [bit for bit in current_index_list if bit == '1']

    amt_of_zeroes = len(zero_bits)
    amt_of_ones = len(one_bits)

    if amt_of_zeroes == amt_of_ones:
        return [bits for bits in scrubber_rating if bits[current_iteration] == '0']
    elif amt_of_zeroes > amt_of_ones:
        return [bits for bits in scrubber_rating if bits[current_iteration] == '1']
    else:
        return [bits for bits in scrubber_rating if bits[current_iteration] == '0']


for current_iteration in range(maximum_iterations):

    # check if len(diagnostic_report) = 1
    oxygen_rating = new_oxygen_rating(oxygen_rating, current_iteration)
    scrubber_rating = new_scrubber_rating(scrubber_rating, current_iteration)

    # print(current_iteration)
    print(current_iteration)
    print(oxygen_rating, scrubber_rating)


oxygen = int(oxygen_rating[0], 2)
co2 = int(scrubber_rating[0], 2)

print(oxygen, '*', co2, '=', oxygen * co2)
# multiple gamma_rate and epsilon decimal numbers
