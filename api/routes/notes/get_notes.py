from fastapi import APIRouter, Depends
from db.functions import authenticate_user, get_notes

router = APIRouter(tags=["Notas"])

@router.get("/nota/coletar")
def coletar_notas(user=Depends(authenticate_user)):
    return get_notes(user["user_id"])