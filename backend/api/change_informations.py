from fastapi import APIRouter, HTTPException, Request
from core.connection import get_db
from core.security import hash_password
from core.security import verify_password
import mysql.connector
import re

router = APIRouter()

@router.put("/edit_user")
async def edit_user(request: Request):
    data = await request.json()
    
    user_id = data.get("id")
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Validações básicas
    if not all([user_id, username, email, password]):
        raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios estarem preenchidos.")

    if " " in username:
        raise HTTPException(status_code=400, detail="O username não deve conter espaços.")
    
    if not "@" in email or ".co" not in email:
        raise HTTPException(status_code=400, detail="Email inválido.")
    
    
    if not re.match(r'^(?=.*[A-Z])(?=.*[\W_]).{8,}$', password):
        raise HTTPException(status_code=400, detail="A senha deve ter no mínimo 8 caracteres, uma letra maiúscula e um símbolo especial.")

    connection = get_db()
    cursor = connection.cursor(dictionary=True)

    try:
        # Verifica se username ou email já existem em outro usuário
        cursor.execute("""
            SELECT id FROM users 
            WHERE (username = %s OR email = %s) AND id != %s
        """, (username, email, user_id))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Username ou email já estão em uso por outro usuário.")

        # Atualiza dados
        hashed_pw = hash_password(password)
        cursor.execute("""
            UPDATE users 
            SET username = %s, email = %s, password_hash = %s 
            WHERE id = %s
        """, (username, email, hashed_pw, user_id))
        connection.commit()

        return {"message": "Informações atualizadas com sucesso"}

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
    finally:
        cursor.close()
        connection.close()
        
@router.put("/delete_user")
async def delete_user(request: Request):
    data = await request.json()
    
    user_id = data.get("id")
    password = data.get("password") 
    
    if not all([user_id, password]):
        raise HTTPException(status_code=400, detail="ID e senha são obrigatórios.")
    
    connection = get_db()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT password_hash FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        
        if not result or not verify_password(password, result["password_hash"]):
            raise HTTPException(status_code=400, detail="A Senha está incorreta, tente novamente")

        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        connection.commit()

        return {"message": "Usuário deletado com sucesso."}

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
    finally:
        cursor.close()
        connection.close()
