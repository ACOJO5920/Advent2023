import unittest
from Day3 import main


class MyTestCase(unittest.TestCase):
    def test_main_test_1(self):
        self.assertEqual(4361, main('Day3Test1.txt'))

    def test_main_input_1(self):
        self.assertEqual(522726, main('Day3Input1.txt'))

    # def test_main_2_test_2(self):
    #     self.assertEqual(2286, main('Day3Test2.txt'))
    #
    # def test_main_2_input_1(self):
    #     self.assertEqual(2286, main('Day3Input1.txt'))


if __name__ == '__main__':
    unittest.main()
