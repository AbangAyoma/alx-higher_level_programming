# Rectangle = __import__("9-rectangle").Rectangle

# class Square(Rectangle):
#     def __init__(self, size):
#         self.__size = size
#         Rectangle.__nit__(self.__size, self.__size)
#     # def area(self):
#     #     return self.__size * self.__size
#     def __str__(self):
#         return ("[square]" str(self.__size) + "/" + str(self.__size))


# """size must be private. No getter or setter
# size must be a positive integer, validated by integer_validator
# the area() method must be implemented
# print() should print, and str() should return, the square description: [Square] <width>/<height>"""


"""Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted"""

class MyInt(int):
    def __init__(self, int):
        self.int = int
        if self.int == int:
            return False
        return True