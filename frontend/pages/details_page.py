import streamlit as st
import json
from utils.sidebar import show_sidebar

# -------------------------------------------------------------------------
# INTERFACE
# -------------------------------------------------------------------------
show_sidebar()
if st.button("⬅ Voltar para lista"):
    st.switch_page("pages/analisis_page.py")

# 🔥 pega a análise completa
analysis = st.session_state.get("selected_analysis")

if not analysis:
    st.warning("Nenhuma análise selecionada.")
    if st.button("⬅ Voltar"):
        st.switch_page("pages/1_Correcoes.py")
    st.stop()

# 🔧 se correction vier como string, converte
corrections = analysis.get("correction", [])
if isinstance(corrections, str):
    corrections = json.loads(corrections)


# -------------------------------------------------------------------------
# INFORMAÇÕES GERAIS
# -------------------------------------------------------------------------
st.subheader("📄 Informações Gerais")

st.write(f"**ID da Análise:** {analysis.get('id')}")
st.write(f"**Seção:** {analysis.get('section')}")
st.write(f"**Criado em:** {analysis.get('created_at')}")
st.write(f"**Tempo de análise:** {analysis.get('analysis_time')}s")

if not corrections:
    st.warning("Nenhuma análise realizada pelos agentes.")
    st.stop()

# -------------------------------------------------------------------------
# ABAS POR AGENTE
# -------------------------------------------------------------------------
tab_titles = [a.get("agente_utilizado", "Agente") for a in corrections]
tabs = st.tabs(tab_titles)

for tab, agent in zip(tabs, corrections):
    with tab:
        agente = agent.get("agente_utilizado")
        st.header(f"🤖 {agente}")

        # -------------------------------------------------------------
        # Agente de Correção Gramatical
        # -------------------------------------------------------------
        if agente == "Agente de Correção Gramatical":
            st.subheader("📌 Texto Corrigido")
            st.success(agent.get("texto_corrigido"))

            st.subheader("📊 Resumo das Correções")
            st.write(agent.get("resumo_correcoes", {}))

            st.subheader("📝 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(f"{c['tipo_correcao']} – {c['descricao'][:60]}..."):
                    st.write(f"**Tipo:** {c['tipo_correcao']}")
                    st.write(f"**Descrição:** {c['descricao']}")

        # -------------------------------------------------------------
        # Agente de Encadeamento Lógico
        # -------------------------------------------------------------
        elif agente == "Agente de Encadeamento Lógico":
            st.subheader("📋 Avaliação Geral")
            st.info(agent.get("avaliacao_geral"))

            st.subheader("🧠 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(c["trecho_relevante"][:70] + "..."):
                    st.write(f"**Problema:** {c['tipo_problema']}")
                    st.write(f"**Análise:** {c['analise']}")
                    st.write(f"**Sugestão:** {c['sugestao_estrutural']}")

        # -------------------------------------------------------------
        # Agente de Rigor Metodológico
        # -------------------------------------------------------------
        elif agente == "Agente de Rigor Metodológico":
            st.subheader("📋 Avaliação Geral")
            st.info(agent.get("avaliacao_geral"))

            st.subheader("🧠 Texto Analisado")
            st.code(agent.get("texto_analisado"))

            st.subheader("📝 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(c["trecho_relevante"][:70] + "..."):
                    st.write(f"**Tipo:** {c['tipo_ponto']}")
                    st.write(f"**Análise:** {c['analise']}")
                    if "recomendacao" in c:
                        st.write(f"**Recomendação:** {c['recomendacao']}")

        else:
            st.warning("Agente não reconhecido")
            st.json(agent)
