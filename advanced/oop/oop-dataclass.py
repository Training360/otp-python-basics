from dataclasses import dataclass


# default: (init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
#            match_args=True, kw_only=False, slots=False, weakref_slot=False)
@dataclass(slots=True)
class Product:
    name: str
    quantity: int
    price: float

    # def __init__(self, name, quantity, price):
    #     self.name = name
    #     self.quantity = quantity
    #     self.price = price

    def full_price(self) -> float:
        return self.quantity * self.price


p = Product('piros pipongpong labda', 289, 10)
p2 = Product('piros pipongpong labda', 289, 10)
print(p)
print(p == p2)
