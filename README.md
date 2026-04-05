# Gerenciador de Notas
> Este projeto é apenas para treino pessoal

# Sobre
Este projeto é um gerenciador de notas simples. Ele não tem uma interface gráfica para testar o projeto, apenas a interface padrão do OpenAPI.

# Tecnologias
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**
- **Bcrypt** *na versão 4.0.1*
- **Passlib**

# Como executar
1. Clonar o repositório:
```bash
   git clone https://github.com/IgorDominguez/gerenciador-de-notas.git

   cd gerenciador-de-notas
```

2. Criar e ativar o ambiente virtual (opcional):
```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
```

3. Instalar as dependências:
```bash
   pip install -r requirements.txt
```

4. Rodar o servidor:
```bash
   cd api

   uvicorn server:app --reload
```

O banco de dados `notes.db` será criado automaticamente na primeira execução, dentro de `/api/db`.
Acesse a documentação em: http://localhost:8000/docs ou http://127.0.0.1:8000/docs
