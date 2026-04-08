from fastapi import APIRouter, HTTPException, Response, Request
from core.connection import get_db  
from core.security import hash_password, verify_password
from core.sessions import create_session, delete_session 
import mysql.connector
import re
from core.sessions import get_session


router = APIRouter()
password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$*&@#])[0-9a-zA-Z$*&@#]{8,}$'
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

@router.post("/register")
async def register_user(request: Request):  
    # Extrai dados do JSON
    data = await request.json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if " " in username:
        raise HTTPException(status_code=400, detail= "O username não deve conter espaços.")
    
    elif not all([username, email, password]):
        raise HTTPException(status_code=400, detail="Todos os dados devem estar obrigatoriamente preenchidos")
    
    elif not re.fullmatch(email_pattern, email):
        raise HTTPException(status_code=400, detail="Email inválido, tente novamente.")

    else:
        if not re.fullmatch(password_pattern, password):
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
                "email": user['email'],
            },
            "session_token": session_token
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

@router.get("/me")
async def get_logged_user(request: Request):
    session_token = request.cookies.get("session_token")
    if not session_token:
        raise HTTPException(status_code=401, detail="Usuário não está logado")

    session = get_session(session_token)
    if not session:
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")

    return {
        "id": session["user_id"],
        "username": session["username"]
    }
    
@router.get("/validate-session")
async def validate_session(request: Request):
    # 🔥 PRIMEIRO TENTA PEGAR DO COOKIE (que é como você está usando)
    session_token = request.cookies.get("session_token")
    
    # 🔥 SE NÃO ENCONTRAR NO COOKIE, TENTA NO HEADER
    if not session_token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            session_token = auth_header.replace("Bearer ", "")
    
    if not session_token:
        print("❌ NENHUM TOKEN ENCONTRADO nem no cookie nem no header!")
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    print(f"✅ Token encontrado: {session_token}")
    
    # Use a função get_session que você já tem
    session = get_session(session_token)
    if not session:
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada")
    
    return {
        "valid": True, 
        "user_id": session["user_id"], 
        "username": session["username"],
        "expires_at": session["expires_at"].isoformat()
    }