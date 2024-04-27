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
		self.__width = value

	@property
	def height(self):
		'''a getter method for the height'''
		return self.__height
	
	@height.setter
	def height(self, value):
		'''a setter method for the height'''
		self.__height = value
	
	@property
	def x(self):
		'''a getter method for x'''
		return self.__x
	
	@x.setter
	def x(self, value):
		'''setter  method for the x attribute'''
		self.__x = value

	@property
	def y(self):
		'''a getter method for y attribute'''
		return self.__y
	@y.setter
	def y(self, value):
		'''a setter method for y attribute'''
		self.__y = value