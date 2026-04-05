from fastapi import APIRouter, Depends
from db.functions import authenticate_user, get_note

router = APIRouter(tags=["Notas"])

@router.get("/nota/coletar/{note_id}")
def coletar_nota(note_id: int, user=Depends(authenticate_user)):
    '''Retorna uma nota específica'''
    return get_note(note_id, user["user_id"])