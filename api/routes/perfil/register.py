from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db.functions import add_user

class User_credentials(BaseModel):
    email: str
    password: str

router = APIRouter(tags=["Usuário"])

@router.post("/perfil/cadastro")
async def criar_perfil(item: User_credentials):
    '''Cadastra o usuário no banco de dados'''
    
    try:
        user_id = add_user(item.email, item.password)

        return {
            'user_id': user_id
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))