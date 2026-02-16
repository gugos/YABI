from fastapi import APIRouter, HTTPException, Query, Body
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.core.database import db_manager

router = APIRouter()


# Модели запросов/ответов
class QueryRequest(BaseModel):
    query: str
    params: Optional[List[Any]] = []


class QueryResponse(BaseModel):
    success: bool
    data: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None
    row_count: Optional[int] = None
    columns: Optional[List[str]] = None


# Базовые эндпоинты
@router.get("/health")
async def health_check():
    """Проверка здоровья сервиса"""
    try:
        # Проверяем подключение к БД
        tables = db_manager.get_tables()
        return {
            "status": "healthy",
            "database": "connected",
            "tables": tables,
            "tables_count": len(tables)
        }
    except Exception as e:
        return {
            "status": "degraded",
            "database": "disconnected",
            "error": str(e)
        }


@router.get("/tables")
async def get_tables():
    """Получить список всех таблиц"""
    try:
        tables = db_manager.get_tables()
        return {"tables": tables, "count": len(tables)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tables/{table_name}")
async def get_table_info(table_name: str):
    """Получить информацию о конкретной таблице"""
    try:
        info = db_manager.get_table_info(table_name)
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/query", response_model=QueryResponse)
async def execute_query(request: QueryRequest):
    """
    Выполнить сырой SQL запрос
    
    Пример тела запроса:
    {
        "query": "SELECT * FROM combined_data WHERE category = ? LIMIT ?",
        "params": ["Electronics", 10]
    }
    """
    try:
        # Выполняем запрос
        results = db_manager.execute_query(request.query, tuple(request.params))
        
        # Получаем имена колонок из первого результата (если есть)
        columns = list(results[0].keys()) if results else []
        
        return QueryResponse(
            success=True,
            data=results,
            row_count=len(results),
            columns=columns
        )
    except Exception as e:
        return QueryResponse(
            success=False,
            error=str(e)
        )


@router.post("/query/df")
async def execute_query_dataframe(
    query: str = Body(..., embed=True),
    params: List[Any] = Body([], embed=True)
):
    """
    Выполнить запрос и вернуть результат в формате, готовом для графиков
    (автоматическая агрегация числовых данных)
    """
    try:
        df = db_manager.execute_query_df(query, tuple(params))
        
        # Базовая статистика для числовых колонок
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        stats = {}
        for col in numeric_cols:
            stats[col] = {
                "min": float(df[col].min()) if not df[col].empty else None,
                "max": float(df[col].max()) if not df[col].empty else None,
                "mean": float(df[col].mean()) if not df[col].empty else None,
                "sum": float(df[col].sum()) if not df[col].empty else None
            }
        
        return {
            "success": True,
            "data": df.to_dict(orient="records"),
            "columns": df.columns.tolist(),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "stats": stats,
            "shape": df.shape
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@router.get("/query/preview/{table_name}")
async def preview_table(table_name: str, limit: int = Query(10, ge=1, le=1000)):
    """Предпросмотр данных из таблицы"""
    try:
        query = f"SELECT * FROM {table_name} LIMIT ?"
        results = db_manager.execute_query(query, (limit,))
        return {
            "table": table_name,
            "data": results,
            "count": len(results)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
