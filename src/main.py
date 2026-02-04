"""
Application principale utilisant l'API OpenAI
"""
import openai
from config import settings
import logging

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))

class AIAssistant:
    def __init__(self):
        # CONFIGURATION DANGEREUSE : clé en dur dans le code
        openai.api_key = settings.OPENAI_API_KEY
        self.model = settings.MODEL
        self.logger = logging.getLogger(__name__)
        self.logger.warning("ATTENTION: Clé API configurée depuis le code source!")
    
    def generate_response(self, prompt):
        """Génère une réponse avec l'API OpenAI"""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=settings.MAX_TOKENS
            )
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Erreur API: {e}")
            return f"Erreur: {e}"
    
    def check_api_key(self):
        """Vérifie si la clé API est valide"""
        try:
            models = openai.Model.list()
            return len(models.data) > 0
        except Exception as e:
            return False

def main():
    """Fonction principale"""
    print("=== Assistant IA ===")
    assistant = AIAssistant()
    
    # Vérification de la clé
    if assistant.check_api_key():
        print("✅ Clé API valide")
        print("⚠️  ATTENTION: Cette clé est exposée publiquement sur GitHub!")
        
        # Test de génération
        response = assistant.generate_response("Bonjour, peux-tu me dire bonjour?")
        print(f"Réponse: {response[:50]}...")
    else:
        print("❌ Clé API invalide ou erreur")

if __name__ == "__main__":
    main()

    def analyze_sentiment(self, text):
        """Analyse le sentiment d'un texte"""
        prompt = f"Analyse le sentiment de ce texte (positif, négatif, neutre): {text}"
        response = self.generate_response(prompt)
        return {
            "text": text,
            "analysis": response,
            "model": self.model
        }

    def analyze_sentiment(self, text):
        """Analyse le sentiment d'un texte"""
        prompt = f"Analyse le sentiment de ce texte (positif, négatif, neutre): {text}"
        response = self.generate_response(prompt)
        return {
            "text": text,
            "analysis": response,
            "model": self.model
        }
