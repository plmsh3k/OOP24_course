class Recording:
    def __init__(self, length : int):
        self.__length = length
        
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, new_length):
        self.__length = new_length

the_wall = Recording(43)
print(the_wall.length)
the_wall.length = 44
print(the_wall.length)