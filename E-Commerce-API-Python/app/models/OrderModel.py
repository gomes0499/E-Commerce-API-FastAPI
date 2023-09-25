from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from ..core.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.utcnow())
    total_price = Column(Float)

    user = relationship("User", back_populates="orders")
    line_items = relationship("LineItem", back_populates="order")
    shipping_address_id = Column(Integer, ForeignKey('shipping_addresses.id'))
    shipping = relationship("ShippingAddress", back_populates="orders")
    invoice = relationship("Invoice", back_populates="order")
    payment = relationship("Payment", back_populates="order")


