import streamlit as st
from utils.session_state import init_session_state, login_user, is_logged_in, logout_user
from utils.api_client import api_client 
from utils.cookie_manager import get_cookie_manager, AUTH_TOKEN_KEY
from utils.sidebar import show_sidebar
from utils.styles import apply_custom_style 

# -------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA
# -------------------------------------------------------------------------
st.set_page_config(
    page_title="ARAMIS - Nova Análise",
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

# -------------------------------------------------------------------------
# 4. FUNÇÕES AUXILIARES
# -------------------------------------------------------------------------
def limpar_texto():
    """Remove quebras de linha indesejadas (comuns em PDFs) mantendo parágrafos."""
    if "texto_input" in st.session_state and st.session_state.texto_input:
        txt = st.session_state.texto_input
        # 1. Preserva parágrafos reais (duplo enter vira marcador)
        txt = txt.replace('\n\n', '{{PARAGRAFO}}')
        # 2. Remove quebras de linha simples (quebras de PDF)
        txt = txt.replace('\n', ' ')
        # 3. Remove espaços duplos excessivos gerados
        txt = ' '.join(txt.split())
        # 4. Restaura os parágrafos
        txt = txt.replace('{{PARAGRAFO}}', '\n\n')
        # Atualiza o estado
        st.session_state.texto_input = txt

# -------------------------------------------------------------------------
# 5. FORMULÁRIO PRINCIPAL
# -------------------------------------------------------------------------
st.title("📝 Nova Correção")
st.markdown("Preencha os detalhes do seu trabalho abaixo para análise.")

# Carrega dados da API para popular os selects
try:
    secoes_opt = api_client.carregar_secoes()
    agentes_opt = api_client.carregar_agentes()
    niveis_opt = api_client.carregar_niveis()
except Exception:
    st.error("Erro de conexão com o servidor. Tente recarregar a página.")
    st.stop()

# Mapeamentos (Nome -> ID)
mapa_agentes = {a["name"]: a["id"] for a in agentes_opt}
nomes_agentes = list(mapa_agentes.keys())

mapa_secoes = {s["name"]: s["id"] for s in secoes_opt}
nomes_secoes = list(mapa_secoes.keys())

mapa_niveis = {n["name"]: n["id"] for n in niveis_opt}
nomes_niveis = list(mapa_niveis.keys())

# Usamos container em vez de st.form para permitir que o botão "Limpar" funcione interativamente
with st.container():
    # Se você tiver a classe css-card no styles.py, o container já terá borda visualmente se configurado,
    # senão o st.container() agrupa os itens logicamente.
    
    st.subheader("1. Informações do trabalho")
    
    col1, col2 = st.columns([2, 1])
    # Como não estamos em st.form, usamos variáveis diretas
    titulo = col1.text_input("Título do TCC", placeholder="Ex: O impacto da IA na educação...")
    area = col2.text_input("Área de conhecimento", placeholder="Ex: Pedagogia Digital")

    st.markdown("---")
    
    st.subheader("2. Configuração da análise")
    
    c1, c2, c3 = st.columns(3)
    secao = c1.selectbox("Seção do Texto", nomes_secoes)
    nivel = c2.selectbox("Nível de rigor", nomes_niveis)
    selecionados = c3.multiselect("Agentes disponíveis", nomes_agentes)

    st.markdown("---")
    
    # --- ÁREA DE TEXTO COM BOTÃO DE LIMPEZA ---
    col_label, col_btn_clean = st.columns([4, 1])
    with col_label:
        st.subheader("3. O texto a ser analisado")
    with col_btn_clean:
        # Botão interativo que chama a função de limpar
        st.button("🧹 Consertar texto", on_click=limpar_texto, help="Remove quebras de linha de PDFs mantendo os parágrafos.")

    # A Key conecta este campo ao st.session_state para que a função limpar_texto funcione
    texto = st.text_area(
        "Insira o conteúdo", 
        height=300, 
        placeholder="Cole aqui o texto do seu TCC...",
        key="texto_input" 
    )

    st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
    
    # Botão de Envio
    col_vazia, col_btn = st.columns([4, 1])
    with col_btn:
        # Botão normal (não é form_submit_button pois removemos o st.form)
        enviar = st.button("🚀 Iniciar Análise", use_container_width=True, type="primary")

# -------------------------------------------------------------------------
# 6. PROCESSAMENTO DO ENVIO
# -------------------------------------------------------------------------
if enviar:
    # Validações Básicas
    # Usamos st.session_state.texto_input para garantir que pegamos a versão limpa se houver
    texto_final = st.session_state.texto_input if "texto_input" in st.session_state else texto

    if not titulo or not texto_final:
        st.warning("Por favor, preencha o título e o texto.", icon="⚠️")
        st.stop()
        
    if len(selecionados) < 1:
        st.warning("É necessário selecionar ao menos um agente.", icon="⚠️")
        st.stop()

    ids_selecionados = [mapa_agentes[n] for n in selecionados]

    payload = {
        "title": titulo,
        "area": area,
        "section": mapa_secoes[secao],
        "rigor": mapa_niveis[nivel],
        "text": texto_final,
        "agents": ids_selecionados
    }

    # UX: Feedback de carregamento
    with st.spinner("O ARAMIS está processando seu texto, aguarde um instante..."):
        resposta = api_client.analyze(payload)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        st.session_state["json_resultado"] = dados
        st.switch_page("pages/result_page.py")
        
    elif resposta.status_code == 500:
        st.error("Erro no Servidor Interno. Tente novamente mais tarde.", icon="🚨")
    else:
        try:
            erro_msg = resposta.json().get('detail', 'Erro desconhecido')
            st.warning(f"Não foi possível concluir: {erro_msg}", icon="⚠️")
        except:
            st.error(f"Erro inesperado: {resposta.status_code}", icon="🚨")