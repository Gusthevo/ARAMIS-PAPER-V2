import streamlit as st

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

def check_backend_status():
    """Verifica status do backend - AGORA COM FEEDBACK VISUAL"""
    from utils.api_client import api_client
    
    # Mostra status de verificação
    with st.spinner("🔍 Verificando conexão com o backend..."):
        backend_online = api_client.check_backend_health()
    
    st.session_state.backend_online = backend_online
    return backend_online

def login_user(username: str, user_id: int):
    """Realiza login do usuário"""
    st.session_state.logged_in = True
    st.session_state.username = username
    st.session_state.user_id = user_id
    st.session_state.current_page = "main"

def logout_user():
    """Realiza logout do usuário"""
    from utils.api_client import api_client
    api_client.logout()
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.user_id = None
    st.session_state.current_page = "login"