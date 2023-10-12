import unittest
from rectangle import Rectangle

class test_rectangle(unittest.TestCase):
    """This class defines unittests"""
    def test_init(self):
        """this method tests the init function of 
        the rect module"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        
        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

        with self.assertRaises(TypeError):
            r3 = Rectangle()

        with self.assertRaises(TypeError):
            r4 = Rectangle(1)

    def test_setters(self):
        """this method tests the setter functions"""
        r1 = Rectangle(10, 2)
        r1.width = 15
        r1.height = 15
        r1.x = 15
        r1.y = 15
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.height, 15)
        self.assertEqual(r1.x, 15)
        self.assertEqual(r1.y, 15)
