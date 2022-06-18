class Mall:

    def __init__(self, name: str = "PortCity", opening_time_hours: int = 9, opening_time_minutes: int = 30,
                 closing_time_hours: int = 11, closing_time_minutes: int = 0) -> None:
        self.name = name
        self.opening_time_hours = opening_time_hours
        self.opening_time_minutes = opening_time_minutes
        self.closing_time_hours = closing_time_hours
        self.closing_time_minutes = closing_time_minutes

    def __str__(self):
        return f"The name of the mall - {self.name}; opening time - " \
               f"{self.opening_time_hours}:{self.opening_time_minutes}; closing time - " \
               f"{self.closing_time_hours}:{self.closing_time_minutes}."
