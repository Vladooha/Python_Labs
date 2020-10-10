from .room import Room

class Kitchen(Room):
    CODE = "K"

    DEFAULT_KITCHEN_WIDTH = 0
    DEFAULT_KITCHEN_HEIGHT = 0

    def __init__(self,
                width = Room.DEFAULT_WIDTH, 
                length = Room.DEFAULT_LENGTH, 
                height = Room.DEFAULT_HEIGHT,
                doors_count = Room.DEFAULT_DOOR_COUNT, 
                windows_count = Room.DEFAULT_WINDOW_COUNT,
                kitchen_width = DEFAULT_KITCHEN_WIDTH,
                kitchen_height = DEFAULT_KITCHEN_HEIGHT):
        print('You are building Kitchen!')
        Room.__init__(self, width, length, height, doors_count, windows_count)
        self.__kitchen_width = DEFAULT_KITCHEN_WIDTH if doors_count is None else kitchen_width
        self.__kitchen_height = DEFAULT_KITCHEN_HEIGHT if windows_count is None else kitchen_height
    
    # Ширина кухонных шкафов
    @property
    def kitchen_width(self):
        return self.__kitchen_width
        
    @kitchen_width.setter
    def kitchen_width(self, value):
        if value is None or value <= 0:
            self.__kitchen_width = value
        else:
            raise ValueError
            
            
    # Высота кухонных шкафов
    @property
    def kitchen_height(self):
        return self.__kitchen_height
        
    @kitchen_height.setter
    def kitchen_height(self, value):
        if value is None or value <= 0:
            self.__kitchen_height = value
        else:
            raise ValueError 
        

    def wall_square(self, without_kitchen = True):
        if without_kitchen:
            return super().wall_square() - self.kitchen_height * self.kitchen_width
        else:
            return super().wall_square() 