import requests
import streamlit as st

class APIClient:
    def __init__(self):
        self.base_url = "http://backend:8000"  # Nome do container Docker
        self.session = requests.Session()
    
    def _get_headers(self):
        """Retorna headers com autenticação se tiver token"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # 🔥 VERIFICA SE O TOKEN EXISTE NO SESSION_STATE
        if hasattr(st.session_state, 'session_token') and st.session_state.session_token:
            headers["Authorization"] = f"Bearer {st.session_state.session_token}"
            print(f"✅ _get_headers - Token adicionado: {st.session_state.session_token}")
        else:
            print("❌ _get_headers - Nenhum token disponível")
        
        return headers
    
    def check_backend_health(self) -> bool:
        """Verifica se o backend está respondendo"""
        try:
            response = self.session.get(
                f"{self.base_url}/health", 
                timeout=5,
                headers=self._get_headers()
            )
            return response.status_code == 200
        except Exception as e:
            print(f"Erro ao conectar com backend: {e}")
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
                timeout=10,
                headers=self._get_headers()
            )
            return response
        except Exception as e:
            print(f"Erro no registro: {e}")
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
                timeout=10,
                headers=self._get_headers()
            )
            return response
        except Exception as e:
            print(f"Erro no login: {e}")
            return None
    
    def logout(self):
        """Faz logout"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/auth/logout",
                headers=self._get_headers()
            )
            return response
        except Exception as e:
            print(f"Erro no logout: {e}")
            return None
            
    def validate_session(self):
        """
        Valida se a sessão é válida e RETORNA O JSON com dados do usuário.
        Retorna None se a sessão for inválida ou houver erro.
        """
        try:
            if not hasattr(st.session_state, 'session_token') or not st.session_state.session_token:
                print("❌ validate_session: Nenhum token encontrado no session_state")
                return None # 👈 CORREÇÃO: Retorna None
                
            print(f"🔍 validate_session - Token a ser enviado: {st.session_state.session_token}")
            
            headers = self._get_headers()
            print(f"🔍 validate_session - Headers: {headers}")
            
            response = self.session.get(
                f"{self.base_url}/api/auth/validate-session",
                headers=headers,
                timeout=5
            )
            
            print(f"🔍 validate_session - Status code: {response.status_code}")
            
            if response.status_code == 200:
                return response.json() # 👈 CORREÇÃO: Retorna o JSON de sucesso
            else:
                return None # 👈 CORREÇÃO: Retorna None em caso de falha (ex: 401)
                
        except Exception as e:
            print(f"❌ validate_session - Erro: {e}")
            return None # 👈 CORREÇÃO: Retorna None em caso de exceção
        
    def update_email(self, new_email: str, current_password: str):
        """Atualiza o email do usuário"""
        try:
            response = self.session.put(  # Ou POST, dependendo da sua API
                f"{self.base_url}/api/change/email",
                json={
                    "new_email": new_email,
                    "password": current_password
                },
                headers=self._get_headers(),
                timeout=10
            )
            return response
        except Exception as e:
            print(f"Erro ao atualizar email: {e}")
            return None

    def update_password(self, current_password: str, new_password: str):
        """Atualiza a senha do usuário"""
        try:
            response = self.session.put(  # Ou POST
                f"{self.base_url}/api/change/password",
                json={
                    "password": current_password,
                    "new_password": new_password
                },
                headers=self._get_headers(),
                timeout=10
            )
            return response
        except Exception as e:
            print(f"Erro ao atualizar senha: {e}")
            return None
        
    def get_about_info(self):
        """Busca informações sobre a plataforma"""
        try:
            response = self.session.get(
                f"{self.base_url}/about", 
                timeout=5,
                headers=self._get_headers()
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Erro ao buscar informações: {e}")
            return None

    def carregar_secoes(self):
        r = requests.get(f"{self.base_url}/api/analysis/sections")
        return r.json()["sections"]

    def carregar_agentes(self):
        r = requests.get(f"{self.base_url}/api/analysis/agents")
        return r.json()["agents"]

    def carregar_niveis(self):
        r = requests.get(f"{self.base_url}/api/analysis/rigor-levels")
        return r.json()["rigor_levels"]

    def analyze(self, payload: dict):
        try:
            response = self.session.post(
                f"{self.base_url}/api/analysis/analyze",
                json=payload,
                headers=self._get_headers()
            )
            return response
        except Exception as e:
            print(f"Erro na Analise: {e}")
            return None
        
    def get_corrections(self, user_id: int):
        try:
            response = self.session.get(
                f"{self.base_url}/api/analysis/corrections/{user_id}",
                headers=self._get_headers()
            )
            return response
        except Exception as e:
            print(f"Erro ao buscar correções: {e}")
            return None

# Instância global
api_client = APIClient()