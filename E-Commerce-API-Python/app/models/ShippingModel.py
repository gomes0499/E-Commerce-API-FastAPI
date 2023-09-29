from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from ..core.database import Base
from sqlalchemy.orm import relationship


class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"
    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(255))
    postal_code = Column(String(10))
    country = Column(String(255))

    user_id = Column(Integer, ForeignKey('users.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    user = relationship("User", back_populates="shippings")
    orders = relationship("Order", back_populates="shipping", foreign_keys=[order_id])
