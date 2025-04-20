from fastapi import FastAPI
from app.routes import products
from fastapi.middleware.cors import CORSMiddleware

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
