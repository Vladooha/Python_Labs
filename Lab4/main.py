from rooms.room import Room
from rooms.bathroom import Bathroom
from rooms.kitchen import Kitchen
from rooms.living_room import LivingRoom

def input_value(value_name, to_int = True):
    if value_name is not None:
        print(value_name)
    value = input()
    if to_int:
        value = int(value)
    
    return value

def test_room():
    print('Creating Room:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    
    my_room = Room(width, length, height, doors, windows)
    print(my_room)
    print('Square: ' + str(my_room.wall_square()))
    print('Only walls square: ' + str(my_room.wall_only_square()))
    del my_room
    
def test_living_room():
    print('Creating LivingRoom:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    
    my_living_room = LivingRoom(width, length, height, doors, windows)
    print(my_living_room)
    print('Square: ' + str(my_living_room.wall_square()))
    print('Only walls square: ' + str(my_living_room.wall_only_square()))
    del my_living_room
    
def test_kitchen():
    print('Creating Kitchen:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    doors = input_value('Input doors count:')
    windows = input_value('Input windows count:')
    kitchen_width = input_value('Input kitchen width:')
    kitchen_height = input_value('Input kitchen height:')
    
    my_kitchen = Kitchen(width, length, height, doors, windows, kitchen_width, kitchen_height)
    print(my_kitchen)
    print('Square: ' + str(my_kitchen.wall_square(without_kitchen = False)))
    print('Square without kitchen: ' + str(my_kitchen.wall_square()))
    print('Only walls square: ' + str(my_kitchen.wall_only_square()))
    del my_kitchen
    
def test_bathroom():
    print('Creating Bathroom:')
    width = input_value('Input width:')
    length = input_value('Input length:')
    height = input_value('Input height:')
    
    my_bathroom = Bathroom(width, length, height)
    print(my_bathroom)
    print('Adding a door...')
    my_bathroom.doors_count += 1
    print(my_bathroom)
    print('Square: ' + str(my_bathroom.wall_square()))
    print('Only walls square: ' + str(my_bathroom.wall_only_square()))
    del my_bathroom    
    

print('Constant value demo: ')
print("Creating Room:")
my_room = Room(width = 8, height = 5)
print(my_room)
print('Adding a door...')
my_room.doors_count += 1
print(my_room)
del my_room

print("Creating Kitchen:")
my_kitchen = Kitchen(kitchen_width = 5, kitchen_height = 2)
print('Wall\'s square with kitchen: '.format(my_kitchen.wall_square(without_kitchen = False)))
print('Wall\'s square without kitchen: '.format(my_kitchen.wall_square()))
del my_kitchen

print("Creating Bathroom:")
my_bathroom = Bathroom(width = 5, height = 2)
print(my_bathroom)
print('Adding a door...')
my_bathroom.doors_count += 1
print(my_bathroom)
del my_bathroom

EXIT_CODE = 'q'
while True:
    try:
        print("-----")
        print('Select room: ')
        print('Room - {}'.format(Room.CODE))
        print('Kitchen - {}'.format(Kitchen.CODE))
        print('Bathroom - {}'.format(Bathroom.CODE))
        print('LivingRoom - {}'.format(LivingRoom.CODE))
        print('To exit type "{}"'.format(EXIT_CODE))
        
        code = input()
        if code is Room.CODE:
            test_room()
        elif code is Kitchen.CODE:
            test_kitchen()
        elif code is Bathroom.CODE:
            test_bathroom()
        elif code is LivingRoom.CODE:
            test_living_room()
        elif code is EXIT_CODE:
            break
        else:
            print('Incorrect input! Try again!')
    except ValueError:
        print('Incorrect input! Try again!')
    