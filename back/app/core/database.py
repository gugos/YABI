import sqlite3
from contextlib import contextmanager
from typing import Any, Dict, List, Optional
import pandas as pd
from app.core.config import settings


class DatabaseManager:
    """Простой менеджер для работы с SQLite"""
    
    def __init__(self, db_path: str = settings.sqlite_path):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Контекстный менеджер для соединения с БД"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Позволяет обращаться по именам колонок
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """
        Выполняет сырой SQL запрос и возвращает результаты как список словарей
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            
            # Получаем имена колонок
            columns = [description[0] for description in cursor.description] if cursor.description else []
            
            # Преобразуем строки в словари
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            return results
    
    def execute_query_df(self, query: str, params: tuple = ()) -> pd.DataFrame:
        """
        Выполняет запрос и возвращает pandas DataFrame
        """
        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn, params=params)
    
    def get_tables(self) -> List[str]:
        """Возвращает список таблиц в БД"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT name FROM sqlite_master 
                WHERE type='table' AND name NOT LIKE 'sqlite_%'
            """)
            return [row[0] for row in cursor.fetchall()]
    
    def get_table_info(self, table_name: str) -> Dict[str, Any]:
        """Возвращает информацию о таблице"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Получаем схему таблицы
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = []
            for col in cursor.fetchall():
                columns.append({
                    "name": col[1],
                    "type": col[2],
                    "notnull": col[3],
                    "pk": col[5]
                })
            
            # Получаем количество строк
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            
            return {
                "name": table_name,
                "columns": columns,
                "row_count": row_count
            }


# Создаем глобальный экземпляр менеджера БД
db_manager = DatabaseManager()
