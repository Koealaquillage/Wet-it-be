from fastapi import APIRouter

router = APIRouter(
    prefix="/weather",
    tags=["weather"]
)

@router.get("/")
async def get_weather():
    return {"message": "This endpoint will provide weather updates!"}
