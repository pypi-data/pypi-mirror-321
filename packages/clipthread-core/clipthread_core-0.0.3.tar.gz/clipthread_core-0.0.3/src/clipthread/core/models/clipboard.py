from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4


class ClipboardBase(BaseModel):
    text: str
    pinned: bool = False

class ClipboardCreate(ClipboardBase):
    pass

class ClipboardUpdate(BaseModel):
    text: Optional[str] = None
    pinned: Optional[bool] = None

class Clipboard(ClipboardBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True