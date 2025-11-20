import streamlit as st
from datetime import datetime, timedelta
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY

def init_session_state():
    """Inicializa o estado da sessão"""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "login"
    if 'backend_online' not in st.session_state:
        st.session_state.backend_online = False
    # 🔥 SESSÃO DO BACKEND
    if 'session_token' not in st.session_state:
        st.session_state.session_token = None
    if 'session_expires' not in st.session_state:
        st.session_state.session_expires = None

def is_session_valid():
    """Verifica se a sessão do backend ainda é válida (localmente)"""
    if not st.session_state.session_token:
        return False
    if st.session_state.session_expires and datetime.now() > st.session_state.session_expires:
        return False
    return True

def is_logged_in():
    """Verifica se o usuário está logado (frontend + backend)"""
    from utils.api_client import api_client
    
    # Primeiro: verificação básica do frontend
    frontend_ok = (st.session_state.logged_in and 
                   st.session_state.username is not None and 
                   st.session_state.user_id is not None and
                   is_session_valid())
    
    if not frontend_ok:
        return False
    
    # Segundo: validação no backend (mais lento, mas mais seguro)
    try:
        return api_client.validate_session()
    except Exception as e:
        print(f"Erro na validação com backend: {e}")
        # Se não conseguiu validar com backend, confia no frontend por enquanto
        return frontend_ok

def login_user(username: str, user_id: int, session_token: str, expires_in_hours: int = 24):
    """Realiza login do usuário com token de sessão do backend"""
    st.session_state.logged_in = True
    st.session_state.username = username
    st.session_state.user_id = user_id
    st.session_state.current_page = "main"
    st.session_state.session_token = session_token
    st.session_state.session_expires = datetime.now() + timedelta(hours=expires_in_hours)

def logout_user():
    """Realiza logout do usuário"""
    from utils.api_client import api_client
    
    # Avisa o backend
    if st.session_state.session_token:
        api_client.logout()
    
    # 🔥 LIMPA O COOKIE
    try:
        cookies = get_cookie_manager()
        if cookies.get(AUTH_TOKEN_KEY):
            del cookies[AUTH_TOKEN_KEY]
            cookies.save()
    except Exception as e:
        print(f"Erro ao limpar cookie: {e}")
    
    # Limpa o frontend (como você já fazia)
    st.session_state.logged_in = False
    st.session_state.username = None
    # ... (limpa todos os campos)

def check_backend_status():
    """Verifica status do backend"""
    from utils.api_client import api_client
    
    with st.spinner("🔍 Verificando conexão com o backend..."):
        backend_online = api_client.check_backend_health()
    
    st.session_state.backend_online = backend_online
    return backend_online