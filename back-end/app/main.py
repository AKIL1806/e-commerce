from fastapi import FastAPI
from app.routes import Products
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Quantum Shop API",
    description="A futuristic eCommerce backend with product categories and detailed routes.",
    version="1.0.0"
)

# CORS config so front-end can talk to the back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include product routes
app.include_router(Products.router)

@app.get("/")
def root():
    return {"message": "E-Commerce API is live"}
