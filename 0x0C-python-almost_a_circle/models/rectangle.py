from models.base import Base
"""A class called Rectangle that inherits from the Base class"""
class Rectangle(Base):
	"""the class takes private attributes"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""Instantiation of the class
		*args: 
		width: the width 
		height: the height 
		then x and y"""
		self.__width = width
		self.height = height
		self.__x = x
		self.__y = y
		super().__init__(id)
	'''Setting getters and setters for all attribute of the 
    rectanlge class'''
	@property
	def width(self):
		return self.__width
	
	@width.setter
    def width(self, value):
        self.__width = value
    
    @property
	def height(self):
		return self.__width
	
	@width.setter
    def height(self, value):
        self.__width = value
	
    @property
    def x(self):
        return self.__x
    
    @x.seter
    def x(self, value):
        '''setter for the x attribute'''
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.seter
    def y(self, value):
        self.__y = value
    
