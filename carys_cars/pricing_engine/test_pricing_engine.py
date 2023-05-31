import unittest

from parameterized import parameterized
from moneyed import Money


class DurationInMinutes:
    def __init__(self, duration_in_minutes: int) -> None:
        self.duration_in_minutes = duration_in_minutes


class PricingEngine:
    def __init__(self, price_per_minute: Money) -> None:
        pass

    def calculate_price(self, duration: DurationInMinutes) -> Money:
        price_per_minute = Money(0.24, "EUR")

        return price_per_minute * duration.duration_in_minutes


class PricingEngineTest(unittest.TestCase):
    @parameterized.expand([
        [Money(24, "EUR"), DurationInMinutes(1), Money(0.24, "EUR")],
        [Money(24, "EUR"), DurationInMinutes(3), Money(0.72, "EUR")],
    ])
    def test_it_calculates_price_based_on_duration(
            self,
            price_per_minute: Money,
            trip_duration: DurationInMinutes,
            total_price: Money
    ):
        expected = total_price
        actual = PricingEngine(price_per_minute).calculate_price(trip_duration)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
