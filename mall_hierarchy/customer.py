class Customer:
    name_of_customer = "Oleh"
    amount_of_good = 16
    type_of_product = "food"

    def __init__(self, name_of_customer: str, amount_of_good: int, type_of_good: str) -> None:
        self.name_of_customer = name_of_customer
        self.amount_of_good = amount_of_good
        self.type_of_product = type_of_good

    def __str__(self):
        return f"Name of customer - {self.name_of_customer}; amount of product - {self.amount_of_good}; type of " \
               f"product - {self.type_of_product}."
