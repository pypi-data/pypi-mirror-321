import unittest
from TAIL.model import Quality

class TestQualityEnum(unittest.TestCase):

    def test_equality(self):
        self.assertTrue(Quality.EXCELLENT == Quality.EXCELLENT)
        self.assertFalse(Quality.EXCELLENT == Quality.GOOD)

    def test_inequality(self):
        self.assertTrue(Quality.EXCELLENT != Quality.GOOD)
        self.assertFalse(Quality.EXCELLENT != Quality.EXCELLENT)

    def test_less_than(self):
        self.assertTrue(Quality.GOOD < Quality.EXCELLENT)
        self.assertFalse(Quality.EXCELLENT < Quality.GOOD)

    def test_less_than_or_equal(self):
        self.assertTrue(Quality.GOOD <= Quality.EXCELLENT)
        self.assertTrue(Quality.EXCELLENT <= Quality.EXCELLENT)
        self.assertFalse(Quality.EXCELLENT <= Quality.GOOD)

    def test_greater_than(self):
        self.assertTrue(Quality.EXCELLENT > Quality.GOOD)
        self.assertFalse(Quality.GOOD > Quality.EXCELLENT)

    def test_greater_than_or_equal(self):
        self.assertTrue(Quality.EXCELLENT >= Quality.GOOD)
        self.assertTrue(Quality.EXCELLENT >= Quality.EXCELLENT)
        self.assertFalse(Quality.GOOD >= Quality.EXCELLENT)

if __name__ == '__main__':
    unittest.main()