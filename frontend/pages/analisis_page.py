import streamlit as st
import pandas as pd
from utils.session_state import init_session_state, login_user, is_logged_in, logout_user
from utils.api_client import api_client 
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY
from utils.sidebar import show_sidebar
from utils.styles import apply_custom_style 

# -------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# -------------------------------------------------------------------------
st.set_page_config(
    page_title="ARAMIS - Análises Realizadas",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

init_session_state()
apply_custom_style()
cookies = get_cookie_manager()

# -------------------------------------------------------------------------
# 2. AUTENTICAÇÃO
# -------------------------------------------------------------------------
def attempt_login_from_cookie():
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
            logout_user()
        except Exception:
            logout_user()
    return False

if not is_logged_in():
    if not attempt_login_from_cookie():
        st.switch_page("pages/login_page.py")
    else:
        st.rerun()

# -------------------------------------------------------------------------
# 3. SIDEBAR
# -------------------------------------------------------------------------
show_sidebar()

# -------------------------------------------------------------------------
# 4. HEADER
# -------------------------------------------------------------------------
st.markdown(
    """
    <div style="padding: 1rem 0;">
        <h1 style="margin-bottom: 0.2rem;">📊 Análises Realizadas</h1>
        <p style="color: #6b7280;">
            Aqui estão todas as análises corrigidas associadas à sua conta.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------------------------------
# 5. BUSCA DAS CORREÇÕES
# -------------------------------------------------------------------------
response = api_client.get_corrections(st.session_state.user_id)

if response.status_code != 200:
    st.error("❌ Erro ao buscar correções")
    st.stop()

corrections = response.json().get("corrections", [])

if not corrections:
    st.info("ℹ️ Nenhuma correção encontrada")
    st.stop()

df = pd.DataFrame(corrections)
df["created_at"] = pd.to_datetime(df["created_at"]).dt.strftime("%d/%m/%Y %H:%M")

# -------------------------------------------------------------------------
# 6. LISTAGEM EM CARDS
# -------------------------------------------------------------------------
for _, row in df.iterrows():
    with st.container():
        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns([5, 2, 2, 1])

        col1.markdown(f"### {row['title']}")
        col2.markdown(f"**Seção**<br>{row['section']}", unsafe_allow_html=True)
        col3.markdown(f"**Criado em**<br>{row['created_at']}", unsafe_allow_html=True)

        if col4.button("👁 Ver", key=f"view_{row['id']}"):
            st.session_state["selected_analysis"] = row.to_dict()
            st.switch_page("pages/details_page.py")

        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")  # espaçamento entre cards
