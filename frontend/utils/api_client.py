import requests
import streamlit as st

class APIClient:
    def __init__(self):
        self.base_url = "http://backend:8000"
        self.session = requests.Session()
    
    def check_backend_health(self) -> bool:
        """Verifica se o backend está respondendo - SEM STREAMLINT NO MÉTODO"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    def register(self, username: str, email: str, password: str):
        """Faz cadastro de usuário"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/auth/register",
                json={
                    "username": username,
                    "email": email,
                    "password": password
                },
                timeout=10
            )
            return response
        except Exception:
            return None
    
    def login(self, username: str, password: str):
        """Faz login"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/auth/login",
                json={
                    "username": username,
                    "password": password
                },
                timeout=10
            )
            return response
        except Exception:
            return None
    
    def logout(self):
        """Faz logout"""
        try:
            response = self.session.post(f"{self.base_url}/api/auth/logout")
            return response
        except:
            return None
    
    def get_about_info(self):
        """Busca informações sobre a plataforma"""
        try:
            response = self.session.get(f"{self.base_url}/about", timeout=5)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

# Instância global
api_client = APIClient()