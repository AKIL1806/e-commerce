from fastapi import APIRouter, HTTPException
from app.models.product import Product, CATEGORIES

router = APIRouter(prefix="/products", tags=["products"])

# In-memory product storage
products_db = []

@router.get("/")
def get_all_products():
    return products_db

@router.get("/category/{category_name}")
def get_products_by_category(category_name: str):
    if category_name not in CATEGORIES:
        raise HTTPException(status_code=400, detail=f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
    return [p for p in products_db if p.category == category_name]

@router.post("/")
def create_product(product: Product):
    product.id = len(products_db)
    products_db.append(product)
    return {"message": "Product added successfully", "product": product}

@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
