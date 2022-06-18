from good import Good


class Furniture(Good):

    def __init__(self, purpose: str = "crib", name: str = "Oasis", producer: str = "Baby Doom",
                 price_in_dollar: float = 200.25) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.purpose = purpose

    def __str__(self):
        return super(Furniture, self).__str__() \
               + f"purpose - {self.purpose}."
