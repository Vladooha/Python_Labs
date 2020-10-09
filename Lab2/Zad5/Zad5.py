import csv
import re
import time

symbols_count = {}

with open('input_big.txt', 'r') as input_file:
    begin_time = time.time()
    for input_line in input_file.readlines():
        cyrillic_symbols = re.findall(r'[а-яА-Я]', input_line)
        for symbol in cyrillic_symbols:
            symbol_lowercase = symbol.lower()
            if symbol_lowercase in symbols_count:
                symbols_count[symbol_lowercase] = symbols_count[symbol_lowercase] + 1 
            else:
                symbols_count[symbol_lowercase] = 1 
    end_time = time.time()
    total_time = end_time - begin_time
    
    with open('output.txt', 'w+') as output_file:
        for symbol_item in symbols_count.items():
            output_file.write("{} - {}\n".format(symbol_item[0], symbol_item[1]))
        output_file.write("Time: {:06.4f} seconds".format(total_time))
    