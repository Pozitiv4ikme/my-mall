from accounting import Accounting


class Furniture(Accounting.Customer.Good):
    purpose = "crib"
    name = "Oasis"
    producer = "Baby Doom"
    price_in_dollar = 200.25

    def __init__(self, purpose: str, name: str, producer: str, price_in_dollar: float) -> None:
        super().__init__(name, producer, price_in_dollar)
        self.purpose = purpose

    def __str__(self):
        return super(Furniture, self).__str__() \
               + f"purpose - {self.purpose}."
