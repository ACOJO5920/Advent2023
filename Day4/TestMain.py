import unittest
from Day4 import main, main_2


class MyTestCase(unittest.TestCase):
    def test_main_test_1(self):
        self.assertEqual(13, main('Day4Test1.txt'))

    def test_main_input_1(self):
        self.assertEqual(30, main('Day4Input1.txt'))

    def test_main_2_test_2(self):
        self.assertEqual(30, main_2('Day4Test2.txt'))

    # def test_main_2_input_1(self):
    #     self.assertEqual(0, main_2('Day4Input1.txt'))


if __name__ == '__main__':
    unittest.main()
