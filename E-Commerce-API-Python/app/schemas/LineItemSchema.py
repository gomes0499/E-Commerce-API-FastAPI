from typing import Optional
from pydantic import BaseModel


class LineItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float


class LineItemCreate(LineItemBase):
    pass


class LineItem(LineItemBase):
    id: int

    class Config:
        orm_mode = True


class LineItemUpdate(BaseModel):
    order_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    price: Optional[float]
