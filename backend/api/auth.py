from fastapi import APIRouter, HTTPException, Response, Request
from core.connection import get_db  
from core.security import hash_password, verify_password
from core.sessions import create_session, delete_session 
import mysql.connector
import re

router = APIRouter()

@router.post("/register")
async def register_user(request: Request):  
    # Extrai dados do JSON
    data = await request.json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if " " in username:
        raise HTTPException(status_code=400, detail= "O username não deve conter espaços.")
    
    if not all([username, email, password]):
        raise HTTPException(status_code=400, detail="Todos os dados devem estar obrigatoriamente preenchidos")
    
    if not "@" in email or ".co" not in email:
        raise HTTPException(status_code=400, detail="Email inválido.")
    

    if not re.match(r'^(?=.*[A-Z])(?=.*[\W_]).{8,}$', password):
        raise HTTPException(status_code=400, detail="A senha deve ter no mínimo 8 caracteres, uma letra maiúscula e um símbolo especial.")
    
    connection = get_db() 
    cursor = connection.cursor(dictionary=True)
    
    try:
        # Verifica se usuário já existe
        cursor.execute("SELECT id FROM users WHERE username = %s OR email = %s", 
                      (username, email))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Usuário ou email já existe")
        
        
        # Cria usuário
        hashed_pw = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hashed_pw)
        )
        connection.commit()
        
        return {"message": "Usuário criado com sucesso"}
        
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
    finally:
        cursor.close()
        connection.close()

@router.post("/login")
async def login_user(request: Request, response: Response):  
    # Extrai dados do JSON
    data = await request.json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username e password são obrigatórios")
    
    connection = get_db() 
    cursor = connection.cursor(dictionary=True)
    
    try:
        # Busca usuário
        cursor.execute(
            "SELECT id, username, email, password_hash FROM users WHERE username = %s", 
            (username,)
        )
        user = cursor.fetchone()
        
        if not user or not verify_password(password, user['password_hash']):
            raise HTTPException(status_code=401, detail="Credenciais inválidas, verifique se digitou corretamente ou se o usuário existe")
        
        # Cria sessão
        session_token = create_session(user['id'], user['username'])
        
        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,
            max_age=86400,  # 24 horas
            secure=False
        )
        
        return {
            "message": "Login realizado",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email']
            }
        }
        
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
    finally:
        cursor.close()
        connection.close()
        
        
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT id, username, email, created_at FROM users WHERE id = %s",
            (user_id,)
        )
        user = cursor.fetchone()

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        return user

    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro no banco: {e}")
    finally:
        cursor.close()
        connection.close()

@router.post("/logout")
async def logout_user(request: Request, response: Response): 
    session_token = request.cookies.get("session_token")  
    
    if session_token:
        delete_session(session_token)
    
    response.delete_cookie("session_token")
    return {"message": "Logout realizado"}