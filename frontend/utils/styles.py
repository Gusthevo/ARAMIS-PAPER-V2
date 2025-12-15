import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* --- LIMPEZA DE VISUAL --- */
        /* Removemos apenas o rodapé 'Made with Streamlit', mas MANTEMOS o cabeçalho
           para garantir que o botão da sidebar sempre apareça */
        
        footer {
            visibility: hidden;
        }

        /* --- ESTILIZAÇÃO DOS COMPONENTES (Mantendo o visual bonito) --- */
        
        /* 1. Inputs arredondados e mais elegantes */
        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
            border-radius: 8px;
            border: 1px solid #E2E8F0;
            padding: 10px;
        }

        /* 2. Botões com sombra suave */
        .stButton button {
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease-in-out;
        }
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* 3. Containers / Cards */
        /* Ajuste sutil para containers com borda */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 10px;
            padding: 1rem;
        }
        
        /* 4. Tipografia */
        h1, h2, h3 {
            font-family: 'Inter', sans-serif;
            color: #1E293B;
        }
        </style>
        """, unsafe_allow_html=True)