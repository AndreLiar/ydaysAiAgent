# 📖 Module 1: Fondamentaux des Agents IA

## 🎯 Votre Mission (3h)

**Construire votre premier agent IA intelligent en maîtrisant les 3 patterns fondamentaux**

À la fin de ce module, vous aurez créé un agent complet qui :
- ✅ **Suit la boucle agentique** : Perception → Plan → Act → Reflect
- ✅ **Comprend l'équation** : **LLM + Tools + Memory = Agent**
- ✅ **Maîtrise 3 patterns de base** : Single Agent, Tool Use, Human-in-Loop
- ✅ **Fonctionne en production** : Avec validation automatique et métriques

## 🔄 Le Loop Agentique Universel

**Perception → Plan → Act → Reflect**

Tous les agents, qu'ils soient simples ou complexes, suivent cette boucle :

```python
class BaseAgent:
    def perceive(self, input_data) -> Dict[str, Any]:
        """Analyser l'input et le contexte"""
        pass
    
    def plan(self, perception) -> List[Dict[str, Any]]:
        """Créer un plan d'action"""
        pass
    
    def act(self, plan) -> List[Dict[str, Any]]:
        """Exécuter les actions planifiées"""
        pass
    
    def reflect(self, results, expected_outcome) -> Dict[str, Any]:
        """Évaluer les résultats et s'améliorer"""
        pass
```

## 📂 Structure du Projet

```
01-fondamentaux/
├── my_first_agent_starter.py     # 🎯 Template principal avec TODOs guidés
├── STEP_BY_STEP_GUIDE.md         # 📖 Guide d'apprentissage progressif
└── README.md                     # 📄 Ce guide d'introduction
```

### 🎓 Approche Pédagogique
Ce module utilise l'**apprentissage par projet** : vous apprenez les fondamentaux en construisant votre premier agent complet avec 8 étapes guidées.

## 📋 Prérequis Techniques

Avant de commencer ce module, assurez-vous d'avoir :

### ✅ **Niveau Python Requis**
- **Python intermédiaire** : Classes, fonctions, dictionnaires
- **APIs basiques** : Requêtes HTTP, JSON
- **Command line** : Utilisation du terminal/invite de commande
- **Variables d'environnement** : Configuration .env

### ✅ **Connaissances Recommandées**
- Notions d'**APIs REST** (GET/POST requests)
- Familiarité avec **pip** et **virtual environments**
- Compréhension basique des **LLMs** (ChatGPT, GPT-4)

### ⚠️ **Si vous êtes débutant Python**
Si ces concepts vous semblent nouveaux, nous recommandons de suivre d'abord :
- [Python Crash Course](https://ehmatthes.github.io/pcc/) (Chapitres 1-10)
- [APIs with Python](https://realpython.com/api-integration-in-python/) 

### 🛠️ **Setup Technique Requis**
- **Python 3.8+** installé sur votre machine
- **Clé API OpenAI** (gratuite pour commencer)
- **Éditeur de code** (VS Code recommandé)
- **Git** pour cloner les projets

## 🚀 Comment Démarrer (3 étapes simples)

### ⚙️ Étape 1: Installation (2 min)
```bash
# Installer les dépendances
pip install openai python-dotenv requests beautifulsoup4

# Configurer votre clé API OpenAI
cp .env.example .env
# Ouvrir .env et ajouter: OPENAI_API_KEY=votre_cle_ici
```

### 📖 Étape 2: Lire le Guide (5 min)
Ouvrez [`STEP_BY_STEP_GUIDE.md`](./STEP_BY_STEP_GUIDE.md) pour comprendre :
- Les concepts fondamentaux
- Les exemples de code détaillés
- Les explications pas à pas

### 💻 Étape 3: Coder votre Agent (2h30)
Ouvrez [`my_first_agent_starter.py`](./my_first_agent_starter.py) et suivez les **8 TODOs guidés** :

```bash
python my_first_agent_starter.py
```

**⚠️ Important** : Suivez les TODOs dans l'ordre numérique (1→2→3→...→8)

## 📋 Votre Feuille de Route (8 TODOs = 2h30)

| 🎯 TODO | 📚 Vous Apprendrez | ⏱️ Temps | ✅ Résultat |
|---------|-------------------|----------|-------------|
| **1-2** | Fondamentaux & Architecture | 15 min | Boucle agentique fonctionnelle |
| **3** | Intégration OpenAI LLM | 10 min | Agent qui parle avec GPT-4 |
| **4** | Pattern Single Agent | 20 min | Agent conversationnel simple |
| **5** | Pattern Tool Use Agent | 35 min | Agent avec calculatrice + recherche |
| **6** | Pattern Human-in-Loop | 20 min | Agent avec validation humaine |
| **7** | Orchestrateur intelligent | 30 min | Sélection automatique de patterns |
| **8** | Tests & Validation | 10 min | Système de métriques complet |

## 🏆 Votre Agent Final en Action

### 🤖 **Capacités Concrètes**

**1. 💬 Conversation Intelligente (Single Agent)**
- Répond naturellement comme ChatGPT
- Se souvient des conversations précédentes
- S'adapte à votre style (amical/formel)

**2. 🔧 Utilisation d'Outils (Tool Use Agent)**
- **Calculatrice** : Résout les problèmes de maths
- **Recherche** : Trouve des informations en ligne
- **Météo** : Donne la météo de n'importe quelle ville

**3. 👤 Validation Humaine (Human-in-Loop)**
- Détecte les sujets sensibles (finance, médical, décisions importantes)
- Demande votre approbation avant de répondre
- Bloque les réponses non autorisées

### 🎬 **Exemples Concrets d'Utilisation**

```
👤 User: "Salut ! Comment ça va ?"
🤖 Agent: [Single Agent] "Bonjour ! Je vais très bien, merci de demander..."

👤 User: "Combien font 15 × 8 + 42 ?"  
🤖 Agent: [Tool Use] 🔧 Calculatrice → "Le résultat est 162"

👤 User: "C'est une décision financière critique"
🤖 Agent: [Human-in-Loop] 🚨 "Validation requise" → Demande votre accord

👤 User: "Quel temps fait-il à Paris ?"
🤖 Agent: [Tool Use] 🌤️ Météo → "À Paris : Ensoleillé, 22°C"
```

### 🧠 **Orchestration Intelligente**
L'agent choisit automatiquement le bon pattern selon votre demande :
- Question simple → **Single Agent** (chat direct)
- Calcul/recherche → **Tool Use** (utilise les outils)
- Contenu sensible → **Human-in-Loop** (demande validation)

**💡 Résultat** : Un assistant personnel intelligent qui combine ChatGPT + outils + sécurité !

## ✅ Comment Savoir si Vous Avez Réussi

### 🎯 Tests Automatiques Intégrés
Le fichier `my_first_agent_starter.py` inclut un système de validation automatique qui vérifie :

- [ ] **Boucle agentique** : Votre agent suit bien Perception → Plan → Act → Reflect
- [ ] **Intégration LLM** : Communication avec OpenAI fonctionnelle  
- [ ] **Système d'outils** : Au moins 3 outils (calculatrice, recherche, météo)
- [ ] **Mémoire conversationnelle** : Historique des interactions sauvegardé
- [ ] **3 Patterns implémentés** : Single Agent, Tool Use, Human-in-Loop
- [ ] **Orchestration** : Sélection automatique du bon pattern

### 🏆 Score de Réussite
- **90-100%** : 🏆 Excellent - Prêt pour les patterns avancés
- **75-89%** : 🥇 Très bien - Quelques ajustements mineurs  
- **60-74%** : 🥈 Bien - Réviser les concepts manqués
- **<60%** : 🥉 À retravailler - Revoir les fondamentaux

### 📄 Fichiers Générés à la Fin
```
01-fondamentaux/
├── my_first_agent_starter.py               # ✅ Votre code complété
├── first_agent_results_YYYYMMDD_HHMMSS.json # ✅ Résultats de démonstration  
└── .env                                     # ✅ Configuration API
```

## 🚀 Étapes Suivantes

### 🎯 Une fois Module 1 maîtrisé (score ≥75%) :

**Option A - Frameworks** : [**Module 2**](../02-frameworks/) 
- Apprenez LangChain, AutoGen, CrewAI, Semantic Kernel
- Même patterns, outils professionnels différents

**Option B - Patterns Avancés** : [**Module 3**](../03-design-patterns/)
- Multi-Agent Collaboration, Self-Correction, RAG, Planning
- Systèmes d'agents sophistiqués

### 💡 Conseil
**Commencez par Module 2** si vous voulez découvrir les frameworks populaires, ou **sautez au Module 3** si vous maîtrisez déjà un framework et voulez apprendre les patterns avancés.

---

## 🚨 Troubleshooting - Erreurs Communes

### ❌ **Erreur: "OpenAI API key not found"**
**Symptôme** : `openai.AuthenticationError` ou `API key not found`
**Solution** :
```bash
# Vérifiez votre fichier .env
cat .env
# Doit contenir: OPENAI_API_KEY=sk-...

# Rechargez les variables
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('OPENAI_API_KEY'))"
```

### ❌ **Erreur: "Module not found"**
**Symptôme** : `ModuleNotFoundError: No module named 'openai'`
**Solution** :
```bash
# Vérifiez l'installation
pip list | grep openai
# Si absent: pip install openai python-dotenv requests beautifulsoup4

# Vérifiez l'environnement virtuel
which python
pip --version
```

### ❌ **Erreur: "Rate limit exceeded"**
**Symptôme** : `RateLimitError` ou requests too frequent
**Solution** :
```python
# Ajoutez des délais dans votre code
import time
time.sleep(1)  # Entre les appels API

# Vérifiez vos quotas OpenAI
# https://platform.openai.com/usage
```

### ❌ **Erreur: "Agent ne répond pas correctement"**
**Symptôme** : Réponses incohérentes ou non pertinentes
**Solution** :
```python
# Vérifiez le system_message
system_message = "Tu es un assistant précis et utile. Réponds toujours en français."

# Testez avec temperature plus basse
llm_config = {"temperature": 0.1}  # Au lieu de 0.7

# Déboguez le prompt complet
print(f"Prompt envoyé: {prompt}")
```

### ❌ **Erreur: "JSON decode error"**
**Symptôme** : `json.JSONDecodeError` lors du parsing
**Solution** :
```python
# Handling robuste
try:
    result = json.loads(response)
except json.JSONDecodeError:
    print(f"Réponse non-JSON: {response}")
    # Fallback ou retry
```

### 🆘 **Bloqué ? Checklist Debug**
1. ✅ Clé API OpenAI valide et créditée
2. ✅ Dépendances installées (`pip list`)
3. ✅ Fichier .env dans le bon répertoire
4. ✅ Python 3.8+ (`python --version`)
5. ✅ Connexion internet stable
6. ✅ TODO précédents complétés dans l'ordre

### 💬 **Support Communautaire**
- **Discord** : [Lien vers community support]
- **GitHub Issues** : Pour bugs du template
- **Stack Overflow** : Tag `ai-agents-python`

🎯 **Objectif** : Créer votre premier agent IA fonctionnel en 3h chrono ! 🚀