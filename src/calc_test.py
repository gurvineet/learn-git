import unittest
from calc import add, sub

class TestStringMethods(unittest.TestCase):

    def test_add_2arg(self):
        # Make sure 3 + 4 = 7
        self.assertEqual(add(3, 4), 7, 'adding three and four')

    def test_sub_2arg(self):
        # Make sure 4 - 3 = 1. Test
        self.assertEqual(sub(4, 3), 1, 'subtracting three from four')

    def test_sub_3arg(self):
        # Make sure 4 - 3 = 1. Test again
        self.assertEqual(sub(4, 3, 1), 0, 'subtracting one from three from four')


if __name__ == '__main__':
    unittest.main()
