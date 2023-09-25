from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship


class LineItem(Base):
    __tablename__ = 'line_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)

    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    order = relationship("Order", back_populates="line_items")
    product = relationship("Product", back_populates="line_items")
