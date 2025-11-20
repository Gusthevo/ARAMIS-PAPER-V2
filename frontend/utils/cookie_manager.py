import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

def get_cookie_manager():
    """
    Retorna uma instância do gerenciador de cookies.
    A 'key' é usada para criptografar o cookie.
    """
    
    key = "123" 
    
    cookies = EncryptedCookieManager(
        prefix="aramis_app_",
        password=key,
    )
    
    if not cookies.ready():
        st.stop()
    
    return cookies

# Chave do cookie onde guardaremos o token
AUTH_TOKEN_KEY = "session_token"