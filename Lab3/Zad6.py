import time

EXIT_CODE = 'q'
START_CODE = 's'
ITEM_DELIMITER = ' '

def find_intersection(list_of_lists):
    print('Finding intersection of:')
    for index in range(len(list_of_lists)):
        print('#{} {}'.format(index, list_of_lists[index]))

    if 0 == len(list_of_lists):
        return set()
    if 1 == len(list_of_lists):
        return set(list_of_lists[0])
    
    intersec_buffer = set(list_of_lists[0])
    for index in range(1, len(list_of_lists)):
        current_set = set(list_of_lists[index])
        intersec_buffer = current_set & intersec_buffer

    return intersec_buffer
    
print('Monotone list checker! Print "q" to exit.')
list_buffer = []
while True:
    try:
        print('Input list delimited by "{}" or input "{}" to start a check:'.format(ITEM_DELIMITER, START_CODE))
        data = input()
        if data == EXIT_CODE:
            break
        elif data == START_CODE:
            begin_time = time.time()
            intersection = find_intersection(list_buffer)
            end_time = time.time()
            total_time = end_time - begin_time
            
            if 0 == len(intersection):
                print('Intersection is empty')
            else:
                print('Intersection: ' + str(intersection))
            print('Execution time: {:06.4f} seconds'.format(total_time))
            list_buffer = []
            continue
        else:
            item_list = []
            item_str_list = data.split(ITEM_DELIMITER)
            list_buffer.append(item_str_list)
    except ValueError:
        print('Incorrect input! Try again!')
        list_buffer = []