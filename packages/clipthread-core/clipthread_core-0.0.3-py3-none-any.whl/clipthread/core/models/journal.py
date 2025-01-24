from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4


class JournalBase(BaseModel):
    query: str
    session_id: str

class JournalCreate(JournalBase):
    pass

class JournalUpdate(BaseModel):
    query: str

class Journal(JournalBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True