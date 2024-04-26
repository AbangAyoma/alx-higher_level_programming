from base import Base
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
		super().__init__
	'''Setting getters and setters for all attribute of the 
    rectanlge class'''
	@property
	def width(self):
        '''getter for the width attribute'''
		return self.__width
	
	@width.setter
    def width(self, value):
        '''setter for the width attribute'''
        self.__width = width
		
    @property
	def height(self):
        """getter for the width attribute"""
		return self.__width
	
	@width.setter
    def height(self, value):
        '''setter for the height attribute'''
        self.__width = width
	
    @property
    def x(self):
        """getter for the x attribute"""
        return self.__x
    
    @x.seter
    def x(self, value):
        '''setter for the x attribute'''
        self.__x = x
    
    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y
    
    @y.seter
    def y(self, value):
        '''setter for the y attribute'''
        self.__y = y