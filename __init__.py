from products import dao
from typing import List, Dict


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def load(cls, data: Dict) -> 'Product':
        return cls(
            data['id'],
            data['name'],
            data['description'],
            data['cost'],
            data['qty']
        )


def list_products() -> List[Product]:
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: Dict) -> None:
    dao.add_product(product)


def update_qty(product_id: int, qty: int) -> None:
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
