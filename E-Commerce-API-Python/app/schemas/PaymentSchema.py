from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    amount: float
    payment_date: str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True


class PaymentUpdate(BaseModel):
    order_id: Optional[int]
    amount: Optional[float]
    payment_date: Optional[str]
