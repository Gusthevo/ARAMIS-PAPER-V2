import streamlit as st
from utils.api_client import api_client
from utils.session_state import (
    login_user,
    check_backend_status,
    init_session_state,
    is_logged_in
)
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY


# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="ARAMIS - Entrar",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ======================================================
# CSS GLOBAL
# ======================================================
CUSTOM_CSS = """
<style>
    body {
        background-color: #f6f7f9;
        font-family: 'Segoe UI', sans-serif;
    }

    .login-container {
        max-width: 420px;
        margin: auto;
        margin-top: 8vh;
        padding: 2.2rem;
        background-color: rgba(255, 255, 255, 0.6); /* leve transparência */
        border-radius: 14px;
    }

    .login-title {
        text-align: center;
        font-size: 1.9rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #111827;
    }

    .login-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }

    .stTextInput > div > div > input {
        padding: 0.75rem;
        border-radius: 8px;
        border: 1px solid #d1d5db;
    }

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.7rem;
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        color: white;
        border: none;
        transition: background 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #2563eb);
    }

    .footer-text {
        text-align: center;
        font-size: 0.85rem;
        color: #9ca3af;
        margin-top: 1.5rem;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ======================================================
# INIT SESSION + COOKIES
# ======================================================
init_session_state()
cookies = get_cookie_manager()

# Redireciona se já estiver logado
if is_logged_in():
    st.switch_page("app.py")


# ======================================================
# LOGIN PAGE
# ======================================================
def show_login_page():
    """Renderiza a página de login."""

    if not check_backend_status():
        st.error("🚫 Backend offline. Verifique se o servidor está rodando.")
        return

    # Container principal
    st.markdown(
        """
        <div class="login-container">
            <div class="login-title">🔑 Bem-vindo ao ARAMIS</div>
            <div class="login-subtitle">Faça login para acessar o sistema</div>
        """,
        unsafe_allow_html=True
    )

    # Formulário de login
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("👤 Usuário", placeholder="Digite seu username")
        password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")

        st.write("")  # Espaçamento

        col1, col2 = st.columns(2)
        with col1:
            login_button = st.form_submit_button("✅ Entrar", use_container_width=True)
        with col2:
            register_button = st.form_submit_button("📝 Criar conta", use_container_width=True)

        # Ações dos botões
        if login_button:
            if not username or not password:
                st.error("⚠️ Preencha todos os campos.")
            else:
                with st.spinner("🔄 Conectando..."):
                    response = api_client.login(username, password)

                if response and response.status_code == 200:
                    data = response.json()
                    session_token = data.get("session_token")
                    user_info = data.get("user", {})

                    # Salva cookie
                    cookies[AUTH_TOKEN_KEY] = session_token
                    cookies.save()

                    # Atualiza sessão
                    login_user(
                        username=user_info.get("username"),
                        user_id=user_info.get("id"),
                        session_token=session_token
                    )

                    st.rerun()
                else:
                    st.error("❌ Credenciais inválidas.")

        if register_button:
            st.switch_page("pages/signup_page.py")

    # Rodapé
    st.markdown(
        """
            <div class="footer-text">
                ❓ Esqueceu sua senha? Entre em contato com o administrador.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    show_login_page()
