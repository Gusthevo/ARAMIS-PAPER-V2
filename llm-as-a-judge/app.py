import streamlit as st
from openai import OpenAI
import os
import random
import sqlite3
import pandas as pd
from dotenv import load_dotenv

# ==========================================
# Configurações Iniciais
# ==========================================
st.set_page_config(page_title="LLM Blind Arena & Ranking", layout="wide")

load_dotenv()
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="lm-studio"
)
AVAILABLE_MODELS = [""]


def carregar_prompt_externo(caminho_arquivo: str) -> str:
    """Lê o conteúdo do arquivo .txt."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Erro: O arquivo de prompt não foi encontrado. Verifique o nome e a pasta."
# ==========================================
# Banco de Dados (SQLite)
# ==========================================
DB_NAME = "arena_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS battles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            prompt TEXT,
            model_1 TEXT,
            model_2 TEXT,
            winner TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_battle(prompt, model_1, model_2, winner):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO battles (prompt, model_1, model_2, winner) VALUES (?, ?, ?, ?)',
              (prompt, model_1, model_2, winner))
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = sqlite3.connect(DB_NAME)
    query = """
        SELECT winner as Modelo, COUNT(*) as Vitorias 
        FROM battles 
        WHERE winner != 'Empate' 
        GROUP BY winner 
        ORDER BY Vitorias DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_history():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT timestamp, prompt, model_1, model_2, winner FROM battles ORDER BY timestamp DESC", conn)
    conn.close()
    return df

init_db()

# ==========================================
# Inicialização de Estado (Session State)
# ==========================================
if "responses" not in st.session_state:
    st.session_state.responses = None
if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "winner_display" not in st.session_state:
    st.session_state.winner_display = None
if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = ""

# ==========================================
# Funções de Inferência
# ==========================================
def generate_response(model_name: str, prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta com {model_name}: {str(e)}"

# ==========================================
# Interface Web
# ==========================================
st.title("🎭 LLM Blind Arena & Leaderboard")

tab_arena, tab_ranking = st.tabs(["⚔️ Batalha às Cegas", "🏆 Ranking Global"])

# ... (Mantenha as importações, banco de dados e funções iniciais intactas) ...

# ------------------------------------------
# ABA 1: ARENA MULTI-REVISOR
# ------------------------------------------
with tab_arena:
    st.markdown("### 📥 Importar Dataset de Revisões")
    
    # Campo para upload do CSV gerado pelo seu extrator
    uploaded_file = st.file_uploader("Faça o upload do CSV com os artigos e revisões", type=["csv"])
    
    if uploaded_file is not None:
        df_papers = pd.read_csv(uploaded_file)
        
        # Cria um selectbox para escolher qual artigo avaliar
        titulos = df_papers['paper_title'].tolist()
        artigo_selecionado = st.selectbox("Selecione o Artigo para Iniciar a Batalha:", titulos)
        
        # Pega a linha do artigo selecionado
        linha_artigo = df_papers[df_papers['paper_title'] == artigo_selecionado].iloc[0]
        
        with st.expander("⚙️ Configuração do Desafiante (LLM)", expanded=not st.session_state.responses):
            st.info(f"**Artigo Selecionado:** {linha_artigo['paper_title']}")
            
            modelo_desafiante = st.selectbox("Escolha o Modelo de Teste", AVAILABLE_MODELS, index=0)
            
            if st.button("Gerar 5ª Revisão e Iniciar Batalha", type="primary"):
                with st.spinner("O LLM está lendo o artigo e gerando a revisão..."):
                    
                    # 1. Carrega o prompt e substitui as variáveis
                    template = carregar_prompt_externo("prompt_revisao_tcc.txt")
                    prompt_pronto = template.replace("{paper_title}", linha_artigo['paper_title'])
                    prompt_pronto = prompt_pronto.replace("{paper_text}", linha_artigo['paper_text'])
                    
                    # 2. Gera a revisão do LLM
                    revisao_llm = generate_response(modelo_desafiante, prompt_pronto)
                    
                    # 3. Agrupa todas as revisões e identifica a origem secreta
                    opcoes = [
                        {"identidade": "Humano 1", "texto": linha_artigo['review_1']},
                        {"identidade": "Humano 2", "texto": linha_artigo['review_2']},
                        {"identidade": "Humano 3", "texto": linha_artigo['review_3']},
                        {"identidade": "Humano 4", "texto": linha_artigo['review_4']},
                        {"identidade": f"LLM ({modelo_desafiante})", "texto": revisao_llm}
                    ]
                    
                    # 4. Embaralha para o teste cego
                    random.shuffle(opcoes)
                    
                    # Salva no estado
                    st.session_state.responses = opcoes
                    st.session_state.current_prompt = linha_artigo['paper_title']
                    st.session_state.revealed = False
                    st.session_state.winner_display = None
                    st.rerun()

    # ==========================================
    # ÁREA DE JULGAMENTO (O TESTE DE TURING)
    # ==========================================
    if st.session_state.responses:
        st.divider()
        st.markdown(f"### Avaliando as Revisões para: *{st.session_state.current_prompt}*")
        
        # Cria 5 abas para leitura confortável
        abas = st.tabs(["Revisor 1", "Revisor 2", "Revisor 3", "Revisor 4", "Revisor 5"])
        
        for i, aba in enumerate(abas):
            with aba:
                st.markdown(f"**Análise do Revisor {i+1}**")
                # Exibe o texto da revisão. Use st.write para renderizar markdown corretamente
                st.write(st.session_state.responses[i]["texto"])

        st.divider()

        # Sistema de Votação
        if not st.session_state.revealed:
            st.markdown("### 🏆 Qual revisor fez o melhor trabalho?")
            st.caption("Considere rigor metodológico, clareza e alinhamento com os padrões ICLR.")
            
            # Botões dinâmicos de votação
            colunas_voto = st.columns(5)
            for i, col in enumerate(colunas_voto):
                with col:
                    if st.button(f"Votar no Revisor {i+1}", use_container_width=True, key=f"btn_rev_{i}"):
                        vencedor_real = st.session_state.responses[i]["identidade"]
                        # Salva no banco (Artigo, Vencedor Real)
                        save_battle(st.session_state.current_prompt, "Vários Humanos", modelo_desafiante, winner=vencedor_real)
                        
                        st.session_state.winner_display = f"Revisor {i+1} (Identidade: {vencedor_real})"
                        st.session_state.revealed = True
                        st.rerun()

        # Revelação
        if st.session_state.revealed:
            st.success(f"## 🎉 Veredito Salvo! Você escolheu o: **{st.session_state.winner_display}**")
            
            st.markdown("### 🕵️ Identidades Reveladas:")
            for i in range(5):
                identidade = st.session_state.responses[i]['identidade']
                icone = "🤖" if "LLM" in identidade else "🧑‍🏫"
                if f"Revisor {i+1}" in st.session_state.winner_display:
                    st.markdown(f"- **Revisor {i+1}: {icone} {identidade} (VENCEDOR 🏆)**")
                else:
                    st.markdown(f"- Revisor {i+1}: {icone} {identidade}")
            
            if st.button("🔄 Avaliar Outro Artigo"):
                st.session_state.responses = None
                st.session_state.revealed = False
                st.session_state.winner_display = None
                st.rerun()

# ------------------------------------------
# ABA 2: RANKING E HISTÓRICO
# ------------------------------------------
with tab_ranking:
    st.header("👑 Leaderboard")
    
    df_leaderboard = get_leaderboard()
    if df_leaderboard.empty:
        st.info("Nenhuma batalha registrada ainda. Faça algumas votações na Arena!")
    else:
        
        # Pega os nomes e vitórias da tabela
        modelos = df_leaderboard["Modelo"].tolist()
        vitorias = df_leaderboard["Vitorias"].tolist()
        
        # Cria as colunas dinamicamente (uma para cada modelo que já pontuou)
        colunas = st.columns(len(modelos))
        
        # Preenche cada coluna com o contador (metric) correspondente
        for i, col in enumerate(colunas):
            with col:
                st.metric(label=modelos[i], value=vitorias[i])
        
        st.divider()
        # Mantém a tabela abaixo dos contadores caso queira ver os dados brutos
        st.dataframe(df_leaderboard, use_container_width=True)
    
    st.divider()
    st.header("📜 Histórico de Batalhas")
    df_history = get_history()
    if not df_history.empty:
        st.dataframe(df_history, use_container_width=True)