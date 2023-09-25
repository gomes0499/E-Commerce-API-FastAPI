from sqlalchemy import Column, Integer, Float, ForeignKey
from ..core.database import Base
from sqlalchemy.orm import relationship

class LineItem(Base):
    __tablename__ = 'line_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order", back_populates="line_items")
    product = relationship("Product", back_populates="line_items")
