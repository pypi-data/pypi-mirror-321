import sqlite3
from contextlib import contextmanager
from queue import Queue
from typing import Optional, List, Tuple, Any
from datetime import datetime
import uuid
import threading

from clipthread.core.db.utils import ConnectionPool, BaseHandler
from clipthread.core.models.clipboard import Clipboard, ClipboardBase, ClipboardCreate, ClipboardUpdate


class ClipboardHandler(BaseHandler):
    def __init__(self, db_path: str):
        pool = ConnectionPool(db_path)
        super().__init__(pool)
        self._create_table()

        # self.journalHandler = JournalHandler(db_path)
        # self.configHandler = ConfigHandler(db_path)

    def _create_table(self):
        with self.get_cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clipboard (
                    id TEXT PRIMARY KEY,
                    text TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    pinned BOOLEAN DEFAULT FALSE
                )
            ''')

    def create(self, text: str, pinned: bool = False) -> str:
        new_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()

        query = 'INSERT INTO clipboard (id, text, created_at, pinned) VALUES (?, ?, ?, ?)'

        with self.get_cursor() as cursor:
            cursor.execute(query, (new_id, text, created_at, pinned))
        self._add_to_journal(query)
        return new_id

    def read(self, clip_id: str) -> Optional[Clipboard]:
        with self.get_cursor() as cursor:
            cursor.execute('SELECT * FROM clipboard WHERE id = ?', (clip_id,))
            row = cursor.fetchone()

        if row:
            return Clipboard(id=row[0], text=row[1], created_at=row[2], pinned=row[3])
        
    def read_all(self, limit: Optional[int] = None) -> List[Clipboard]:
        query = 'SELECT * FROM clipboard'
        if limit:
            query += f' LIMIT {limit}'
        
        with self.get_cursor() as cursor:
            cursor.execute(query)

            output = []
            for item in cursor.fetchall():
                output.append(Clipboard(id=item[0], text=item[1], created_at=item[2], pinned=item[3]))
            
            return output

    def update(self, clip_id: str, text: Optional[str] = None, pinned: Optional[bool] = None) -> bool:
        updates = []
        params = []
        if text is not None:
            updates.append("text = ?")
            params.append(text)
        if pinned is not None:
            updates.append("pinned = ?")
            params.append(pinned)
        
        if not updates:
            return False

        params.append(clip_id)
        query = f"UPDATE clipboard SET {', '.join(updates)} WHERE id = ?"
        
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
        
        self._add_to_journal(query)
        return cursor.rowcount > 0

    def delete(self, clip_id: str) -> bool:
        query = 'DELETE FROM clipboard WHERE id = ?'
        with self.get_cursor() as cursor:
            cursor.execute(query, (clip_id,))
        
        self._add_to_journal(query)
        return cursor.rowcount > 0
    
    def clear(self):
        query = 'DELETE FROM clipboard'
        with self.get_cursor() as cursor:
            cursor.execute(query)
        
        self._add_to_journal(query)
        return cursor.rowcount
        
    def _add_to_journal(self, query: str):
        pass
        # server_id = self.configHandler.get('server_id')
        # self.journalHandler.create(query, server_id)