from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional

from db.functions import update_note, authenticate_user

class Note_info(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

router = APIRouter(tags=["Notas"])

@router.put("/nota/editar")
async def criar_perfil(note_id: int, item: Note_info, user=Depends(authenticate_user)):
    return update_note(note_id, user['user_id'], item.title, item.content)