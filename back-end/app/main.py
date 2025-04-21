from fastapi import FastAPI
from app.routes import products, auth
from app.database import database
from fastapi.middleware.cors import CORSMiddleware
from app import models

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect DB on startup and disconnect on shutdown
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routes
app.include_router(products.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "E-Commerce API is live"}
