"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
calorie_data = test_input.split('\n\n')

x = [z.split('\n') for z in calorie_data]

calorie_sums = []

most_calories = 0

for y in x:
    current_counter = 0

    for calories in y:
        current_counter += int(calories)

    if current_counter > most_calories:
        most_calories = current_counter

    calorie_sums.append(current_counter)



print(calorie_sums)
print(most_calories)

calorie_sums.sort()
print(sum(calorie_sums[-3:]))



