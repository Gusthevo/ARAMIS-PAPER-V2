import streamlit as st

def apply_custom_style():
    st.markdown(
        """
        <style>

        /* =========================
           RESET E BASE
        ========================== */

        html, body, [class*="css"] {
            font-family: "Inter", "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
            color: #0f172a;
        }

        body {
            background-color: #f8fafc;
        }

        /* Container principal */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        /* =====================a====
           TÍTULOS E TEXTO
        ========================== */

        h1 {
            font-weight: 700;
            letter-spacing: -0.03em;
        }

        h2 {
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
        }

        h3, h4 {
            font-weight: 600;
        }

        p {
            line-height: 1.6;
        }

        .stCaption {
            color: #64748B;
            font-size: 0.95rem;
        }

        /* =========================
           BOTÕES
        ========================== */

        .stButton > button {
            border-radius: 10px;
            padding: 0.6rem 1rem;
            font-weight: 600;
            transition: all 0.15s ease-in-out;
            background-color: #f1f5f9;
            border: 1px solid #e5e7eb;
        }

        .stButton > button:hover {
            background-color: #2563eb;
            color: #ffffff;
            border-color: #2563eb;
            transform: translateY(-1px);
        }

        /* Botão primário */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #2563EB, #1D4ED8);
            color: #ffffff;
            border: none;
        }

        .stButton > button[kind="primary"]:hover {
            filter: brightness(1.05);
        }

        /* =========================
           CARDS
        ========================== */

        .card {
            background-color: #ffffff;
            border-radius: 14px;
            padding: 1.4rem;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }

        /* Remove containers vazios */
        div[data-testid="stContainer"]:empty {
            padding: 0 !important;
            margin: 0 !important;
            background: transparent !important;
        }

        /* =========================
           EXPANDER
        ========================== */

        details {
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            padding: 0.6rem 1rem;
            background-color: #ffffff;
        }

        summary {
            font-weight: 600;
            cursor: pointer;
        }

        /* =========================
           SIDEBAR (LIGHT)
        ========================== */

        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #e5e7eb;
        }

        section[data-testid="stSidebar"] * {
            color: #0f172a;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #020617;
        }

        /* =========================
           ALERTAS
        ========================== */

        div[data-testid="stAlert"] {
            border-radius: 12px;
            font-size: 0.95rem;
        }

        /* =========================
           INPUTS
        ========================== */

        input, textarea, select {
            border-radius: 10px !important;
        }

        textarea {
            line-height: 1.6;
        }

        /* =========================
           DIVIDER
        ========================== */

        hr {
            border: none;
            border-top: 1px solid #e5e7eb;
            margin: 2rem 0;
        }

        /* =========================
           RESPONSIVIDADE
        ========================== */

        @media (max-width: 768px) {
            h1 {
                font-size: 2.2rem;
            }

            .block-container {
                padding-left: 1.2rem;
                padding-right: 1.2rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )
