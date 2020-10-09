import time

EXIT_CODE = 'q'
START_CODE = 's'
NUM_DELIMITER = ' '

def is_monotone(num_list):
    print('Checking list ' + str(num_list))

    if len(num_list) < 3:
        return True
    
    is_not_desc = num_list[0] <= num_list[1]
    
    for index in range(1, len(num_list) - 1):
        current = num_list[index]
        next = num_list[index + 1]
        if is_not_desc and next < current:
            return False
        elif not is_not_desc and current < next:
            return False
    
    return True
    
print('Monotone list checker! Print "q" to exit.')
num_list_buffer = []
while True:
    try:
        print('Input one or more nums from list delimited by "{}" or input "{}" to start a check:'.format(NUM_DELIMITER, START_CODE))
        data = input()
        if data == EXIT_CODE:
            break
        elif data == START_CODE:
            begin_time = time.time()
            is_monotone_list = is_monotone(num_list_buffer)
            end_time = time.time()
            total_time = end_time - begin_time
            
            print('Is monotone: ' + str(is_monotone_list))
            print('Execution time: {:06.4f} seconds'.format(total_time))
            num_list_buffer = []
            continue
        else:
            num_str_list = data.split(NUM_DELIMITER)
            for num_str in num_str_list:
                num_list_buffer.append(int(num_str))
    except ValueError:
        print('Incorrect input! Try again!')
        num_list_buffer = []