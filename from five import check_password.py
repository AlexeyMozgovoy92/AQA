from five import check_password
import unittest

class TestPasswordSpace(unittest.TestCase):
    def test_space(self):
        self.assertEqual(check_password("Pass word1!"), False)               

class TestPasswordUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(check_password("password1!"), False) 

class TestPasswordLower(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(check_password("PASSWORD1!"), False) 

class TestPasswordDigit(unittest.TestCase):
    def test_digit(self):
        self.assertEqual(check_password("Password!"), False) 

class TestPasswordSymbol(unittest.TestCase):
    def test_symbol(self):
        self.assertFalse(check_password("Password")) 

class TestPasswordAlpha(unittest.TestCase):
    def test_alpha(self):
        self.assertFalse(check_password("!!!!!!!!!")) 

class TestPasswordTrue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_password("Password!2"))


if __name__ == "__main__":
    unittest.main()   