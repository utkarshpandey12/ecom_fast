from pydantic import BaseModel
from typing import List


class Catalog(BaseModel):
    name: str
    price: float
    qty: int

class CatalogProduct(Catalog):
    id: str

class PaginationProducts(BaseModel):
    data: list
    page: dict


class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class OrderItem(BaseModel):
    productId: str
    boughtQuantity: int

class ProductsOrder(BaseModel):
    items: List[OrderItem]
    totalAmount: float
    userAddress: UserAddress