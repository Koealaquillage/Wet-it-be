from fastapi import FastAPI
from app.routers import weather

app = FastAPI()

# Include routers
app.include_router(weather.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to And Wet It Be!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
