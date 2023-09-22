from typing import Optional
from pydantic import BaseModel


class InvoiceBase(BaseModel):
    order_id: int
    invoice_date: str


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True


class InvoiceUpdate(BaseModel):
    order_id: Optional[int]
    invoice_date: Optional[str]
