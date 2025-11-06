import streamlit as st
from utils.api_client import api_client
from utils.session_state import login_user, check_backend_status

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
        
        col1, col2 = st.columns([1, 3])
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
                        login_user(data["user"]["username"], data["user"]["id"])
                        st.success(f"✅ Bem-vindo, {data['user']['username']}!")
                        st.switch_page("app.py")  # ← Vai para app principal
                        st.rerun() 
                    else:
                        error_msg = "Erro de conexão"
                        if response:
                            error_msg = response.json().get("detail", "Credenciais inválidas")
                        st.error(f"❌ {error_msg}")
        
        if register_button:
            st.switch_page("pages/signup_page.py")  # ← Vai para cadastro
            st.rerun()
    
    # Link para recuperação de senha (futuro)
    st.markdown("---")
    st.caption("Esqueceu sua senha? Entre em contato com o administrador.")
    
def main():
    show_login_page()

if __name__ == "__main__":
    main()
