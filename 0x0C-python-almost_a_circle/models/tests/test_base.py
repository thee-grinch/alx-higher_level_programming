import unittest
from base import Base

class test_base(unittest.TestCase):
    """This is a test Base"""
    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b2 = Base()
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()
