import unittest
from Day3 import main, main_2


class MyTestCase(unittest.TestCase):
    def test_main_test_1(self):
        self.assertEqual(4361, main('Day3Test1.txt'))

    def test_main_input_1(self):
        self.assertEqual(522726, main('Day3Input1.txt'))


    def test_main_2_test_2(self):
        self.assertEqual(467835, main_2('Day3Test2.txt'))

    def test_main_2_input_1(self):
        self.assertEqual(81721933, main_2('Day3Input1.txt'))


if __name__ == '__main__':
    unittest.main()
