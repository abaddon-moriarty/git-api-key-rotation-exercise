"""
Tests de l'assistant IA
ATTENTION: Ces tests utilisent la clé API exposée
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import AIAssistant
import unittest
from unittest.mock import patch

class TestAIAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = AIAssistant()
    
    def test_check_api_key(self):
        """Test que la clé API est valide"""
        # Ce test utilise la VRAIE clé exposée
        is_valid = self.assistant.check_api_key()
        self.assertTrue(is_valid, "La clé API devrait être valide")
    
    @patch('openai.ChatCompletion.create')
    def test_generate_response_mocked(self, mock_create):
        """Test avec mock pour éviter d'appeler la vraie API"""
        mock_create.return_value.choices[0].message.content = "Réponse mockée"
        response = self.assistant.generate_response("Test")
        self.assertEqual(response, "Réponse mockée")
    
    def test_api_key_exposure(self):
        """Test qui DEVRAIT échouer - vérifie que la clé n'est pas exposée"""
        from config import settings
        # Cette assertion échouera car la clé EST exposée
        self.assertNotIn("sk-", settings.OPENAI_API_KEY, 
                        "CLÉ API EXPOSÉE: la clé ne devrait pas être dans le code source!")

if __name__ == "__main__":
    unittest.main()
