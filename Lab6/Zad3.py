import multiprocessing
import math
import time
from random import uniform

UPPER_NUM = 1000000
LOWER_NUM = -1000000
N = 5000

P = []
Q = []

# Generating few structures for minimizing
# non-math computations
def generate_vector_values():
    global P, Q
    for i in range(N):
        p = uniform(LOWER_NUM, UPPER_NUM)
        q = uniform(LOWER_NUM, UPPER_NUM)
        P.append(p)
        Q.append(q)

def do_math(p, q):
    return 1 / (1 + math.pow(q - p, 2))
    
def do_math_row(p, q_row):
    row = []
    for q in q_row:
        row.append(do_math(p, q))
    return row
    
def do_math_by_arr(p_arr, q_arr, p_begin, p_end):
    matrix = []
    for p in p_arr[p_begin : p_end]:
        matrix_row = []
        for q in q_arr:
            value = do_math(p, q)
            matrix_row.append(value)
        matrix.append(matrix_row)
            
    
def calc_with_single_proccess():
    matrix = []
    for p in P:
        matrix_row = []
        for q in Q:
            value = do_math(p, q)
            matrix_row.append(value)
        matrix.append(matrix_row)
    
def calc_with_multiprocess_rows(process_count):
    global P, Q
    
    args_arr = []
    step = N // process_count
    for i in range(process_count):
        begin = i * step
        end = (i+1) * step - 1 if i != (process_count - 1) else N - 1
        args_arr.append((P, Q, begin, end))
    
    with multiprocessing.Pool(4) as pool:
        matrix_parts = pool.starmap(do_math_by_arr, args_arr)
        return [].extend(matrix_parts)   

def test():
    start_time = time.time()
    generate_vector_values()
    end_time = time.time()
    print('Value generation time: {} s'.format(end_time - start_time))

    start_time = time.time()
    calc_with_single_proccess()
    end_time = time.time()
    print('Single process: {} s'.format(end_time - start_time))

    process_count = 2
    start_time = time.time()
    calc_with_multiprocess_rows(process_count)
    end_time = time.time()
    print('Multiple processes (P array split for {} parts): {} s'.format(process_count, end_time - start_time))
    
    process_count = 4
    start_time = time.time()
    calc_with_multiprocess_rows(process_count)
    end_time = time.time()
    print('Multiple processes (P array split for {} parts): {} s'.format(process_count, end_time - start_time))
    
    process_count = 8
    start_time = time.time()
    calc_with_multiprocess_rows(process_count)
    end_time = time.time()
    print('Multiple processes (P array split for {} parts): {} s'.format(process_count, end_time - start_time))
    
    process_count = 16
    start_time = time.time()
    calc_with_multiprocess_rows(process_count)
    end_time = time.time()
    print('Multiple processes (P array split for {} parts): {} s'.format(process_count, end_time - start_time))

if __name__ == '__main__':
    multiprocessing.freeze_support()
    test()
    