from mall import Mall


class Store(Mall):

    def __init__(self, name: str = "Cropp", species: str = "street clothes", opening_time_hours: int = 10,
                 opening_time_minutes: int = 0, closing_time_hours: int = 22, closing_time_minutes: int = 30) -> None:
        super().__init__(name, opening_time_hours, opening_time_minutes, closing_time_hours, closing_time_minutes)
        self.species = species

    def __str__(self):
        return f"The name of the store - {self.name}; opening time - " \
               f"{self.opening_time_hours}:{self.opening_time_minutes}; closing time - " \
               f"{self.closing_time_hours}:{self.closing_time_minutes}; species of store - {self.species}."
