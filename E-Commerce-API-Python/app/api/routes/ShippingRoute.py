from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.ShippingModel import ShippingAddress
from app.schemas.ShippingSchema import ShippingAddressBase, ShippingAddressCreate, ShippingAddressUpdate
from app.core.database import SessionLocal

router = APIRouter()


# Dependência para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/shipping_addresses/", response_model=ShippingAddressBase)
def create_shipping_address(shipping_address: ShippingAddressCreate, db: Session = Depends(get_db)):
    db_shipping_address = ShippingAddress(**shipping_address.dict())
    db.add(db_shipping_address)
    db.commit()
    db.refresh(db_shipping_address)
    return db_shipping_address


@router.get("/shipping_addresses/{shipping_address_id}", response_model=ShippingAddressBase)
def read_shipping_address(shipping_address_id: int, db: Session = Depends(get_db)):
    db_shipping_address = db.query(ShippingAddress).filter(ShippingAddress.id == shipping_address_id).first()
    if db_shipping_address is None:
        raise HTTPException(status_code=404, detail="Shipping address not found")
    return db_shipping_address


@router.put("/shipping_addresses/{shipping_address_id}", response_model=ShippingAddressBase)
def update_shipping_address(shipping_address_id: int, shipping_address: ShippingAddressUpdate,
                            db: Session = Depends(get_db)):
    db_shipping_address = db.query(ShippingAddress).filter(ShippingAddress.id == shipping_address_id).first()
    if db_shipping_address is None:
        raise HTTPException(status_code=404, detail="Shipping address not found")

    for key, value in shipping_address.dict().items():
        setattr(db_shipping_address, key, value)

    db.commit()
    db.refresh(db_shipping_address)
    return db_shipping_address


@router.delete("/shipping_addresses/{shipping_address_id}", response_model=ShippingAddressBase)
def delete_shipping_address(shipping_address_id: int, db: Session = Depends(get_db)):
    db_shipping_address = db.query(ShippingAddress).filter(ShippingAddress.id == shipping_address_id).first()
    if db_shipping_address is None:
        raise HTTPException(status_code=404, detail="Shipping address not found")

    db.delete(db_shipping_address)
    db.commit()
    return db_shipping_address
