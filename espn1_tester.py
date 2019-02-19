from espn1 import find_target
import unittest

class TestEspnMethods(unittest.TestCase):

    def test_find_target(self):
        self.assertEqual(find_target(100,50,100),151)

if __name__ == '__main__':
    unittest.main()

