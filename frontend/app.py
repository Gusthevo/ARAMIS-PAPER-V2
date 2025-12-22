import streamlit as st
from utils.session_state import init_session_state, logout_user, login_user, is_logged_in
from utils.api_client import api_client 
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY 
from utils.sidebar import show_sidebar 
from utils.styles import apply_custom_style

# ---------------- CONFIGURAÇÃO DA PÁGINA ---------------- #
st.set_page_config(
    page_title="ARAMIS",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- INICIALIZAÇÃO ---------------- #
init_session_state()
apply_custom_style()
cookies = get_cookie_manager()


# ====================== HOME ====================== #
def show_home_page():
    """Página inicial redesenhada com foco em UX e hierarquia visual"""

# ---------- BANNER DE AVISO ---------- #
# Configure esta variável conforme necessário
SHOW_WARNING = True  # Mude para False quando não precisar mais
WARNING_MESSAGE = "<strong>Informação Importante</strong> - Os resultados obtidos pelos agentes podem não ser perfeitos, atente-se para ver se eles fazem sentido. Lembre-se, a intenção da ferramenta não é substituir o autor e seu estilo de escrita, mas ser um revisor aliado para aprimorar a escrita do TCC."

if SHOW_WARNING:
    st.markdown(f"""
    <div style="
        background: linear-gradient(90deg, #FFF3CD 0%, #FFEAA7 100%);
        border: 1px solid #FFC107;
        color: #856404;
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        font-size: 0.95rem;
    ">
        <span style="font-size: 1.2rem; margin-right: 10px;">⚠️</span>
        <div style="flex-grow: 1;">{WARNING_MESSAGE}</div>
        <button onclick="this.parentElement.style.display='none'" 
                style="
                    background: none;
                    border: none;
                    color: #856404;
                    font-size: 1.2rem;
                    cursor: pointer;
                    padding: 0 5px;
                "
    </div>
    """, unsafe_allow_html=True)

    # ---------- HERO ---------- #
    st.markdown(
        f"""
        <div style="
            text-align: center;
            padding: 3rem 0 2.5rem 0;
            max-width: 900px;
            margin: auto;
        ">
            <h1 style="font-size: 3rem; margin-bottom: 0.3rem;">
                ARAMIS
            </h1>
            <p style="font-size: 1.35rem; font-weight: 500;">
                Análise e revisão de textos Acadêmicos com LLM open-source
            </p>
            <p style="font-size: 1rem; color: #64748B; margin-top: 0.8rem;">
                Olá, <b>{st.session_state.username}</b>.  
                Revise seu texto com a ajuda de até 3 agentes.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- CTA PRINCIPAL ---------- #
    col_esq, col_center, col_dir = st.columns([1, 2, 1])

    with col_center:
        with st.container(border=True):
            st.markdown("### 📝 Nova Correção Acadêmica")
            st.caption(
                "Envie uma seção do seu TCC e receba uma análise detalhada, "
                "estruturada por agentes especializados."
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "Iniciar nova análise",
                type="primary",
                use_container_width=True
            ):
                st.switch_page("pages/request_page.py")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------- FEATURES ---------- #
    st.markdown("## 🔍 Como o ARAMIS analisa seu texto")
    st.caption(
        "Cada agente atua sobre um aspecto essencial da escrita acadêmica."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("#### ✍️ Correção Gramatical")
            st.write(
                "Revisão ortográfica, concordância, pontuação e adequação "
                "à norma culta da língua portuguesa."
            )

    with col2:
        with st.container(border=True):
            st.markdown("#### 🧠 Encadeamento Lógico")
            st.write(
                "Avaliação da coesão textual, coerência entre parágrafos "
                "e progressão lógica das ideias."
            )

    with col3:
        with st.container(border=True):
            st.markdown("#### 📚 Rigor Metodológico")
            st.write(
                "Verificação da consistência entre problema de pesquisa, "
                "objetivos, método e análise dos resultados."
            )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---------- DICAS ---------- #
    with st.expander("ℹ️ Orientações para obter melhores resultados"):
        st.markdown(
            """
            - **Recomendamos o envio de uma seção por vez** (Introdução, Metodologia, Resultados).
            - No agente de **Rigor Metodológico**, recomendamos inserir a seção de Metodologia, pois é onde se concentra a maior parte das etapas metodológicas de um TCC.
            - **Escolha corretamente a área do conhecimento para reposta mais precisa**.
            - Utilize **Rigor Alto** para versões finais do trabalho.
            - Temos a funcionalidade de **conserto automático de parágrafos**, mas confirme se na caixa de texto estão corretamente separados
            """
        )


# ====================== ABOUT ====================== #
def show_about_page():
    st.markdown("## ℹ️ Sobre o ARAMIS")
    st.caption("Plataforma inteligente de apoio à escrita acadêmica")
    st.markdown("<br>", unsafe_allow_html=True)

    try:
        about_info = api_client.get_about_info()
    except:
        about_info = None

    c1, c2 = st.columns([2, 1])

    with c1:
        with st.container(border=True):
            if about_info:
                platform = about_info.get("platform", {})
                st.markdown(f"### {platform.get('name', 'ARAMIS')}")
                st.write(platform.get("description", ""))
            else:
                st.write(
                    "O ARAMIS é uma plataforma desenvolvida para auxiliar estudantes "
                    "na revisão e aprimoramento de textos acadêmicos, utilizando "
                    "arquitetura multiagente baseada em Modelos de Linguagem (LLMs)."
                )

            st.markdown("#### 🎯 Missão")
            st.write(
                "Democratizar o acesso a revisões acadêmicas de alta qualidade, "
                "promovendo clareza, rigor e excelência científica."
            )

    with c2:
        with st.container(border=True):
            st.markdown("#### 📌 Informações")
            st.write("**Versão:** 1.0.0 (Beta)")
            st.write("**Status:** Online 🟢")
            st.write("**Desenvolvido por:**")
            st.write("- Gustavo Campelo")
            st.write("- Pablo Kauan")


# ====================== PROFILE ====================== #
def show_profile_page():
    st.markdown("## 👤 Meu Perfil")
    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(f"### {st.session_state.username}")
        st.caption("Status: Conectado 🟢")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("🚧 Funcionalidades de perfil e histórico estão em desenvolvimento.")


# ====================== AUTENTICAÇÃO ====================== #
def attempt_login_from_cookie():
    if st.session_state.logged_in:
        return True

    token = cookies.get(AUTH_TOKEN_KEY)
    if not token:
        return False

    st.session_state.session_token = token
    try:
        validation = api_client.validate_session()
        if validation and validation.get("valid"):
            login_user(
                username=validation["username"],
                user_id=validation["user_id"],
                session_token=token
            )
            return True
    except Exception as e:
        print(f"Erro ao validar cookie: {e}")

    logout_user()
    return False


# ====================== APP ROOT ====================== #
def show_main_app():
    show_sidebar()

    if "current_view" not in st.session_state:
        st.session_state["current_view"] = "home"

    view = st.session_state["current_view"]

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
