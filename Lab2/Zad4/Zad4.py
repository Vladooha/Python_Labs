with open('input_1.txt', 'r') as input_1_file:
    with open('input_2.txt', 'r') as input_2_file:
        input1_arr = input_1_file.read().split()
        input2_arr = input_2_file.read().split()
        result_arr = [
            value for value in input2_arr 
                if value not in input1_arr]
        with open('output.txt', 'w+') as output_file:
            output_file.write(' '.join(result_arr))