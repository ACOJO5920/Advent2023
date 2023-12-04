import unittest
from Day5 import main


class MyTestCase(unittest.TestCase):
    def test_main_test_1(self):
        self.assertEqual(13, main('Day5Test1.txt'))

    def test_main_input_1(self):
        self.assertEqual(21138, main('Day5Input1.txt'))

    # def test_main_2_test_2(self):
    #     self.assertEqual(30, main_2('Day5Test2.txt'))

    # def test_main_2_input_1(self):
    #     self.assertEqual(0, main_2('Day5Input1.txt'))


if __name__ == '__main__':
    unittest.main()
