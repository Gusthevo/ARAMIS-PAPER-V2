import streamlit as st
from utils.api_client import api_client
from utils.session_state import login_user, check_backend_status, init_session_state, is_logged_in
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY


# 👈 CORREÇÃO 1: st.set_page_config DEVE ser o primeiro comando st
st.set_page_config(
    page_title="ARAMIS - Login",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Inicializa o session state e os cookies
init_session_state()
cookies = get_cookie_manager()

# Se já estiver logado (após o st.rerun), redireciona para o app principal
if is_logged_in():
    st.switch_page("app.py")

def show_login_page():
    """Exibe a tela de login"""
    
    st.title("🤝 Bem-vindo ao ARAMIS, realize o seu login para entrar")
    st.markdown("---")
    
    # Verifica status do backend
    if not check_backend_status():
        st.error("🚫 Backend offline - Verifique se o servidor está rodando")
        #st.info("Execute: `docker-compose up backend` no terminal")
        return
    
    with st.form("login_form"):
        st.subheader("Acesse sua conta")
        
        username = st.text_input(f"👤 **Usuário**", placeholder="Digite seu username")
        password = st.text_input(f"🔐 **Senha**", type="password", placeholder="Digite sua senha")
        
        col1, col2 = st.columns([4, 4])
        with col1:
            login_button = st.form_submit_button(f"🚀 **Entrar**", use_container_width=True)
        with col2:
            register_button = st.form_submit_button(f"📝 **Criar conta**", use_container_width=True)
        
        if login_button:
            if not username or not password:
                st.error("⚠️ Preencha todos os campos")
            else:
                with st.spinner("Conectando..."):
                    response = api_client.login(username, password)
                    
                    if response and response.status_code == 200:
                        data = response.json()
                        
                        session_token = data.get("session_token")
                        user_info = data.get("user", {})
                        
                        if not session_token:
                            st.error("❌ Erro: Token de sessão não recebido do backend")
                            return
                        
                        # 1. Salva o cookie
                        cookies[AUTH_TOKEN_KEY] = session_token
                        cookies.save() # Salva o cookie

                        # 2. Faz o login no session_state
                        login_user(
                            username=user_info["username"], 
                            user_id=user_info["id"],
                            session_token=session_token
                        )
                        
                        # st.success(f"✅ Bem-vindo, {user_info['username']}!") # Opcional, pois vai recarregar rápido
                        
                        st.rerun()
                    else:
                        error_msg = "Verifique suas credenciais e tente novamente"
                        if response:
                            try:
                                error_data = response.json()
                                error_msg = error_data.get("detail", "Credenciais inválidas")
                            except:
                                error_msg = "Erro de conexão com o servidor"
                        st.error(f"❌ {error_msg}")
        
        if register_button:
            st.switch_page("pages/signup_page.py")
    
    # Link para recuperação de senha (futuro)
    st.markdown("---")
    st.caption("Esqueceu sua senha? Entre em contato com o administrador do sistema.")

if __name__ == "__main__":
    show_login_page()