from fastapi import FastAPI
from app.routes import products, auth
from app.database import database, engine
from app.models import user  # Import your models to register metadata
from fastapi.middleware.cors import CORSMiddleware
from routes.Users import router as UserRouter

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
@app.on_event("startup")
async def startup():
    user.metadata.create_all(bind=engine)  # Create the users table
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routes
app.include_router(products.router)
app.include_router(auth.router)
app.include_router(UserRouter)


@app.get("/")
def root():
    return {"message": "E-Commerce API is live"}
