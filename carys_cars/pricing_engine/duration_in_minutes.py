class DurationInMinutes:
    def __init__(self, duration_in_minutes: int) -> None:
        if duration_in_minutes < 0:
            raise SorryInvalidDurationInMinutes.because_it_should_be_positive()

        self.duration_in_minutes = duration_in_minutes


class SorryInvalidDurationInMinutes(Exception):
    @classmethod
    def because_it_should_be_positive(cls):
        return SorryInvalidDurationInMinutes("Sorry, DurationInMinutes should be a positive value of at least 1")
