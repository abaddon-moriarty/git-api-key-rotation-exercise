#!/usr/bin/env python3
"""
Script de scan de sécurité - Détection de clés API exposées
"""
import re
import requests

def scan_for_api_keys(filepath):
    """Scan un fichier pour des clés API"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Patterns de clés API courantes
    patterns = {
        'openai': r'sk-[a-zA-Z0-9]{48}',
        'github': r'ghp_[a-zA-Z0-9]{36}',
        'stripe': r'sk_(live|test)_[a-zA-Z0-9]{24}',
        'aws': r'AKIA[0-9A-Z]{16}',
        'generic': r'[a-zA-Z0-9]{32,64}'
    }
    
    found_keys = {}
    for key_type, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            found_keys[key_type] = matches
    
    return found_keys

# Scan des fichiers du projet
import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py') or file.endswith('.env') or file.endswith('.json'):
            filepath = os.path.join(root, file)
            keys = scan_for_api_keys(filepath)
            if keys:
                print(f"⚠️  CLÉS API TROUVÉES dans {filepath}:")
                for key_type, key_list in keys.items():
                    print(f"   {key_type.upper()}: {len(key_list)} clé(s) trouvée(s)")
                    for key in key_list[:2]:  # Montre seulement 2 pour éviter l'exposition
                        print(f"     - {key[:10]}...{key[-6:]}")
