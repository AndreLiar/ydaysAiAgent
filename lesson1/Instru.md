
Ce fichier fournit des instructions pour travailler avec le code contenu dans ce dépôt.

## Commandes

### Installation et Dépendances
```bash
# Installer les dépendances Python
pip install -r requirements.txt

# Configurer les variables d’environnement
cp .env.example .env
# Modifier le fichier .env pour ajouter votre clé API OpenAI
```

### Exécution du Code
```bash
# Lancer la démo interactive complète avec tous les types d’agents
python ai_agents_complete_demo.py

# Lancer des démonstrations individuelles d’agents
python simple_agent.py               # Agent PPAR de base
python tool_agent_demo.py            # Agent utilisant des outils avec recherche web
python multi_agent_simple.py         # Système collaboratif multi-agents
```

## Vue d’Ensemble de l’Architecture

Ce dépôt est un tutoriel sur les agents IA, implémentant trois modèles fondamentaux d’agents :

### 1. Agent Simple (`simple_agent.py`)
- **Modèle** : Cycle PPAR (Percevoir-Planifier-Agir-Réfléchir)
- **Classe principale** : `SimpleAgent`
- Utilise directement l’API OpenAI pour des fonctionnalités basiques
- Illustre l’architecture fondamentale d’un agent

### 2. Agent Utilisant des Outils (`tool_agent_demo.py`, `tool_agent.py`)
- **Modèle** : Agent + Intégration d’outils externes
- **Framework** : LangChain avec les fonctions OpenAI
- **Outils** : Capacité de recherche web via DuckDuckGo
- **Classe principale** : `ToolUsingAgent`
- Montre comment un agent peut interagir avec des systèmes externes

### 3. Système Multi-Agents (`multi_agent_simple.py`, `multi_agent_system.py`)
- **Modèle** : Agents spécialistes collaboratifs
- **Framework** : CrewAI pour l’orchestration des agents
- **Agents** : Agent Chercheur + Agent Rédacteur travaillant en séquence
- **Classe principale** : `SimpleMultiAgentSystem`
- Démonstration de la collaboration entre agents et de la gestion des flux de travail

### Dépendances Clés
- **API OpenAI** : Capacités principales du modèle de langage
- **LangChain** : Intégration d’outils et framework d’agents
- **CrewAI** : Framework de collaboration multi-agents
- **Recherche DuckDuckGo** : Outil de recherche web pour l’information en temps réel

### Configuration de l’Environnement
- Nécessite `OPENAI_API_KEY` dans le fichier `.env`
- Tous les agents utilisent les modèles OpenAI (par défaut : GPT-4)
- La fonctionnalité de recherche web nécessite un accès à Internet

### Modèles de Communication des Agents
- Agent Simple : Interaction directe utilisateur ↔ agent
- Agent avec Outils : Utilisateur → Agent → Outils → Agent → Utilisateur
- Multi-Agent : Utilisateur → Chercheur → Rédacteur → Utilisateur (flux séquentiel)

---

Souhaitez-vous que je vous aide à adapter ce fichier pour un usage spécifique ou à le intégrer dans une documentation technique ?