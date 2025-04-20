# app/schemas/product.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID, uuid4
from app.models.product import CATEGORIES

class ProductIn(BaseModel):
    name: str
    description: Optional[str]
    price: float
    image_url: Optional[str]
    category: str

    @validator("category")
    def validate_category(cls, v):
        if v not in CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
        return v

class ProductOut(ProductIn):
    id: UUID
