"""
"""

f = open("01_data.txt")
# f = open("01_example_data.txt")

test_data_part_1 = ''.join(f.readlines())
sonar_scan_data = test_data_part_1.split('\n')

initial_measurement = sonar_scan_data[0]

previous_scan = int(initial_measurement)
deeper_counter = 0

grouped_sonar_data = []

for window_start in range(len(sonar_scan_data)-2):

    grouped_sonar_data.append(
        int(sonar_scan_data[window_start])
        +
        int(sonar_scan_data[window_start+1])
        +
        int(sonar_scan_data[window_start+2])
    )

print(grouped_sonar_data)

previous_scan = grouped_sonar_data[0]
deeper_counter = 0

for scan in grouped_sonar_data[1:]:
    if previous_scan < int(scan):
        deeper_counter += 1

    previous_scan = int(scan)

print('deeper_counter:', deeper_counter)

#
#     print(window_start)

    # if previous_scan < int(scan):
    #     deeper_counter += 1
    #
    # previous_scan = int(scan)

# print('deeper_counter:', deeper_counter)
