import unittest
from Day2 import main


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(8, main())  # add assertion here


if __name__ == '__main__':
    unittest.main()
