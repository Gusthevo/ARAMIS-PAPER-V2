import streamlit as st
from utils.session_state import init_session_state, logout_user, login_user, is_logged_in
from utils.api_client import api_client 
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY 
from utils.sidebar import show_sidebar 
from utils.styles import apply_custom_style 

# Configuração da página
st.set_page_config(
    page_title="ARAMIS - Início",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializa serviços
init_session_state()
apply_custom_style() # <--- 2. APLICA O CSS GLOBAL
cookies = get_cookie_manager()

def show_home_page():
    """Página inicial com design estilo 'Landing Page'"""
    
    # --- HERO SECTION (Cabeçalho de Boas Vindas) ---
    # Usamos HTML para centralizar e dar destaque, fugindo do padrão alinhado à esquerda
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0 3rem 0;">
        <h1 style="margin-bottom: 0.5rem;">Bem-vindo ao ARAMIS</h1>
        <p style="font-size: 1.2rem; color: #64748B;">
            Olá, <b>{st.session_state.username}</b>. Bem-vindo ao seu assistente inteligente de auxílio à escrita acadêmica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- ACTION CARD (Ação Principal) ---
    # Colocamos a ação mais importante em destaque no topo
    col_vazia_esq, col_center, col_vazia_dir = st.columns([1, 2, 1])
    with col_center:
        with st.container(border=True):
            st.markdown("### 🚀 Iniciar Nova Análise")
            st.write("Submeta um novo texto para correção gramatical, lógica e metodológica.")
            if st.button("📝 Criar Nova Correção", use_container_width=True, type="primary"):
                st.switch_page("pages/request_page.py")

    st.markdown("---")

    # --- FEATURES GRID (O que a ferramenta faz) ---
    st.subheader("🔍 O que é cada agente?")
    
    col1, col2, col3 = st.columns(3)
    
    # Card 1
    with col1:
        with st.container(border=True):
            st.markdown("#### ✍️ Correção Gramatical")
            st.caption("Correção ortográfica, concordância e pontuação seguindo a norma culta.")
    
    # Card 2
    with col2:
        with st.container(border=True):
            st.markdown("#### 🧠 Encadeamento Lógico")
            st.caption("Análise de coesão, coerência e encadeamento de ideias entre sentenças e parágrafos.")
    
    # Card 3
    with col3:
        with st.container(border=True):
            st.markdown("#### 📚 Rigor Metodológico")
            st.caption("Verificação de coerência entre o problema de pesquisa, o método e a análise de resultados.")

    # --- DICAS / RODAPÉ ---
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("ℹ️ Dicas para um melhor resultado"):
        st.write("""
        1. Envie uma seção por vez (ex: Introdução, Metodologia).
        2. Certifique-se de selecionar a área de conhecimento correta.
        3. Utilize o nível de rigor 'Alto' para versões finais do trabalho.
        """)

def show_about_page():
    """Página sobre a plataforma"""
    st.title("ℹ️ Sobre o ARAMIS")
    st.markdown("---")
    
    try:
        about_info = api_client.get_about_info()
    except:
        about_info = None
    
    # Layout em duas colunas para o Sobre
    c1, c2 = st.columns([2, 1])
    
    with c1:
        if about_info:
            platform = about_info.get("platform", {})
            st.subheader(platform.get("name", "ARAMIS"))
            st.write(platform.get("description", ""))
        else:
            st.subheader("ARAMIS - Sistema Inteligente")
            st.write("""
            O ARAMIS é uma plataforma desenvolvida para auxiliar estudantes na correção 
            e melhoria de seus trabalhos acadêmicos. Utilizamos um sistema multiagente 
            baseados em Modelos de Linguagem (LLMs) para obter revisões coesas e direcionadas.
            """)
            
            st.markdown("#### Nossa Missão")
            st.write("Democratizar o acesso a revisões acadêmicas de alta qualidade.")

    with c2:
        # Um card lateral com versão ou status
        with st.container(border=True):
            st.write("**Versão:** 1.0.0 (Beta)")
            st.write("**Status:** Online 🟢")
            st.write("**Desenvolvido por:** Gustavo Campelo e Pablo Kauan")

def show_profile_page():
    """Página de gerenciamento de perfil"""
    st.title("👤 Meu Perfil")
    
    # Layout de perfil usando containers
    with st.container(border=True):
        col_icon, col_info = st.columns([1, 4])
        with col_icon:
            st.markdown("# 👤") # Placeholder de avatar
        with col_info:
            st.subheader(st.session_state.username)
            st.markdown(f"**Status:** Conectado")
            
    st.markdown("---")
    st.info("🚧 Edição de perfil e histórico de correções em desenvolvimento.")

def attempt_login_from_cookie():
    """Tenta logar o usuário se um cookie de token válido for encontrado."""
    if st.session_state.logged_in:
        return True
    
    token_from_cookie = cookies.get(AUTH_TOKEN_KEY)
    
    if token_from_cookie:
        st.session_state.session_token = token_from_cookie
        try:
            validation_data = api_client.validate_session() 
            if validation_data and validation_data.get("valid"):
                login_user(
                    username=validation_data["username"],
                    user_id=validation_data["user_id"],
                    session_token=token_from_cookie
                )
                return True
            else:
                logout_user()
                return False
        except Exception as e:
            print(f"Erro ao validar cookie: {e}")
            logout_user()
            return False
            
    return False

def show_main_app():
    """Gerencia a exibição das views principais"""
    
    show_sidebar()
    
    if "current_view" not in st.session_state:
        st.session_state["current_view"] = "home"
    
    view = st.session_state["current_view"]
    
    # Pequena animação/transição suave (opcional, apenas visual)
    if view == "home":
        show_home_page()
    elif view == "profile":
        show_profile_page()
    elif view == "about":
        show_about_page()
    elif view == "request":
        st.switch_page("pages/request_page.py")
    else:
        show_home_page()

def main():
    if not is_logged_in():
        if not attempt_login_from_cookie():
            st.switch_page("pages/login_page.py")
        else:
            st.rerun()
    else:
        show_main_app()

if __name__ == "__main__":
    main()