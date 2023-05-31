import unittest

from moneyed import Money


class PricingEngineTest(unittest.TestCase):
    def test_it_calculates_price_based_on_duration(self):
        expected = Money(0.72, "EUR")
        actual = PricingEngine().calculate_price(DurationInMinutes(3))

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
