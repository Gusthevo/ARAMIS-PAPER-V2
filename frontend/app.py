import streamlit as st
from utils.session_state import init_session_state, logout_user, login_user
from utils.session_state import is_logged_in
from utils.api_client import api_client 
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY 


# Configuração da página
st.set_page_config(
    page_title="ARAMIS",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializa estado da sessão
init_session_state()
cookies = get_cookie_manager()

def show_main_app():
    """Exibe a aplicação principal (após login)"""
    
    # Sidebar com informações do usuário
    with st.sidebar:
        st.title("ARAMIS")
        st.markdown("---")
        
        st.write(f"👤 **Usuário:** {st.session_state.username}")
        st.write("🟢 **Status:** Conectado")
        
        st.markdown("---")
        
        # Navegação
        st.subheader("Navegação")
        menu_option = st.radio(
            "Selecione uma opção:",
            ["🏠 Início", "📝 Correção", "📊 Resultados", "👤 Meu Perfil", "ℹ️ Sobre"]
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
    elif menu_option == "👤 Meu Perfil":
        show_profile_page()
    elif menu_option == "ℹ️ Sobre":
        show_about_page()

def show_home_page():
    """Página inicial da aplicação"""
    col1, col2 = st.columns([6, 1])

    with col1:
        st.title("🏠 Página Inicial - ARAMIS")

    with col2:
        if st.button("🚪 Sair"):
            logout_user()
            st.rerun()

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
            # Muda para página de correção via session state
            pass  # Sua lógica aqui

def show_correction_page():
    st.switch_page("pages/request_page.py")

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
    

def attempt_login_from_cookie():
    """
    Tenta logar o usuário se um cookie de token válido for encontrado.
    Isso é o que "sobrevive" ao F5.
    """
    
    # 1. Se já estamos logados no session_state, não faz nada
    if st.session_state.logged_in:
        return True
    
    # 2. Busca o token no cookie
    token_from_cookie = cookies.get(AUTH_TOKEN_KEY)
    
    if token_from_cookie:
        # 3. Encontramos um token. Coloca-o no session_state para o api_client usar
        st.session_state.session_token = token_from_cookie
        
        try:
            # Chamamos a api_client.validate_session() MODIFICADA
            # (Ela deve retornar o JSON de sucesso ou None se falhar)
            validation_data = api_client.validate_session() 

            if validation_data and validation_data.get("valid"):
                # 5. SESSÃO VÁLIDA!
                # Loga o usuário no session_state usando os dados da validação
                login_user(
                    username=validation_data["username"],
                    user_id=validation_data["user_id"],
                    session_token=token_from_cookie
                )
                return True
            else:
                # 6. Token do cookie é inválido ou expirou
                logout_user() # Limpa tudo (inclusive o cookie ruim, se session_state.py foi atualizado)
                return False
                
        except Exception as e:
            print(f"Erro ao validar cookie: {e}")
            logout_user()
            return False
            
    # 7. Nenhum token no cookie
    return False

def show_profile_page():
    """Página de gerenciamento de perfil do usuário"""
    st.title(f"👤 Perfil de {st.session_state.username}")
    st.markdown("---")
    st.warning("🚧 Funcionalidade em desenvolvimento")

def main():
    
    if not is_logged_in():
        # Se o session_state está limpo, tenta logar pelo cookie (F5)
        if not attempt_login_from_cookie():
            # Se o cookie falhou ou não existe, vai pro login
            st.switch_page("pages/login_page.py")
        else:
            # Logado com sucesso via cookie!
            st.rerun() # Recarrega a página no estado "logado"
    else:
        # Já estava logado (navegação normal)
        show_main_app()


if __name__ == "__main__":
    main()