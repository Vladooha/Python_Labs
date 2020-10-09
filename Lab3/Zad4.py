import time

EXIT_CODE = 'q'

def is_even(num):
    return 0 == num % 2

def is_simple(num):
    # There is no simple numbers before 2
    if num < 2:
        return False
    # '1' is first simple number
    if 2 == num:
        return True
    # Even numbers can't be simple    
    if is_even(num):
        return False
    
    is_simple = True
    delimiter = 3
    while delimiter**2 <= num and is_simple:
        if 0 == num % delimiter:
            is_simple = False
        else:
            delimiter += 2
    
    return is_simple

def simple_in_range(begin , end):
    if begin > end:
        temp = begin
        begin = end
        end = temp
        
    simple_nums = []
    for num in range(begin, end):
        if is_simple(num):
            simple_nums.append(num)
    
    return simple_nums
    
    
print('Simple nums finder! Print "q" to exit.')
while True:
    try:
        print('Input first range border (integer): ')
        begin = input()
        if begin == EXIT_CODE:
            break
        begin = int(begin)
        
        print('Input second range border (integer): ')
        end = input()
        if end == EXIT_CODE:
            break
        end = int(end)
        
        begin_time = time.time()
        simple_nums = simple_in_range(begin, end)
        end_time = time.time()
        total_time = end_time - begin_time
        
        print('Answer is: ' + str(simple_nums))
        print('Execution time: {:06.4f} seconds'.format(total_time))
    except ValueError:
        print('Incorrect input! Try again!')