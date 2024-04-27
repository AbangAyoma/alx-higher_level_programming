"""importing unittest module so the files can be tested"""

import unittest

"""Importing the module to be tested"""

from models.base import Base

"""writing a test class for the testCase"""
class Test_Base(unittest.TestCase):
    def test_CorrectBase(self):
        obj = Base()
        # result = obj.__init__()
        self.assertEqual(obj, 1)

if __name__ == '__main__':
    unittest.main()
