from typing import Optional
from pydantic import BaseModel


class ShippingAddressBase(BaseModel):
    user_id: int
    address: str
    city: str
    state: str
    postal_code: str


class ShippingAddressCreate(ShippingAddressBase):
    pass


class ShippingAddress(ShippingAddressBase):
    id: int

    class Config:
        orm_mode = True


class ShippingAddressUpdate(BaseModel):
    user_id: Optional[int]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
