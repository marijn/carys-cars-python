import unittest

from carys_cars.pricing_engine.duration_in_minutes import DurationInMinutes


class TestDurationInMinutes(unittest.TestCase):
    def test_it_guards_against_negative_DurationInMinutes(self):
        with self.assertRaises(SorryInvalidDurationInMinutes, msg="Sorry, DurationInMinutes should be a positive value of at least 1"):
            DurationInMinutes(-1)


if __name__ == '__main__':
    unittest.main()
