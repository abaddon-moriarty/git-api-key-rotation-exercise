#!/bin/bash
# Script de déploiement - NE PAS UTILISER EN PRODUCTION

echo "Déploiement de l'application IA..."
echo "ATTENTION: Ce déploiement expose une clé API sensible!"

# Installation des dépendances
pip install -r requirements.txt

# Vérification que la clé fonctionne
python -c "
import openai
from config import settings
openai.api_key = settings.OPENAI_API_KEY
try:
    models = openai.Model.list()
    print(f'✅ Clé API valide, {len(models.data)} modèles disponibles')
except Exception as e:
    print(f'❌ Erreur avec la clé API: {e}')
    exit 1
"

# Démarrage de l'application
echo "Démarrage de l'application..."
nohup python src/main.py > app.log 2>&1 &
echo "Application démarrée (PID: $!)"
echo "⚠️  LA CLÉ API EST EXPOSÉE DANS config/settings.py"
