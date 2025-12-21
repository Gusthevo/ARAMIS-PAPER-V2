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

# Inicializa serviços essenciais
init_session_state()
apply_custom_style() # Aplica o CSS (cards, botões, inputs arredondados)
cookies = get_cookie_manager()

# -------------------------------------------------------------------------
# 2. LÓGICA DE AUTENTICAÇÃO
# -------------------------------------------------------------------------
def attempt_login_from_cookie():
    """Tenta recuperar a sessão via cookie se o usuário der F5."""
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

# Bloqueio de Segurança: Redireciona se não estiver logado
if not is_logged_in():
    if not attempt_login_from_cookie():
        st.switch_page("pages/login_page.py")
    else:
        st.rerun()

# -------------------------------------------------------------------------
# 3. INTERFACE DE NAVEGAÇÃO
# -------------------------------------------------------------------------
show_sidebar()

# 🔎 busca correções
response = api_client.get_corrections(st.session_state.user_id)

if response.status_code != 200:
    st.error("Erro ao buscar correções")
    st.stop()

data = response.json()
corrections = data["corrections"]

if not corrections:
    st.info("Nenhuma correção encontrada")
    st.stop()

# 📊 monta dataframe completo
df = pd.DataFrame(corrections)
df["created_at"] = pd.to_datetime(df["created_at"])

# 🧩 cabeçalho da tabela
cols = st.columns([5, 2, 2, 1])
cols[0].markdown("**Title**")
cols[1].markdown("**Section**")
cols[2].markdown("**Created at**")
cols[3].markdown("**Visualizar**")

st.divider()

# 📌 linhas — ITERA NO DF COMPLETO
for _, row in df.iterrows():
    cols = st.columns([5, 2, 2, 1])

    cols[0].write(row["title"])
    cols[1].write(row["section"])
    cols[2].write(row["created_at"])

    # 👁 botão de detalhe
    if cols[3].button("👁", key=f"view_{row['id']}"):
        # 🔥 passa TODA a análise
        st.session_state["selected_analysis"] = row.to_dict()
        st.switch_page("pages/details_page.py")

