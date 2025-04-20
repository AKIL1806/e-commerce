from fastapi import FastAPI, HTTPException
from app.routes import products
from fastapi.middleware.cors import CORSMiddleware

# Dummy data - move this to a database or proper module later
products_list = [
    {
        "id": 0,
        "name": "MacBook Pro",
        "price": 2499,
        "description": "A high-performance laptop from Apple.",
        "image_url": "https://example.com/macbook.jpg"
    },
    {
        "id": 1,
        "name": "iPhone 15 Pro",
        "price": 1299,
        "description": "The latest iPhone with advanced camera and performance.",
        "image_url": "https://example.com/iphone.jpg"
    },
    # Add more products if needed
]

app = FastAPI()

# CORS config so front-end can talk to the back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origin in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include product routes
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "E-Commerce API is live"}

# New route to get product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if 0 <= product_id < len(products_list):
        return products_list[product_id]
    else:
        raise HTTPException(status_code=404, detail="Product not found")
