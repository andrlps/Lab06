from dataclasses import dataclass

@dataclass
class Prodotto:
    number: int
    line: str
    type: str
    product: str
    brand: str
    color: str
    cost: float
    price: float

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)



