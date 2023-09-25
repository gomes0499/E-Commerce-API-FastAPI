from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from ..core.database import Base
from sqlalchemy.orm import relationship


class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float)

    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="invoice")

