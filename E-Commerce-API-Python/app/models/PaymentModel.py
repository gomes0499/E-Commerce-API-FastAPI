from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class PaymentModel(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    payment_method = Column(String, index=True)
    payment_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, index=True)  # e.g., "Completed", "Pending", "Failed"

    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship("Order", back_populates="payment")