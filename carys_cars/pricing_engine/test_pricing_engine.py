import unittest

from moneyed import Money


class DurationInMinutes:
    def __init__(self, duration_in_minutes: int) -> None:
        pass


class PricingEngine:
    def calculate_price(self, duration: DurationInMinutes) -> Money:
        return Money(0.72, "EUR")


class PricingEngineTest(unittest.TestCase):
    def test_it_calculates_price_based_on_duration(self):
        expected = Money(0.72, "EUR")
        actual = PricingEngine().calculate_price(DurationInMinutes(3))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
