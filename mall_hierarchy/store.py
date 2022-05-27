from mall import Mall


class Store(Mall):
    name = "Cropp"
    species = "street clothes"
    opening_time = 10.00
    closing_time = 22.30

    def __init__(self, name: str, species: str, opening_time_hours: int, opening_time_minutes: int,
                 closing_time_hours: int, closing_time_minutes: int) -> None:
        super().__init__(name, opening_time_hours, opening_time_minutes, closing_time_hours, closing_time_minutes)
        self.species = species

    def __str__(self):
        return f"The name of the store - {self.name}; opening time - " \
               f"{self.opening_time_hours}:{self.opening_time_minutes}; closing time - " \
               f"{self.closing_time_hours}:{self.closing_time_minutes}; species of store - {self.species}."
