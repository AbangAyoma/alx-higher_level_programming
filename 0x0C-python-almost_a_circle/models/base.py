#!/usr/bin/python3
'''Base class is a class that have a private class attribute __nb_objects = 0'''
class Base():
    '''__nb_object is a private attribute of the class base'''
    __nb_objects = 0
    def __init__(self, id=None):
        '''Initializing the base class
        *arg: id
        The base class takes in one argument'''
        if id is not None:
            '''checking if id is not None
            if the function is called with a number'''
            self.id = id
        
        else:
            '''incrementing the private attribute when id is None'''
            Base.__nb_objects += 1
            '''Assigning the private attribute to id'''
            self.id = Base.__nb_objects