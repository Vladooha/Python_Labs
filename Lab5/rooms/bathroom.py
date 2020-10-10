from .room import Room

class Bathroom(Room):
    CODE = "B"

    def __init__(self,
                width = Room.DEFAULT_WIDTH, 
                length = Room.DEFAULT_LENGTH, 
                height = Room.DEFAULT_HEIGHT):
        print('You are building Bathroom!')
        Room.__init__(self, width, length, height, 1, 0)
     
    # В ванной всегда 1 дверь
    @Room.doors_count.setter
    def doors_count(self, value):
        pass
            
    # В ванной всегда 0 окон
    @Room.windows_count.setter
    def windows_count(self, value):
        pass