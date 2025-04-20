# back-end/app/routes/products.py
from fastapi import APIRouter, HTTPException
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

fake_db = []  # Temporary in-memory store

@router.get("/")
def get_products():
    return fake_db

@router.get("/{product_id}")
def get_product(product_id: int):
    for product in fake_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/")
def add_product(product: Product):
    fake_db.append(product)
    return {"message": "Product added", "product": product}
