class Room:
    CODE = "R"
    
    DEFAULT_WIDTH = 10
    DEFAULT_LENGTH = 10
    DEFAULT_HEIGHT = 3
    
    DEFAULT_WINDOW_COUNT = 1
    WINDOW_SQUARE = 30
    
    DEFAULT_DOOR_COUNT = 1
    DOOR_SQUARE = 16
    
    def __init__(self,
                width = DEFAULT_WIDTH, 
                length = DEFAULT_LENGTH, 
                height = DEFAULT_HEIGHT, 
                doors_count = DEFAULT_DOOR_COUNT, 
                windows_count = DEFAULT_WINDOW_COUNT):
        
        print('You are building Room!')
        
        self.__width = DEFAULT_WIDTH if width is None else width
        self.__length = DEFAULT_LENGTH if length is None else length
        self.__height = DEFAULT_HEIGHT if height is None else height
        self.__doors_count = DEFAULT_DOOR_COUNT if doors_count is None else doors_count
        self.__windows_count = DEFAULT_WINDOW_COUNT if windows_count is None else windows_count
    
    
    # Ширина комнаты
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        if value is None or value <= 0:
            self.__width = value
        else:
            raise ValueError
            

    # Длина комнаты
    @property
    def length(self):
        return self.__length
        
    @length.setter
    def length(self, value):
        if value is None or value <= 0:
            self.__length = value
        else:
            raise ValueError
            
    
    # Высота комнаты
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if value is None or value <= 0:
            raise ValueError
        else:
            self.__height = value
            
           
    # Кол-во дверей в комнате
    @property
    def doors_count(self):
        return self.__doors_count
        
    @doors_count.setter
    def doors_count(self, value):
        if value is None or value <= 0:
            raise ValueError
        else:
            self.__doors_count = value
            
           
    # Кол-во окон в комнате
    @property
    def windows_count(self):
        return self.__windows_count
        
    @windows_count.setter
    def windows_count(self, value):
        if value is None or value <= 0:
            self.__windows_count = value
        else:
            raise ValueError
            
            
    
    def wall_only_square(self):
        return 2 * (self.width + self.length) * self.height
        
    def wall_square(self):
        return self.wall_only_square() - self.windows_count * Room.WINDOW_SQUARE - self.doors_count * Room.DOOR_SQUARE
    
    def __str__(self):
        return '{} ({} x {} x {}, {} windows, {} doors)'.format(
            type(self).__name__, 
            self.width, 
            self.length, 
            self.height, 
            self.windows_count, 
            self.doors_count)
    
    def __del__(self):
        print('You destroyed a ' + self.__str__())