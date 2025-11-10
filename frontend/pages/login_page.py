import streamlit as st
from utils.api_client import api_client
from utils.session_state import login_user, check_backend_status, init_session_state, is_authenticated

# Inicializa o session state
init_session_state()

# Se já estiver logado, redireciona para o app principal
if is_authenticated():
    st.switch_page("app.py")

st.set_page_config(
    page_title="ARAMIS - Login",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def show_login_page():
    """Exibe a tela de login"""
    
    st.title("🔐 Login - ARAMIS")
    st.markdown("---")
    
    # Verifica status do backend
    if not check_backend_status():
        st.error("🚫 Backend offline - Verifique se o servidor está rodando")
        st.info("Execute: `docker-compose up backend` no terminal")
        return
    
    with st.form("login_form"):
        st.subheader("Acesse sua conta")
        
        username = st.text_input("👤 Usuário", placeholder="Digite seu username")
        password = st.text_input("🔒 Senha", type="password", placeholder="Digite sua senha")
        
        col1, col2 = st.columns([4, 4])
        with col1:
            login_button = st.form_submit_button("🚀 Entrar", use_container_width=True)
        with col2:
            register_button = st.form_submit_button("📝 Criar conta", use_container_width=True)
        
        if login_button:
            if not username or not password:
                st.error("⚠️ Preencha todos os campos")
            else:
                with st.spinner("Conectando..."):
                    response = api_client.login(username, password)
                    
                    if response and response.status_code == 200:
                        data = response.json()
                        
                        # 🔥 CORREÇÃO: Pega o token da resposta
                        auth_token = data.get("access_token") or data.get("token")
                        
                        # 🔥 CORREÇÃO: Chama login_user com token
                        login_user(
                            username=data["user"]["username"], 
                            user_id=data["user"]["id"],
                            auth_token=auth_token
                        )
                        st.success(f"✅ Bem-vindo, {data['user']['username']}!")
                        st.switch_page("app.py")
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
    st.caption("Esqueceu sua senha? Entre em contato com o administrador.")

if __name__ == "__main__":
    show_login_page()