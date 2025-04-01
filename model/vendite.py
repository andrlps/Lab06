from dataclasses import dataclass
from datetime import datetime
from model.metodi import Metodo
from model.prodotti import Prodotto
from model.retailer import Retailer


@dataclass
class Vendita:
    retailer: Retailer
    prodotto: Prodotto
    metodo: Metodo
    data: datetime
    quantity: int
    price: float
    sale_price: float

    def __eq__(self, other):
        return (self.retailer == other.retailer and  self.prodotto == other.prodotto
                and self.metodo == other.metodo)

    def __hash__(self):
        return hash(self.data)

    def __str__(self):
        ricavo = self.sale_price*self.quantity
        return (f"Data: {self.data}; Ricavo: {ricavo}; Retailer: {self.retailer.code}; "
                f"Prodotto: {self.prodotto.number}")



