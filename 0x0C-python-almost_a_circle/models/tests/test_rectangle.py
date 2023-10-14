import unittest
from rectangle import Rectangle

class test_rectangle(unittest.TestCase):
    """This class defines unittests"""
    def test_init(self):
        """this method tests the init function of 
        the rect module"""
        r1 = Rectangle(10, 2, 1, 1, 10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        
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
        r3 = Rectangle(10, 2)
        r3.width = 15
        r3.height = 15
        r3.x = 15
        r3.y = 15
        self.assertEqual(r3.width, 15)
        self.assertEqual(r3.height, 15)
        self.assertEqual(r3.x, 15)
        self.assertEqual(r3.y, 15)

    def test_getters(self):
        """this method is used for setting getter functions"""
        r4 = Rectangle(2, 3)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 3)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_area(self):
        """This is a test for finding the area  of the rectangle"""
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.area(), 6)

if __name__ == "__main__":
    unittest.main()
