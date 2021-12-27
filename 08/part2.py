"""
"""

# f = open("data.txt")
# f = open("example_data.txt")
f = open("example_data2.txt")

test_input = ''.join(f.readlines())
segment_data = test_input.split('\n')

occurrences = 0

def signal_must_contain(signals, requirement):
    temp_signals = []


for line in segment_data:
    all_entries = line.split() 

    signal_patterns = all_entries[:all_entries.index('|')]
    output_signal_patterns = all_entries[all_entries.index('|')+1:]

    print(signal_patterns)
    print(output_signal_patterns)

    signal_one = [signal for signal in signal_patterns if len(signal) == 2][0]
    signal_seven = [signal for signal in signal_patterns if len(signal) == 3][0]

    top_signal = [signal for signal in signal_seven if signal not in signal_one][0]

    signal_four = [signal for signal in signal_patterns if top_signal not in signal and len(signal)!=2][0]
    # find 

    signal_eight = [signal for signal in signal_patterns if len(signal) == 7][0]

    signal_zero = ''
    signal_two = ''
    signal_three = ''
    signal_five = ''
    signal_six = ''
    signal_nine = ''


    top_left = ''
    middle = ''
    bottom_left = ''
    bottom = ''

    # knowing the top and 4, compare with 8
    # the remaining wires correspond with the bottom and bottom left
    four_plus = signal_four + top_signal
    bottom_bottom_left = ''

    for signal in signal_eight:
        if signal not in four_plus:
            bottom_bottom_left += signal
            
    for signal in signal_patterns:
        if len(signal) == 5 and bottom_bottom_left[0] in signal and bottom_bottom_left[1] in signal:
            signal_two = signal

    top_right = ''
    for signal in signal_two:
        if signal in signal_one:
            top_right = signal

    bottom_right = signal_one.replace(top_right, '')

    # for signal in signal_patterns:
        
    print('top_right:', top_right)
    print('bottom_right:', bottom_right)


    for signal in signal_patterns:
            if len(signal) == 5 and signal != signal_two:
                if top_right in signal:
                    signal_three = signal
                else:
                    signal_five = signal

    middle = ''
    for signal in signal_zero:
        print(signal, 'in', signal_three)
        if signal not in signal_three:
            middle = signal

    # diff 4 and 9, remove top

    # for signal in signal_nine:
    #     four_plus_top = signal_four + top_signal
    #     print(signal, 'in', four_plus_top)
    #     if signal not in four_plus_top:
    #         bottom = signal

    # for signal in output_signal_patterns:
    #     sorted_signal = sorted(signal)
    #     print('signal', signal)
    #     if sorted_signal == sorted(signal_one) or sorted_signal == sorted(signal_four) or sorted_signal == sorted(signal_seven) or sorted_signal == sorted(signal_eight):
    #         print('occurrences', occurrences)
    #         occurrences += 1

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
 {top_signal*4}
{top_left}     {top_right}
{top_left}     {top_right}
 {middle*4}
{bottom_left}     {bottom_right}
{bottom_left}     {bottom_right}
 {bottom*4}
    """)

# print(occurrences)

    # get unique for one and seven

