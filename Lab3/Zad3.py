EXIT_CODE = -1
DIGIT_SPACE = 6

def pascal_triangle(previous_row, max_height):
    if max_height < 1:
        print('Incorrect Pascal triangle height: ' + max_height)
        print('Height must be a positive integer!')

    if len(previous_row) == max_height:
        return
    
    if previous_row:
        new_row = [1]
        for i in range(0, len(previous_row) - 1):
            new_row.append(previous_row[i] + previous_row[i+1])
        new_row.append(1)
    else:
        print("Triangle:")
        new_row = [1]
    
    row_offset = ' ' * (int(DIGIT_SPACE / 2)) * (max_height - len(previous_row))
    row_str = ''
    for num in new_row:
        row_str += '{:^{space}}'.format(num, space = int(DIGIT_SPACE))
    print(row_offset + row_str)
    
    pascal_triangle(new_row, max_height)
    return
    
while True:
    try: 
        print('Input heigth of Pascal triangle (height must be a positive integer, type {} to exit): '.format(EXIT_CODE))
        height = input()
        height = int(height)
        
        if EXIT_CODE == height:
            break;
        pascal_triangle([], height)
    except ValueError:
        print('Height must be a positive integer! Try again!')
    except Exception as error:
        print('Unknown error: ' + str(error))
        break