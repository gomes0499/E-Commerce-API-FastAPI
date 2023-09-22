from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class ShippingAddress(Base):
    __tablename__ = "shipping_addresses"
    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(255))
    postal_code = Column(String(10))
    country = Column(String(255))


