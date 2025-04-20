# app/models/product.py
from sqlalchemy import Table, Column, String, Float, MetaData
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()

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

products = Table(
    "products",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", String, nullable=False),
    Column("description", String),
    Column("price", Float, nullable=False),
    Column("image_url", String),
    Column("category", String, nullable=False)
)
