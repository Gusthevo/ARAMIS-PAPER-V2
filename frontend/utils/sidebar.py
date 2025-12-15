# utils/sidebar.py
import streamlit as st
from utils.session_state import logout_user

def show_sidebar():
    """
    Renderiza a sidebar comum a todas as páginas.
    Gerencia a navegação e o estado da sessão.
    """
    with st.sidebar:
        st.title("ARAMIS")
        st.markdown("---")
        
        # Informações do Usuário
        if "username" in st.session_state:
            st.write(f"👤 **Usuário:** {st.session_state.username}")
            st.write("🟢 **Status:** Conectado")
        
        st.markdown("---")
        st.subheader("Navegação")

        # Botão INÍCIO
        # Se clicado, define a view como 'home' e vai para o main
        if st.button("🏠 Início", use_container_width=True):
            st.session_state["current_view"] = "home"
            st.switch_page("app.py")

        # Botão CORREÇÃO
        # Vai direto para o arquivo de request
        if st.button("📝 Nova Correção", use_container_width=True):
            st.session_state["current_view"] = "request"
            st.switch_page("app.py")

        # Botão PERFIL
        # Define view como 'profile' e vai para o main
        if st.button("👤 Meu Perfil", use_container_width=True):
            st.session_state["current_view"] = "profile"
            st.switch_page("app.py")

        # Botão SOBRE
        # Define view como 'about' e vai para o main
        if st.button("ℹ️ Sobre", use_container_width=True):
            st.session_state["current_view"] = "about"
            st.switch_page("app.py")

        st.markdown("---")
        
        # Botão SAIR
        if st.button("🚪 Sair", use_container_width=True):
            logout_user()
            return False