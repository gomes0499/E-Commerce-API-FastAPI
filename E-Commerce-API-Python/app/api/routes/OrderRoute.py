from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.OrderModel import Order
from app.schemas.OrderSchema import OrderBase, OrderCreate, OrderUpdate
from app.core.database import SessionLocal

router = APIRouter()


# Dependência para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/orders/", response_model=OrderBase)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@router.get("/orders/{order_id}", response_model=OrderBase)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.put("/orders/{order_id}", response_model=OrderBase)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    for key, value in order.dict().items():
        setattr(db_order, key, value)

    db.commit()
    db.refresh(db_order)
    return db_order


@router.delete("/orders/{order_id}", response_model=OrderBase)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(db_order)
    db.commit()
    return db_order
