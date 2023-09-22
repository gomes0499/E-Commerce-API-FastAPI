from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    user_id: int
    total_price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class OrderUpdate(BaseModel):
    user_id: Optional[int]
    total_price: Optional[float]
