from two import find_min_number
import unittest

class TestFindMinNumber(unittest.TestCase):
    def test_num1_is_min(self):
        self.assertEqual(find_min_number(1, 2, 3), 1)

    def test_num2_is_min(self):
        self.assertEqual(find_min_number(4, 2, 3), 2)
    
    def test_num3_is_min(self):
        self.assertEqual(find_min_number(4, 5, 3), 3)
    
    def test_num4_is_min(self):
        self.assertEqual(find_min_number(3, 3, 3), "все числа равны")
        

if __name__ == "__main__":
    unittest.main()    
