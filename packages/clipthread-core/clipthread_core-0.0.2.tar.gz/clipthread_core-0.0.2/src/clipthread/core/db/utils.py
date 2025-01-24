import sqlite3
from contextlib import contextmanager
from queue import Queue
from typing import Optional, List, Tuple, Any
from datetime import datetime
import uuid
import threading

from clipthread.core.models.clipboard import ClipboardBase, ClipboardCreate, ClipboardUpdate


class ConnectionPool:
    def __init__(self, db_path: str, max_connections: int = 5):
        self.db_path = db_path
        self.max_connections = max_connections
        self._local = threading.local()
        self._lock = threading.Lock()
        self.active_connections = 0

    def _create_connection(self):
        with self._lock:
            if self.active_connections >= self.max_connections:
                raise Exception("Maximum connections reached")
            self.active_connections += 1
        
        try:
            return sqlite3.connect(self.db_path)
        
        except Exception:
            with self._lock:
                self.active_connections -= 1
            raise


    @contextmanager
    def get_connection(self):
        if not hasattr(self._local, 'connection'):
            self._local.connection = self._create_connection()
        
        try:
            yield self._local.connection

        except Exception as e:
            self._local.connection.rollback()
            raise e
        
        finally:
            if not hasattr(self._local, 'connection'):
                return
            
            with self._lock:
                self.active_connections -= 1

            if self.active_connections == 0:
                self._local.connection.close()
                delattr(self._local, 'connection')

    def close_all(self):
        if hasattr(self._local, 'connection'):
            self._local.connection.close()
            with self._lock:
                self.active_connections -= 1
            delattr(self._local, 'connection')


class BaseHandler:
    def __init__(self, pool: ConnectionPool):
        self.pool = pool

    @contextmanager
    def get_cursor(self):
        with self.pool.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            finally:
                cursor.close()