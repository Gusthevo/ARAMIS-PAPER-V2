import secrets
from datetime import datetime, timedelta
from typing import Dict

active_sessions: Dict[str, dict] = {}

def create_session(user_id: int, username: str) -> str:
    session_token = secrets.token_urlsafe(32)
    expires_at = datetime.now() + timedelta(hours=24)
    
    active_sessions[session_token] = {
        "user_id": user_id,
        "username": username,
        "expires_at": expires_at
    }
    
    return session_token

def get_session(session_token: str) -> dict:
    if session_token not in active_sessions:
        return None
    
    session = active_sessions[session_token]
    if datetime.now() > session["expires_at"]:
        del active_sessions[session_token]
        return None
    
    return session

def delete_session(session_token: str):
    if session_token in active_sessions:
        del active_sessions[session_token]