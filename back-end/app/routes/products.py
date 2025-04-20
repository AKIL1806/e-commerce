from fastapi import APIRouter
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

fake_db = []  # Temporary in-memory store

@router.get("/")
def get_products():
    return fake_db

@router.post("/")
def add_product(product: Product):
    fake_db.append(product)
    return {"message": "Product added", "product": product}
