"""
"""

f = open("01_data.txt")
# f = open("01_example_data.txt")
test_data_part_1 = ''.join(f.readlines())
sonar_scan_data = test_data_part_1.split('\n')

initial_measurement = sonar_scan_data[0]

previous_scan = int(initial_measurement)
deeper_counter = 0

for scan in sonar_scan_data[1:]:
    if previous_scan < int(scan):
        deeper_counter += 1

    previous_scan = int(scan)

print('deeper_counter:', deeper_counter)
