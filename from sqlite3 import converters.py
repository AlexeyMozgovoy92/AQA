from four import converter
import unittest

class TestConverterEuro(unittest.TestCase):
    def test_euro(self):
        self.assertEqual(converter(320, "евро"), 100)

class TestConverterDollar(unittest.TestCase):
    def test_dollar(self):
        self.assertEqual(converter(265, "доллар"), 100)  

class TestConverterRur(unittest.TestCase):
    def test_rur(self):
        self.assertEqual(converter(3030, "росруб"), 1)

class TestConverterByn(unittest.TestCase):
    def test_byn(self):
        self.assertEqual(converter(320, "рубли"), 'неправильная валюта')               

if __name__ == "__main__":
    unittest.main()    
