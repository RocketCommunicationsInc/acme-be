from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get("/")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "alive": "true",
        "environment": settings.environment,
        "testing": settings.testing
    }
