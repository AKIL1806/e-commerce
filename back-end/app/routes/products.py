# app/routes/Products.py

from fastapi import APIRouter, HTTPException
from app.schemas.product import ProductIn, ProductOut
from app.models.product import products, CATEGORIES
from app.database import database
from uuid import UUID, uuid4
from typing import List

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductOut)
async def create_product(product: ProductIn):
    new_product = {
        "id": uuid4(),
        **product.dict()
    }
    query = products.insert().values(**new_product)
    await database.execute(query)
    return new_product

@router.get("/", response_model=List[ProductOut])
async def get_all_products():
    query = products.select()
    return await database.fetch_all(query)

@router.get("/category/{category_name}", response_model=List[ProductOut])
async def get_products_by_category(category_name: str):
    if category_name not in CATEGORIES:
        raise HTTPException(status_code=400, detail=f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
    query = products.select().where(products.c.category == category_name)
    return await database.fetch_all(query)

@router.get("/{product_id}", response_model=ProductOut)
async def get_product_by_id(product_id: UUID):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
