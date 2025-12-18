import streamlit as st
import json
from utils.sidebar import show_sidebar
from utils.api_client import api_client
from utils.styles import apply_custom_style
from utils.session_state import init_session_state, login_user, is_logged_in, logout_user
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY

# -------------------------------------------------------------------------
# 3. INTERFACE DE NAVEGAÇÃO
# -------------------------------------------------------------------------
init_session_state()
show_sidebar()
apply_custom_style()

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


st.title("🔎 Resultados da Análise dos Agentes")

# Entrada (você provavelmente já recebe isso da API)
# Para teste rápido:
json_data = st.session_state.get("json_resultado", None)

if not json_data:
    st.warning("Nenhum resultado encontrado. Insira o JSON.")
    input_text = st.text_area("Cole aqui o JSON da análise:")
    if st.button("Carregar JSON"):
        try:
            st.session_state["json_data"] = json.loads(input_text)
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao carregar JSON: {e}")
    st.stop()

data = json_data

st.subheader("📄 Informações Gerais")

st.write(f"*ID da Análise:* {data.get('analysis_id')}")
st.write(f"*Seção:* {data.get('section')}")
st.write(f"*Texto Original:*")
st.info(data.get("original_text"))

corrections = data.get("correction", [])

if not corrections:
    st.warning("Nenhuma análise realizada pelos agentes.")
    st.stop()

# Criar abas para cada agente encontrado
tabs = []
tab_titles = []

for agent in corrections:
    tab_titles.append(agent.get("agente_utilizado", "Agente"))
    tabs.append(agent)

tab_objects = st.tabs(tab_titles)

# Renderizar cada agente
for tab, agent in zip(tab_objects, tabs):
    with tab:
        agente = agent.get("agente_utilizado")

        st.header(f"🤖 {agente}")

        # Agente de Correção Gramatical
        if agente == "Agente de Correção Gramatical":
            st.subheader("📌 Texto Corrigido")
            st.success(agent.get("texto_corrigido"))

            st.subheader("📊 Resumo das Correções")
            resumo = agent.get("resumo_correcoes", {})

            st.write(resumo)

            st.subheader("📝 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(f"{c['tipo_correcao']} – {c['descricao'][:50]}..."):
                    st.write(f"*Tipo:* {c['tipo_correcao']}")
                    st.write(f"*Descrição:* {c['descricao']}")

        # Agente de Encadeamento Lógico
        elif agente == "Agente de Encadeamento Lógico":
            st.subheader("📋 Avaliação Geral")
            st.info(agent.get("avaliacao_geral"))

            st.subheader("🧠 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(c["trecho_relevante"][:70] + "..."):
                    st.write(f"*Problema:* {c['tipo_problema']}")
                    st.write(f"*Análise:* {c['analise']}")
                    st.write(f"*Sugestão:* {c['sugestao_estrutural']}")

        # Agente de Rigor Metodológico
        elif agente == "Agente de Rigor Metodológico":
            st.subheader("📋 Avaliação Geral")
            st.info(agent.get("avaliacao_geral"))

            st.subheader("🧠 Texto Analisado")
            st.code(agent.get("texto_analisado"))

            st.subheader("📝 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(c["trecho_relevante"][:70] + "..."):
                    st.write(f"*Tipo:* {c['tipo_ponto']}")
                    st.write(f"*Análise:* {c['analise']}")
                    if "recomendacao" in c:
                        st.write(f"*Recomendação:* {c['recomendacao']}")

        else:
            st.warning("Agente não reconhecido, mas exibindo dados crus:")
            st.json(agent)