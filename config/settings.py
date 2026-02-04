"""
Configuration de l'application - AVEC CLÉ API EXPOSÉE
"""
import os

# Clé API OpenAI - EXPOSÉE PUBLIQUEMENT
OPENAI_API_KEY = "sk-proj-abc1234567890DEFGHIJKLMNOPQRSTUVWXYZ-987654321"

# Configuration de l'application
API_ENDPOINT = "https://api.openai.com/v1"
MODEL = "gpt-4"
MAX_TOKENS = 4096

# Base de données
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/db")

# Logging
LOG_LEVEL = "INFO"
DEBUG = False
