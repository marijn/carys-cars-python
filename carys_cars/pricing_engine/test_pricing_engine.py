import unittest

from parameterized import parameterized
from moneyed import Money

from carys_cars.pricing_engine.duration_in_minutes import DurationInMinutes
from carys_cars.pricing_engine.pricing_engine import PricingEngine


class PricingEngineTest(unittest.TestCase):
    @parameterized.expand([
        [Money(0.24, "EUR"), DurationInMinutes(1), Money(0.24, "EUR")],
        [Money(0.24, "EUR"), DurationInMinutes(3), Money(0.72, "EUR")],
        [Money(0.36, "EUR"), DurationInMinutes(1), Money(0.36, "EUR")],
    ])
    def test_it_calculates_price_based_on_duration(
            self,
            price_per_minute: Money,
            trip_duration: DurationInMinutes,
            total_price: Money
    ):
        # Act
        actual = PricingEngine(price_per_minute).calculate_price(trip_duration)

        # Assert
        expected = total_price
        self.assertEqual(expected, actual)

    #def test_it_calculates_price_based_on_duration_including_an_extended_reservation(self):
    #    """
    #    People that rent a car are allowed 20 minutes to reach the Vehicle.
    #    Once those 20 minutes have passed the Reservation is ended in case the Rent has not been started.
    #    Some people need more time, these Customers want to pay money to take longer to reach the Vehicle.
    #    Initially these customers will pay 0,12 EUR/minute of extended reservation.
    #    """
    #    # Arrange
    #    price_per_minute = Money(0.24, "EUR")
    #    trip_duration = DurationInMinutes(10),
    #    total_reservation_time = DurationInMinutes(30),
    #    # total_price = Money(2,88, "EUR")
    #    total_price = Money(0.24 * 10 + (30 - 20) * 0.12, "EUR")
    #
    #    # Act
    #    actual = PricingEngine(price_per_minute).calculate_price(trip_duration, total_reservation_time)
    #
    #    # Assert
    #    expected = total_price
    #    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
