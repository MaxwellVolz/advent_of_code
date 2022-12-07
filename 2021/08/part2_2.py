"""
"""

f = open("data.txt")
# f = open("example_data.txt")
# f = open("example_data2.txt")

test_input = ''.join(f.readlines())
segment_data = test_input.split('\n')

occurrences = 0
output_sum = 0


for line in segment_data:
    all_entries = line.split() 

    signal_patterns = all_entries[:all_entries.index('|')]
    output_signal_patterns = all_entries[all_entries.index('|')+1:]

    print(signal_patterns)
    print(output_signal_patterns)

    signal_zero = signal_two = signal_three = signal_five = signal_six = signal_nine = ''
    top = top_left = top_right = middle = bottom_left = bottom_right = bottom = ' '

    # find signals 1,7,8 by length
    for signal in signal_patterns:
        signal_length = len(signal)

        if signal_length == 2:
            signal_one = signal
        elif signal_length == 3:
            signal_seven = signal
        elif signal_length == 4:
            signal_four = signal
        elif signal_length == 7:
            signal_eight = signal
    
    top = [signal for signal in signal_seven if signal not in signal_one][0]

    unknown_middle_and_left_top = signal_four
    for signal in signal_one:
        unknown_middle_and_left_top = unknown_middle_and_left_top.replace(signal,'')

    two_three_five = [signal for signal in signal_patterns if len(signal) == 5]

    for signal in two_three_five:
        if unknown_middle_and_left_top[0] in signal and unknown_middle_and_left_top[1] in signal:
            signal_five = signal
            two_three_five.remove(signal_five)

    for signal in signal_one:
        if signal in signal_five:
            bottom_right = signal
        else:
            top_right = signal
            
    for signal in two_three_five:
        if top_right in signal and bottom_right in signal:
            signal_three = signal
            two_three_five.remove(signal_three)

    bottom = signal_three
    for signal in signal_four:
        bottom = bottom.replace(signal,'')
    bottom = bottom.replace(top,'')
    
    signal_two = two_three_five[0]

    bottom_left = signal_two
    for signal in signal_three:
        bottom_left = bottom_left.replace(signal, '')

    signal_six = signal_five + bottom_left
    signal_nine = signal_five + top_right

    middle = signal_three.replace(top,'')
    middle = middle.replace(top_right,'')
    middle = middle.replace(bottom_right,'')
    middle = middle.replace(bottom,'')

    for signal in signal_patterns:
        if len(signal) == 6:
            if middle not in signal:
                signal_zero = signal
    
    # signal_zero = top + top_right + top_left + middle + bottom_left + bottom_right + bottom
    
    print('0:', signal_zero)
    print('1:', signal_one)
    print('2:', signal_two)
    print('3:', signal_three)
    print('4:', signal_four)
    print('5:', signal_five)
    print('6:', signal_six)
    print('7:', signal_seven)
    print('8:', signal_eight)
    print('9:', signal_nine)

    print(f"""
 {top*4}
{top_left}    {top_right}
{top_left}    {top_right}
 {middle*4}
{bottom_left}    {bottom_right}
{bottom_left}    {bottom_right}
 {bottom*4}
    """)
    
    output_number = []

    for signal in output_signal_patterns:
        if set(signal) == set(signal_zero):
            output_number.append(0)

        if set(signal) == set(signal_one):
            output_number.append(1)
        
        if set(signal) == set(signal_two):
            output_number.append(2)
                    
        if set(signal) == set(signal_three):
            output_number.append(3)
                    
        if set(signal) == set(signal_four):
            output_number.append(4)
                    
        if set(signal) == set(signal_five):
            output_number.append(5)
                    
        if set(signal) == set(signal_six):
            output_number.append(6)
                    
        if set(signal) == set(signal_seven):
            output_number.append(7)
                    
        if set(signal) == set(signal_eight):
            output_number.append(8)
                    
        if set(signal) == set(signal_nine):
            output_number.append(9)

    print('output_signal_patterns')
    print(output_signal_patterns)

    output = int("".join([str(integer) for integer in output_number]))

    print(output)
    output_sum += output

print(output_sum)

