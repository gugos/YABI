from fastapi import APIRouter, Depends
from datetime import datetime
from app.core.config import settings
from app.schemas.health import HealthCheckResponse

router = APIRouter()


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """Health check endpoint"""
    return HealthCheckResponse(
        status="healthy",
        message="Service is running",
        timestamp=datetime.now(),
        version=settings.app_version,
        service=settings.app_name
    )


@router.get("/test")
async def test_endpoint():
    """Test endpoint for frontend"""
    return {
        "message": "Hello from FastAPI backend!",
        "endpoints": [
            "/api/health",
            "/api/test",
            "/docs",
            "/redoc"
        ],
        "timestamp": datetime.now().isoformat()
    }


@router.get("/data")
async def get_sample_data():
    """Sample data endpoint"""
    return {
        "data": [
            {"id": 1, "name": "Product A", "value": 100, "category": "Electronics"},
            {"id": 2, "name": "Product B", "value": 200, "category": "Books"},
            {"id": 3, "name": "Product C", "value": 150, "category": "Electronics"},
            {"id": 4, "name": "Product D", "value": 300, "category": "Clothing"},
            {"id": 5, "name": "Product E", "value": 250, "category": "Books"},
        ],
        "summary": {
            "total": 5,
            "total_value": 1000,
            "avg_value": 200
        }
    }
