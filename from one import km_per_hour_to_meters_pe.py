from oneee import km_per_hour_to_meters_per_second
import unittest

class TestKM(unittest.TestCase):
    def test_km_per_hour(self):
        self.assertEqual(km_per_hour_to_meters_per_second(36), 10)

    def test_zero(self):
        self.assertEqual(km_per_hour_to_meters_per_second(0),0)

    if __name__ == "__main__":
        unittest.main()    
