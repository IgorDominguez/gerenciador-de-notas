from fastapi import APIRouter, Depends
from db.functions import authenticate_user, delete_note

router = APIRouter(tags=["Notas"])

@router.delete("/nota/deletar/{note_id}")
def coletar_notas(note_id: int, user=Depends(authenticate_user)):
    return delete_note(note_id, user['user_id'])