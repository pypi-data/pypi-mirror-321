import sqlite3
from contextlib import contextmanager
from queue import Queue
from typing import Optional, List, Tuple, Any
from datetime import datetime
import uuid
import threading

from clipthread.core.db.utils import ConnectionPool, BaseHandler


class JournalHandler(BaseHandler):
    def __init__(self, db_path: str):
        pool = ConnectionPool(db_path)
        super().__init__(pool)
        self._create_table()

    def _create_table(self):
        with self.get_cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS journal (
                    id TEXT PRIMARY KEY,
                    query TEXT NOT NULL,
                    session_id TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL
                )
            ''')

    def create(self, query: str, session_id: str) -> str:
        new_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        with self.get_cursor() as cursor:
            cursor.execute(
                'INSERT INTO journal (id, query, session_id, created_at) VALUES (?, ?, ?, ?)',
                (new_id, query, session_id, created_at)
            )
        return new_id

    def read(self, journal_id: str) -> Optional[Tuple]:
        with self.get_cursor() as cursor:
            cursor.execute('SELECT * FROM journal WHERE id = ?', (journal_id,))
            row = cursor.fetchone()

        if row:
            return {
                "id": row[0],
                "query": row[1],
                "session_id": row[2],
                "created_at": row[3]
            }

    def update(self, journal_id: str, query: str) -> bool:
        with self.get_cursor() as cursor:
            cursor.execute(
                'UPDATE journal SET query = ? WHERE id = ?',
                (query, journal_id)
            )
            return cursor.rowcount > 0

    def delete(self, journal_id: str) -> bool:
        with self.get_cursor() as cursor:
            cursor.execute('DELETE FROM journal WHERE id = ?', (journal_id,))
            return cursor.rowcount > 0