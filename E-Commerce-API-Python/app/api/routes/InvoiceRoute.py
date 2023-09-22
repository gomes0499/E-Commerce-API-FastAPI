from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.InvoiceModel import Invoice
from app.schemas.InvoiceSchema import InvoiceBase, InvoiceCreate, InvoiceUpdate
from app.core.database import SessionLocal

router = APIRouter()


# Dependência para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/invoices/", response_model=InvoiceBase)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


@router.get("/invoices/{invoice_id}", response_model=InvoiceBase)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice


@router.put("/invoices/{invoice_id}", response_model=InvoiceBase)
def update_invoice(invoice_id: int, invoice: InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    for key, value in invoice.dict().items():
        setattr(db_invoice, key, value)

    db.commit()
    db.refresh(db_invoice)
    return db_invoice


@router.delete("/invoices/{invoice_id}", response_model=InvoiceBase)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    db.delete(db_invoice)
    db.commit()
    return db_invoice
