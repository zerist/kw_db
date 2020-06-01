import unittest

class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Set up the test!")

    def tearDown(self):
        print("Tear down the test!")

    def test_case1(self):
        total = 2 + 2
        self.assertEqual(4, total)

if __name__ == '__main__':
    unittest.main()