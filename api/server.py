from routes.perfil import register
from routes.perfil import infos
from routes.notes import register_note
from routes.notes import get_notes
from routes.notes import get_note
from routes.notes import delete_note
from routes.notes import update_note
from db.functions import create_db
from fastapi import FastAPI

create_db()

app = FastAPI()

# PERFIL
app.include_router(register.router)
app.include_router(infos.router)

# NOTES
app.include_router(register_note.router)
app.include_router(get_notes.router)
app.include_router(get_note.router)
app.include_router(delete_note.router)
app.include_router(update_note.router)
