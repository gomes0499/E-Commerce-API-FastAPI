from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ...models.LineItemModel import LineItem
from ...schemas.LineItemSchema import LineItemBase, LineItemCreate, LineItemUpdate
from ...core.database import SessionLocal

router = APIRouter()


# Dependência para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/line_items/", response_model=LineItemBase)
def create_line_item(line_item: LineItemCreate, db: Session = Depends(get_db)):
    db_line_item = LineItem(**line_item.dict())
    db.add(db_line_item)
    db.commit()
    db.refresh(db_line_item)
    return db_line_item


@router.get("/line_items/{line_item_id}", response_model=LineItemBase)
def read_line_item(line_item_id: int, db: Session = Depends(get_db)):
    db_line_item = db.query(LineItem).filter(LineItem.id == line_item_id).first()
    if db_line_item is None:
        raise HTTPException(status_code=404, detail="Line item not found")
    return db_line_item


@router.put("/line_items/{line_item_id}", response_model=LineItemBase)
def update_line_item(line_item_id: int, line_item: LineItemUpdate, db: Session = Depends(get_db)):
    db_line_item = db.query(LineItem).filter(LineItem.id == line_item_id).first()
    if db_line_item is None:
        raise HTTPException(status_code=404, detail="Line item not found")

    for key, value in line_item.dict().items():
        setattr(db_line_item, key, value)

    db.commit()
    db.refresh(db_line_item)
    return db_line_item


@router.delete("/line_items/{line_item_id}", response_model=LineItemBase)
def delete_line_item(line_item_id: int, db: Session = Depends(get_db)):
    db_line_item = db.query(LineItem).filter(LineItem.id == line_item_id).first()
    if db_line_item is None:
        raise HTTPException(status_code=404, detail="Line item not found")

    db.delete(db_line_item)
    db.commit()
    return db_line_item
