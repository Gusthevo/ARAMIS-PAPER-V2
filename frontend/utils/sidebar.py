# utils/sidebar.py
import streamlit as st
from utils.session_state import logout_user
import os

def show_sidebar():
    """
    Renderiza a sidebar comum a todas as páginas.
    Gerencia a navegação e o estado da sessão.
    """
    with st.sidebar:
# 1. Pega a pasta onde este arquivo (sidebar.py) está: /seu_projeto/utils
        dir_atual = os.path.dirname(os.path.abspath(__file__))
        # 2. Sobe um nível e entra em images: /seu_projeto/images/logo...
        caminho_logo = os.path.join(dir_atual, "..", "images", "logo-aramis-cropped.png")
        
        # 3. Exibe a imagem (com verificação de segurança)
        if os.path.exists(caminho_logo):
            col_esq, col_img, col_dir = st.columns([1, 2, 1])
            with col_img:
                st.image(caminho_logo, width="stretch")
                #TÍTULO com fonte maior
                st.markdown("""
                <h1 style='text-align: center; margin-top: -20px; margin-bottom: 20px;'>
                    ARAMIS
                </h1>
                """, unsafe_allow_html=True)
        else:
            # Se não achar a imagem, mostra apenas o título para não quebrar
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