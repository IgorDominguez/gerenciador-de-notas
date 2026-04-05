from fastapi import APIRouter, Depends
from db.functions import authenticate_user

router = APIRouter(tags=["Usuário"])

@router.get("/perfil/verificar")
async def verificar_usuario(user_data = Depends(authenticate_user)):
    """Retorna os dados do usuário"""
    return user_data