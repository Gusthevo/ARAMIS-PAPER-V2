import streamlit as st
import json

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

st.write(f"**ID da Análise:** {data.get('analysis_id')}")
st.write(f"**Seção:** {data.get('section')}")
st.write(f"**Texto Original:**")
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
                    st.write(f"**Tipo:** {c['tipo_correcao']}")
                    st.write(f"**Descrição:** {c['descricao']}")

        # Agente de Encadeamento Lógico
        elif agente == "Agente de Encadeamento Lógico":
            st.subheader("📋 Avaliação Geral")
            st.info(agent.get("avaliacao_geral"))

            st.subheader("🧠 Comentários Detalhados")
            for c in agent.get("comentarios_detalhados", []):
                with st.expander(c["trecho_relevante"][:70] + "..."):
                    st.write(f"**Problema:** {c['tipo_problema']}")
                    st.write(f"**Análise:** {c['analise']}")
                    st.write(f"**Sugestão:** {c['sugestao_estrutural']}")

        # Agente de Rigor Metodológico
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
            st.warning("Agente não reconhecido, mas exibindo dados crus:")
            st.json(agent)