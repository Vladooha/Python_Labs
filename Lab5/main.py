import pickle
import random
import os
from rooms.room import Room
from rooms.bathroom import Bathroom
from rooms.kitchen import Kitchen
from rooms.living_room import LivingRoom

EXIT_CODE = 'q'
SAVE_CODE = 's'
LOAD_CODE = 'l'
TEST_CODE = 't'

def input_value(value_name = None, to_int = True):
    if value_name is not None:
        print(value_name)
    value = input()
    if to_int:
        value = int(value)
    
    return value
    
def dump(my_room, filename = None):
    if filename is None:
        filename = input_value('Input filename:')
    try: 
        filename = os.path.dirname(os.path.realpath(__file__)) + os.sep + filename
        with open(filename, 'wb+') as file:
            pickle.dump(my_room, file)
    except OSError:
        print('Can\'t open file {}'.format(filename))
    except Exception as e:
        print('Incorrect class for dumping! {}'.format(str(e)))
        
def load_room(filename = None):
    try:
        if filename is None:
            filename = input_value('Input filename:')
        filename = os.path.dirname(os.path.realpath(__file__)) + os.sep + filename
        with open(filename, 'rb') as file:
            my_room = pickle.load(file)
            print('-----')
            print('Loaded:')
            print(my_room)
            print('-----')
            
            return my_room
    except OSError:
        print('Can\'t open file {}'.format(filename))
    except Exception:
        print('Invalid binary file!')
   
def test():
    type_code = random.choice([Room.CODE, Kitchen.CODE, Bathroom.CODE, LivingRoom.CODE])
    width = random.randint(5, 10)
    length = random.randint(5, 10)
    height = random.randint(5, 10)
    doors = random.randint(5, 10)
    windows = random.randint(5, 10)
    kitchen_width = random.randint(5, 10)
    kitchen_height = random.randint(5, 10)
    
    if type_code is Kitchen.CODE:
        my_room = Kitchen(width, length, height, doors, windows, kitchen_width, kitchen_height)
    elif type_code is Bathroom.CODE:
        my_room = Bathroom(width, length, height)
    elif type_code is LivingRoom.CODE:
        my_room = LivingRoom(width, length, height, doors, windows)
    else:
        my_room = Room(width, length, height, doors, windows)
        
    print('-----')
    print('Saving:')
    print(my_room)
    print('-----')
    
    dump(my_room, "test.room")
    my_room_loaded = load_room("test.room")
    
    try:
        assert type(my_room).__name__ == type(my_room_loaded).__name__, ('Type is incorrect!')
        assert my_room.width == my_room_loaded.width, 'Width is incorrect!'
        assert my_room.height == my_room_loaded.height, 'Height is incorrect!'
        
        print('Test successfully passed!')
    except AssertionError:
        print('Test passed with error!')
   
def save_room():
    print('Creating Room:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    
    my_room = Room(width, length, height, doors, windows)
    print('-----')
    print(my_room)
    print('-----')
    
    dump(my_room)
    
def save_living_room():
    print('Creating LivingRoom:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    
    my_living_room = LivingRoom(width, length, height, doors, windows)
    print('-----')
    print(my_living_room)
    print('-----')
    
    dump(my_living_room)
    
    
def save_kitchen():
    print('Creating Kitchen:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    kitchen_width = input_value('Input kitchen width:')
    kitchen_height = input_value('Input kitchen height:')
    
    my_kitchen = Kitchen(width, length, height, doors, windows, kitchen_width, kitchen_height)
    print('-----')
    print(my_kitchen)
    print('-----')
    
    dump(my_kitchen)
    
    
def save_bathroom():
    print('Creating Bathroom:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    
    my_bathroom = Bathroom(width, length, height)
    print('-----')
    print(my_bathroom)
    print('-----')
    
    dump(my_bathroom)

def save_room():
    print('Select room: ')
    print('Room - {}'.format(Room.CODE))
    print('Kitchen - {}'.format(Kitchen.CODE))
    print('Bathroom - {}'.format(Bathroom.CODE))
    print('LivingRoom - {}'.format(LivingRoom.CODE))
    print('Type "{}" to go to main menu'.format(EXIT_CODE))
    code = input_value()
    
    if code is Room.CODE:
        save_room()
    elif code is Kitchen.CODE:
        save_kitchen()
    elif code is Bathroom.CODE:
        save_bathroom()
    elif code is LivingRoom.CODE:
        save_living_room()
    elif code is EXIT_CODE:
        return
    else:
        print('Incorrect input! Try again!')
        

while True:
    try:
        print('Select action: ')
        print('Save room - {}'.format(SAVE_CODE))
        print('Load room - {}'.format(LOAD_CODE))
        print('Autotest - {}'.format(TEST_CODE))
        print('Type "{}" to exit'.format(EXIT_CODE))
        code = input_value(to_int = False)
        if code is SAVE_CODE:
            save_room()
        elif code is LOAD_CODE:
            load_room()
        elif code is TEST_CODE:
            test()
        elif code is EXIT_CODE:
            break
        else:
            print('Incorrect input! Try again!')
    except ValueError:
        print('Incorrect input! Try again!')
    