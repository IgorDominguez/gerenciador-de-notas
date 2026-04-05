from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from db.functions import add_note, authenticate_user

class Note_info(BaseModel):
    title: str
    content: str

router = APIRouter(tags=["Notas"])

@router.post("/nota/criar")
async def criar_perfil(item: Note_info, user=Depends(authenticate_user)):
    '''Cadastra o usuário no banco de dados'''
    
    try:
        note = add_note(user['user_id'], item.title, item.content)

        return {
            'note_id': note['note_id'],
            'user_id': note['user_id']
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))