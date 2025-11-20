import streamlit as st
from utils.api_client import api_client
from utils.session_state import check_backend_status

st.set_page_config(
    #Colocar o emoji da aplicação no titulo
    page_title="ARAMIS - Sign Up",
    page_icon = "images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def show_register_page():
    """Exibe a tela de cadastro"""
    
    st.title("📝 Cadastro - ARAMIS")
    st.markdown("---")
    
    # Verifica status do backend
    if not check_backend_status():
        st.error("🚫 Backend offline - Verifique se o servidor está rodando")
       # st.info("Execute: `docker-compose up backend` no terminal")
        return
    
    with st.form("register_form"):
        st.subheader("Crie sua conta")
        
        col1, col2 = st.columns(2)
        with col1:
            username = st.text_input("👤 Usuário*", placeholder="Escolha um username")
        with col2:
            email = st.text_input("📧 Email*", placeholder="seuemail@email.com")
        
        col1, col2 = st.columns(2)
        with col1:
            password = st.text_input("🔒 Senha*", type="password", placeholder="Mínimo 6 caracteres, 1 número e 1 caractere especial")
        with col2:
            confirm_password = st.text_input("🔒 Confirmar Senha*", type="password", placeholder="Digite novamente")
        
        # Termos de uso
        accept_terms = st.checkbox("Verifique se todas as informações foram inseridas corretamente.")
        
        col1, col2 = st.columns([4, 4])
        with col1:
            register_button = st.form_submit_button("✅ Criar conta", use_container_width=True)
        with col2:
            back_button = st.form_submit_button("↩️ Voltar", use_container_width=True)
        
        if register_button:
            if not all([username, email, password, confirm_password]):
                st.error("⚠️ Preencha todos os campos obrigatórios")
            elif password != confirm_password:
                st.error("⚠️ As senhas não coincidem")
            elif len(password) < 6:
                st.error("⚠️ A senha deve ter pelo menos 6 caracteres")
            elif not accept_terms:
                st.error("⚠️ Aceite os termos de uso")
            else:
                with st.spinner("Criando sua conta..."):
                    response = api_client.register(username, email, password)
                    
                    if response and response.status_code == 200:
                        st.success("✅ Conta criada com sucesso! Faça login.")
                        st.switch_page("pages/login_page.py")  # ← Vai para login
                    else:
                        error_msg = "Erro de conexão, tente novamente"
                        if response:
                            error_msg = response.json().get("detail", "Erro ao criar conta")
                        st.error(f"❌ {error_msg}")
        
        if back_button:
            st.switch_page("pages/login_page.py") 

def main():
    show_register_page()

if __name__ == "__main__":
    main()