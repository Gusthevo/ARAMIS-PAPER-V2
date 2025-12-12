import streamlit as st
from utils.api_client import api_client


st.set_page_config(
    page_title="ARAMIS - Analise",
    page_icon="images/logo-aramis-cropped.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("ARAMIS - Análise")

secoes = api_client.carregar_secoes()
agentes = api_client.carregar_agentes()
niveis = api_client.carregar_niveis()

# Criar mapeamentos
mapa_agentes = {a["name"]: a["id"] for a in agentes}
nomes_agentes = list(mapa_agentes.keys())

mapa_secoes = {s["name"]: s["id"] for s in secoes}
nomes_secoes = list(mapa_secoes.keys())

mapa_niveis = {n["name"]: n["id"] for n in niveis}
nomes_niveis = list(mapa_niveis.keys())

with st.form(key="formulario"):
    titulo = st.text_input("TCC Título", placeholder="Digite o título")

    area = st.text_input("Área do TCC", placeholder="Digite a área de conhecimento abordada")

    secao = st.selectbox("Seção a ser analisada", nomes_secoes)

    nivel = st.selectbox("Nível de rigor", nomes_niveis)

    texto = st.text_area("Texto", height=300)

    selecionados = st.multiselect(
        "Escolha os agentes:",
        nomes_agentes
    )

    enviar = st.form_submit_button("Enviar")

if enviar:
    if len(selecionados) < 1:
        st.warning("É necessário selecionar ao menos um agente.", icon="⚠️")
        st.stop()

    ids_selecionados = [mapa_agentes[n] for n in selecionados]

    payload = {
        "title": titulo,
        "area": area,
        "section": mapa_secoes[secao],
        "rigor": mapa_niveis[nivel],
        "text": texto,
        "agents": ids_selecionados
    }

    st.json(payload, expanded=False)

    with st.spinner("Análisando..."):
        resposta = api_client.analyze(payload)

    if resposta.status_code == 200:
        dados = resposta.json()
        st.session_state["json_resultado"] = dados
        st.switch_page("pages/result_page")
    elif resposta.status_code == 500:
        st.error("Erro no Servidor Interno", icon="🚨")
    else:
        try:
            resposta = resposta.json()
            st.warning(f"{resposta.get('detail', 'Erro desconhecido')}", icon="⚠️")
        except:
            st.error(f"Erro inesperado ao processar a resposta da API", icon="🚨")
