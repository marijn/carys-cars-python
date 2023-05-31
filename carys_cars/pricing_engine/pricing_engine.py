from moneyed import Money

from carys_cars.pricing_engine.duration_in_minutes import DurationInMinutes


class PricingEngine:
    def __init__(self, price_per_minute: Money) -> None:
        self.__price_per_minute = price_per_minute

    def calculate_price(self, duration: DurationInMinutes) -> Money:
        return self.__price_per_minute * duration.duration_in_minutes
