import unittest
from Day2 import main_2


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(2286, main_2())  # add assertion here


if __name__ == '__main__':
    unittest.main()
