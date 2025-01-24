import sqlite3
from contextlib import contextmanager
from queue import Queue
from typing import Optional, List, Tuple, Any
from datetime import datetime
import uuid
import threading

from clipthread.core.db.utils import ConnectionPool, BaseHandler


class ConfigHandler(BaseHandler):
    def __init__(self, pool: ConnectionPool):
        super().__init__(pool)
        self._create_table()
        self._init_server_id()

    def _create_table(self):
        with self.get_cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS config (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            ''')

    def set(self, key: str, value: str) -> None:
        with self.get_cursor() as cursor:
            cursor.execute(
                'INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)',
                (key, value)
            )

    def get(self, key: str) -> Optional[str]:
        with self.get_cursor() as cursor:
            cursor.execute('SELECT value FROM config WHERE key = ?', (key,))
            result = cursor.fetchone()
            return result[0] if result else None
        
    def _init_server_id(self) -> None:
        if self.get('server_id') is None:
            self.set('server_id', str(uuid.uuid4()))