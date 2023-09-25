from fastapi import FastAPI
from app.api.routes import UserRoute, ProductRoute, OrderRoute, CategoryRoute, InvoiceRoute, LineItemRoute, PaymentRoute, \
    ShippingRoute

app = FastAPI()

app.include_router(UserRoute.router, prefix="/api", tags=["users"])
app.include_router(ProductRoute.router, prefix="/api", tags=["products"])
app.include_router(OrderRoute.router, prefix="/api", tags=["orders"])
app.include_router(CategoryRoute.router, prefix="/api", tags=["categories"])
app.include_router(InvoiceRoute.router, prefix="/api", tags=["invoice"])
app.include_router(LineItemRoute.router, prefix="/api", tags=["lineitem"])
app.include_router(PaymentRoute.router, prefix="/api", tags=["payment"])
app.include_router(ShippingRoute.router, prefix="/api", tags=["shipping"])
