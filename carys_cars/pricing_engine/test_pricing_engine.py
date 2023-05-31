import unittest

from parameterized import parameterized
from moneyed import Money


class DurationInMinutes:
    def __init__(self, duration_in_minutes: int) -> None:
        self.duration_in_minutes = duration_in_minutes


class PricingEngine:
    def calculate_price(self, duration: DurationInMinutes) -> Money:
        return Money(0.24, "EUR") * duration.duration_in_minutes


class PricingEngineTest(unittest.TestCase):
    @parameterized.expand([
        [DurationInMinutes(1), Money(0.24, "EUR")],
        [DurationInMinutes(3), Money(0.72, "EUR")],
    ])
    def test_it_calculates_price_based_on_duration(self, trip_duration: DurationInMinutes, total_price: Money):
        expected = total_price
        actual = PricingEngine().calculate_price(trip_duration)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
