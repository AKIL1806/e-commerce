from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID, uuid4

# Supported categories
CATEGORIES = [
    "mobiles",
    "laptops",
    "books",
    "lamps",
    "dresses",
    "shoes",
    "accessories",
    "furniture",
    "home-appliances",
    "toys",
    "groceries"
]

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    price: float
    image_url: str
    category: str

    @validator("category")
    def validate_category(cls, v):
        if v not in CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(CATEGORIES)}")
        return v

    class Config:
        schema_extra = {
            "example": {
                "name": "MacBook Pro",
                "description": "Powerful laptop from Apple",
                "price": 2499.99,
                "image_url": "https://example.com/macbook.jpg",
                "category": "laptops"
            }
        }
