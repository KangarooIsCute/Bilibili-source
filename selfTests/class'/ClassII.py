class volume:
    def __init__(self,length,width,height):
        self.__length = length
        self.__width = width
        self.__height = height

    def get_result(self):
        result = self.__length * self.__width * self.__height
        return result

    def set_length(self,length):
        self.__length = length

    def set_width(self,width):
        self.__width = width

    def set_height(self,height):
        self.__height = height