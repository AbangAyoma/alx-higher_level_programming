#!/usr/bin/python3

'''importing a module from models called base with a class of Base'''

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
		self.__height = height
		self.__x = x
		self.__y = y
		super().__init__(id)

	'''Setting getters and setters for all attribute of the 
    	rectanlge class'''

	@property
	def width(self):
		'''a getter method for the width'''
		return self.__width
	
	@width.setter
	def width(self, value):
		'''a setter method for the width'''
		if type(value) != int:
			"""validation of all setter methods and instantiation"""
			raise TypeError("width must be an integer.")
		elif self.__width <= 0:
			'''checkng If width or height is under or equals 0'''
			raise ValueError("width must be > 0.")
		else:
			self.__width = value

	@property
	def height(self):
		'''a getter method for the height'''
		return self.__height
	
	@height.setter
	def height(self, value):
		'''a setter method for the height'''
		if type(value) != int:
			"""validation of all setter methods and instantiation"""
			raise TypeError("height must be an integer.")
		elif self.__height <= 0:
			'''checkng If width or height is under or equals 0'''
			raise ValueError("height must be > 0.")
		else:
			self.__height = value
	
	@property
	def x(self):
		'''a getter method for x'''
		return self.__x
	
	@x.setter
	def x(self, value):
		'''setter  method for the x attribute'''
		if type(value) != int:
			"""validation of all setter methods and instantiation"""
			raise TypeError("x  must be an integer.")
		elif self.__x <= 0:
			'''checkng If width or height is under or equals 0'''
			raise ValueError("x must be > 0.")
		else:
			self.__x = value

	@property
	def y(self):
		'''a getter method for y attribute'''
		return self.__y
	@y.setter
	def y(self, value):
		'''a setter method for y attribute'''
		if type(value) != int:
			"""validation of all setter methods and instantiation"""
			raise TypeError("y  must be an integer.")
		elif self.__y <= 0:
			'''checkng If width or height is under or equals 0'''
			raise ValueError("y must be > 0.")
		else:
			self.__y = value
	