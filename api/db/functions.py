from db.config.connection import Base, db, Session
from db.config.models import User, Notes
from passlib.hash import bcrypt
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status
from typing import Optional

security = HTTPBasic()

# CRIAR BANCO DE DADOS
def create_db():
    Base.metadata.create_all(db)

# DELETAR USUÁRIO A PARTIR DO ID
def delete_user(user_id: int):
    '''Deleta usuário a partir do ID'''
    session = Session()
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# CRIPTOGRAFAR SENHA
def encrypt_pass(password: str):
    '''Criptografa a senha'''

    pass_crypt = bcrypt.hash(password)

    return pass_crypt

# ADICIONAR DADOS
def add_user(email: str, password: str):
    '''Adiciona usuário ao banco de dados'''
    session = Session()
    try:
        password_crypt = encrypt_pass(password)
        user = User(email=email, password=password_crypt)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# VERIFICAR SE EMAIL E SENHA ESTÃO CORRETOS
# 
# REMOVIDA TEMPORARIAMENTE POIS NÃO É NECESSÁRIA POR AGORA
# 
# def verify_user(email: str, password: str):
#     '''Verifica se o email e senha estão corretos'''
#     session = Session()
#     try:
#         user = session.query(User).filter_by(email=email).first()

#         if not user:
#             return False

#         return bcrypt.verify(password, user.password)
#     finally:
#         session.close()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    """Verifica as credenciais do Basic Auth e retorna os dados do usuário."""
    session = Session()
    try:
        user = session.query(User).filter_by(email=credentials.username).first()

        if not user or not bcrypt.verify(credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas",
                headers={"WWW-Authenticate": "Basic"},
            )

        return {
            "user_id": user.id,
            "email": user.email
        }
    finally:
        session.close()

# ADICIONA UMA NOTA NO BANCO
def add_note(user_id: int, title: str, content: str):
    '''Adiciona uma nota ao banco de dados'''
    session = Session()
    try:
        note = Notes(user_id=user_id, title=title, content=content)
        session.add(note)
        session.commit()
        session.refresh(note)
        return {
            "note_id": note.note_id,
            "user_id": user_id
        }
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# RETORNA TODAS AS NOTAS DE UM USUÁRIO
def get_notes(user_id: int):
    '''Retorna todas as notas do usuário'''
    session = Session()
    try:
        notes = session.query(Notes).filter_by(user_id=user_id).all()
        result = []
        for note in notes:
            result.append({
                "note_id": note.note_id,
                "title": note.title,
                "content": note.content,
                "by": note.user.email,
                "created_at": note.date_time
            })
        return result
    finally:
        session.close()

# RETORNA UMA NOTA ESPECÍFICA
def get_note(note_id: int, user_id: int):
    session = Session()
    try:
        note = session.query(Notes).filter_by(note_id=note_id, user_id=user_id).first()
        if not note:
            raise HTTPException(status_code=404, detail="Nota não encontrada ou esta nota não é sua")

        author = note.user
        result = {
            "note_id": note.note_id,
            "title": note.title,
            "content": note.content,
            "by": author.email,
            "created_at": note.date_time
        }
        return result
    finally:
        session.close()

def delete_note(note_id: int, user_id: int):
    session = Session()
    try:
        note = session.query(Notes).filter_by(note_id=note_id, user_id=user_id).first()
        author = note.user

        if not note:
            raise HTTPException(status_code=404, detail="Nota não encontrada ou esta nota não é sua")
        
        deleted_id = note.note_id
        deleted_title = note.title
        
        session.delete(note)
        session.commit()
        
        return {
            "delete": True,
            "note_id": deleted_id,
            "title": deleted_title,
            "by": author.email
        }
    finally:
        session.close()

def update_note(note_id: int, user_id: int, title: Optional[str] = None, content: Optional[str] = None):
    session = Session()
    try:
        note = session.query(Notes).filter_by(note_id=note_id, user_id=user_id).first()

        if not note:
            raise HTTPException(status_code=404, detail="Nota não encontrada ou esta nota não é sua")

        if title is not None and title != "string" and title != "":
            note.title = title
        if content is not None and content != "string" and content != "":
            note.content = content

        session.commit()
        session.refresh(note)

        return {
            "note_id": note.note_id,
            "title": note.title,
            "content": note.content
        }
    finally:
        session.close()