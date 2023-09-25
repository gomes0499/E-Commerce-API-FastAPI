from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.utcnow())
    total_price = Column(Float)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    line_items = relationship("LineItem", back_populates="product")
