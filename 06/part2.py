"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())

data_stream = list(test_input)

counter = 14

for x in range(len(data_stream)):

    # print(data_stream[x:x+4])
    # print(len(set(data_stream[x:x+4])))
    
    if len(set(data_stream[x:x+14])) > 13:
        print(data_stream[x:x+14])
        break

    counter += 1

print(counter)