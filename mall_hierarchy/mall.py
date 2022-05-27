class Mall:
    name = "PortCity"
    opening_time = 9.30
    closing_time = 11.00

    def __init__(self, name: str, opening_time_hours: int, opening_time_minutes: int, closing_time_hours: int,
                 closing_time_minutes: int) -> None:
        self.name = name
        self.opening_time_hours = opening_time_hours
        self.opening_time_minutes = opening_time_minutes
        self.closing_time_hours = closing_time_hours
        self.closing_time_minutes = closing_time_minutes

    def __str__(self):
        return f"The name of the mall - {self.name}; opening time - " \
               f"{self.opening_time_hours}:{self.opening_time_minutes}; closing time - " \
               f"{self.closing_time_hours}:{self.closing_time_minutes}."
