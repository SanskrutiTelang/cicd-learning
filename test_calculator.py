import unittest

class TestExample(unittest.TestCase):

    def test_something(self):
        self.assertEqual(1 + 1, 2)

    def test_another_thing(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
