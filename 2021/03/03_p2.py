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


def get_allowed_bits(bit_list, zero_for_max=0, default_value=0):
    occurences = Counter(bit_list).most_common(2)

    if occurences[0][1] == occurences[1][1]:
        # return [int(occurences[0][0]), int(occurences[1][0])]
        return [default_value]
    else:
        return [int(occurences[zero_for_max][0])]


for current_iteration in range(maximum_iterations):

    temp_oxygen_rating = []
    temp_scrubber_rating = []
    list_of_bits = []

    for bit in oxygen_rating:
        list_of_bits.append(bit[current_iteration])

    if len(oxygen_rating) != 1:
        allowed_bits = get_allowed_bits(list_of_bits, 0, 1)

        for bit_index, bit in enumerate(oxygen_rating):
            if int(bit[current_iteration]) in allowed_bits:
                # print(bit, 'is', bit[current_iteration], 'in', allowed_bits)
                temp_oxygen_rating.append(oxygen_rating[bit_index])

        oxygen_rating = temp_oxygen_rating

    for bit in scrubber_rating:
        list_of_bits.append(bit[current_iteration])

    if len(scrubber_rating) != 1:
        allowed_bits = get_allowed_bits(list_of_bits, 1, 0)

        for bit_index, bit in enumerate(scrubber_rating):
            if int(bit[current_iteration]) in allowed_bits:
                # print(bit, 'is', bit[current_iteration], 'in', allowed_bits)
                temp_scrubber_rating.append(scrubber_rating[bit_index])

        scrubber_rating = temp_scrubber_rating


# print('temp_oxygen_rating', int(int(oxygen_rating[0]),2))
# print(scrubber_rating)
oxygen = int(oxygen_rating[0], 2)
co2 = int(scrubber_rating[0], 2)
print(oxygen)
print(co2)
print(oxygen * co2)
# multiple gamma_rate and epsilon decimal numbers
