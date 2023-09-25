from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    line_items = relationship("LineItem", back_populates="product")
