import csv


class Item:
    pay_rate = 0.8  # the pay rate after 20% disc
    all = []

    def __init__(self, name: str, price, quantity=0):
        # run validations to the received args
        assert price >= 0, f"Price {price} is not greater that zero!"
        assert quantity >= 0, f"Quatity {quantity} is not greater that zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions ti execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    # static method
    @staticmethod
    def is_integer(num):

        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# Item.instantiate_from_csv()
# print(Item.all)


# print(Item.is_integer(7.05))


class Phone(Item):
    pass


phone1 = Phone("jscPhone10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("jscPhonev20", 700, 5)
phone2.broken_phones = 1
