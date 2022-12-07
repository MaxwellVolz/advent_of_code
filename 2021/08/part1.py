"""
"""

f = open("data.txt")
# f = open("example_data.txt")

test_input = ''.join(f.readlines())
segment_data = test_input.split('\n')

occurrences = 0

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

    for signal in output_signal_patterns:
        sorted_signal = sorted(signal)
        print('signal', signal)
        if sorted_signal == sorted(signal_one) or sorted_signal == sorted(signal_four) or sorted_signal == sorted(signal_seven) or sorted_signal == sorted(signal_eight):
            print('occurrences', occurrences)
            occurrences += 1

    # print('0:', signal_zero)
    # print('1:', signal_one)
    # print('2:', signal_two)
    # print('3:', signal_three)
    # print('4:', signal_four)
    # print('5:', signal_five)
    # print('6:', signal_six)
    # print('7:', signal_seven)
    # print('8:', signal_eight)
    # print('9:', signal_nine)

    # print('\ntop:', top_signal)

print(occurrences)

    # get unique for one and seven

