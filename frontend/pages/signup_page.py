import streamlit as st
from utils.api_client import api_client
from utils.session_state import check_backend_status

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="ARAMIS - Criar Conta",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================================
# CSS GLOBAL (ESTILO CLEAN, SEM CARD)
# ======================================================
CUSTOM_CSS = """
<style>
    body {
        background-color: #f6f7f9;
        font-family: 'Segoe UI', sans-serif;
    }

    .register-wrapper {
        max-width: 640px;
        margin: auto;
        margin-top: 8vh;
        background-color: rgba(255, 255, 255, 0.6); /* leve transparência */
        border-radius: 14px;
    }

    .register-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: #111827;
    }

    .register-subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 2.2rem;
    }

    .stTextInput > div > div > input {
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        transition: border 0.2s ease;
    }

    .stTextInput > div > div > input:focus {
        border: 1px solid #2563eb;
        outline: none;
    }

    .stCheckbox > label {
        font-size: 0.9rem;
    }

    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.75rem;
        background: linear-gradient(90deg, #2563eb, #1d4ed8);
        color: white;
        border: none;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
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
# REGISTER PAGE
# ======================================================
def show_register_page():
    st.markdown(
        """
        <div class="register-wrapper">
            <div class="register-title">📝 Cadastro - ARAMIS</div>
            <div class="register-subtitle">
                Crie sua conta para acessar o sistema
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Verifica status do backend
    if not check_backend_status():
        st.error("🚫 Backend offline - Verifique se o servidor está rodando")
        return

    with st.form("register_form"):
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("👤 Usuário*", placeholder="Escolha um username")
        with col2:
            email = st.text_input("📧 Email*", placeholder="seuemail@email.com")

        col1, col2 = st.columns(2)
        with col1:
            password = st.text_input(
                "🔒 Senha*",
                type="password",
                placeholder="Mínimo 6 caracteres, 1 número e 1 caractere especial"
            )
        with col2:
            confirm_password = st.text_input(
                "🔒 Confirmar Senha*",
                type="password",
                placeholder="Digite novamente"
            )

        accept_terms = st.checkbox("Confirmo que todas as informações estão corretas")

        st.write("")  # espaçamento

        col1, col2 = st.columns(2)
        with col1:
            register_button = st.form_submit_button(
                "✅ Criar conta",
                use_container_width=True
            )
        with col2:
            back_button = st.form_submit_button(
                "↩️ Voltar",
                use_container_width=True
            )

        # Validações
        if register_button:
            if not all([username, email, password, confirm_password]):
                st.error("⚠️ Preencha todos os campos obrigatórios")
            elif password != confirm_password:
                st.error("⚠️ As senhas não coincidem")
            elif len(password) < 6:
                st.error("⚠️ A senha deve ter pelo menos 6 caracteres")
            elif not accept_terms:
                st.error("⚠️ Confirme as informações antes de prosseguir")
            else:
                with st.spinner("Criando sua conta..."):
                    response = api_client.register(username, email, password)

                    if response and response.status_code == 200:
                        st.success("✅ Conta criada com sucesso! Faça login.")
                        st.switch_page("pages/login_page.py")
                    else:
                        error_msg = "Erro de conexão, tente novamente"
                        if response:
                            error_msg = response.json().get(
                                "detail", "Erro ao criar conta"
                            )
                        st.error(f"❌ {error_msg}")

        if back_button:
            st.switch_page("pages/login_page.py")

    # Rodapé
    st.markdown(
        """
        <div class="footer-text">
            Já possui conta? Faça login para continuar.
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    show_register_page()
