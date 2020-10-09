from functools import reduce

with open('input.txt', 'r') as input_file:
    input_str = input_file.read()
    input_str_arr = input_str.split()
    input_arr = list(map(int, input_str_arr))
    
    min_num = None
    max_num = None
    for num in input_arr:
        if min_num is None or min_num > num:
            min_num = num
        if max_num is None or max_num < num:
            max_num = num

    output_str = "{} {}".format(min_num, max_num)
        
    with open('output.txt', 'w+') as output_file:
        output_file.write(output_str)