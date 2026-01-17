class Square:
    def __init__(self, length = 5):
        if length < 0:
            length = -length
        self.__length = length
        self.__ch = '*'

    def get_length(self):
        return self.__length

    def get_ch(self):
        return self.__ch

    def set_length(self, length):
        if length < 0:
            length = -length
        self.__length = length

    def set_ch(self, ch):
        self.__ch = ch

    def calc_area(self):
        return self.__length * self.__length

    def calc_perimeter(self):
        return self.__length * 4

    def __str__(self):
        shape_str = ""
        for i in range(self.__length):
            for j in range(self.__length):
                shape_str += self.__ch
            shape_str += "\n"
        return shape_str



