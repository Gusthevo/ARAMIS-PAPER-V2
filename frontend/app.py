import streamlit as st
from utils.session_state import init_session_state, logout_user
from pages.login_page import show_login_page
from pages.signup_page import show_register_page
from pages import login_page, signup_page

# Configuração da página
st.set_page_config(
    #Colocar o emoji da aplicação no titulo
    page_title="ARAMIS",
    page_icon="../images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializa estado da sessão
init_session_state()

def show_main_app():
    """Exibe a aplicação principal (após login)"""
    
    # Sidebar com informações do usuário
    with st.sidebar:
        st.title("📚 ARAMIS")
        st.markdown("---")
        
        st.write(f"👤 **Usuário:** {st.session_state.username}")
        st.write("🟢 **Status:** Conectado")
        
        st.markdown("---")
        
        # Navegação
        st.subheader("Navegação")
        menu_option = st.radio(
            "Selecione uma opção:",
            ["🏠 Início", "📝 Correção", "📊 Resultados", "ℹ️ Sobre"]
        )
        
        st.markdown("---")
        if st.button("🚪 Sair", use_container_width=True):
            logout_user()
            st.rerun()
    
    # Conteúdo principal baseado na seleção do menu
    if menu_option == "🏠 Início":
        show_home_page()
    elif menu_option == "📝 Correção":
        show_correction_page()
    elif menu_option == "📊 Resultados":
        show_results_page()
    elif menu_option == "ℹ️ Sobre":
        show_about_page()

def show_home_page():
    """Página inicial da aplicação"""
    st.title("🏠 Página Inicial - ARAMIS")
    st.markdown("---")
    
    st.success(f"Bem-vindo ao ARAMIS, {st.session_state.username}!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **📝 Correção de Texto**
        - Análise gramatical
        - Estrutura acadêmica  
        - Coerência textual
        """)
    
    with col2:
        st.info("""
        **🚀 Como Usar**
        1. Selecione a seção do TCC
        2. Escolha os agentes de análise
        3. Cole seu texto
        4. Receba a correção
        """)
    
    with col3:
        st.info("""
        **📊 Resultados**
        - Histórico de análises
        - Estatísticas de melhorias
        - Relatórios detalhados
        """)
    
    # Card de ação rápida
    st.markdown("---")
    st.subheader("🚀 Iniciar Correção")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Comece agora uma nova análise do seu TCC")
    with col2:
        if st.button("📝 Nova Correção", use_container_width=True):
            st.session_state.current_page = "correction"
            st.rerun()

def show_correction_page():
    """Página de correção (em desenvolvimento)"""
    st.title("📝 Correção de TCC")
    st.markdown("---")
    st.warning("🚧 Funcionalidade em desenvolvimento")
    st.info("Em breve você poderá fazer a correção do seu TCC aqui!")

def show_results_page():
    """Página de resultados (em desenvolvimento)"""
    st.title("📊 Resultados")
    st.markdown("---")
    st.warning("🚧 Funcionalidade em desenvolvimento")

def show_about_page():
    """Página sobre a plataforma"""
    st.title("ℹ️ Sobre o ARAMIS")
    st.markdown("---")
    
    from utils.api_client import api_client
    about_info = api_client.get_about_info()
    
    if about_info:
        platform = about_info.get("platform", {})
        st.header(platform.get("name", "ARAMIS"))
        st.write(platform.get("description", ""))
    else:
        st.info("""
        **ARAMIS** - Sistema Inteligente de Correção de TCCs
        
        Plataforma desenvolvida para auxiliar estudantes na correção 
        e melhoria de seus trabalhos acadêmicos utilizando agentes 
        especializados em análise textual.
        """)

def main():
    # Verifica se está logado
    if not st.session_state.logged_in:
        # Controla qual página de autenticação mostrar
        if st.session_state.current_page == "login":
             st.switch_page("pages/login_page.py") 
        elif st.session_state.current_page == "register":
             st.switch_page("pages/signup_page.py")  # ← Vai para cadastro
    else:
        show_main_app()

if __name__ == "__main__":
    main()