# 🦜 LangChain/LangGraph - Apprentissage par Projet

## 📚 Vue d'ensemble

LangChain est le framework le plus populaire pour développer des applications avec des modèles de langage. LangGraph ajoute des capacités de workflows stateful et de routage conditionnel.

### 🎯 Cas d'usage principaux
- **RAG complexe** : Systèmes de question-réponse avec documents
- **Workflows multi-étapes** : Orchestration de tâches complexes  
- **Intégration APIs** : Connexion avec 100+ services externes
- **Monitoring production** : Observabilité et métriques avancées

## 📂 Structure du Projet

```
langchain-langgraph/
├── my_rag_system_starter.py     # 🎯 Template principal avec TODOs guidés
├── STEP_BY_STEP_GUIDE.md        # 📖 Guide d'apprentissage progressif
└── documents/                   # 📄 Documents d'exemple (auto-générés)
```

### 🎓 Approche Pédagogique
Ce module utilise l'**apprentissage par projet** : vous apprenez LangChain/LangGraph en construisant un système RAG complet avec 13 étapes guidées.

## 🚀 Installation

```bash
# Dépendances principales
pip install langchain langchain-openai langchain-community

# Pour RAG et vectorisation
pip install chromadb pypdf

# Pour LangGraph
pip install langgraph

# Pour monitoring
pip install langsmith
```

## ⚙️ Configuration

Créez un fichier `.env` :

```bash
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langsmith_key_here  # Optionnel pour monitoring
```

## 🚀 Démarrage du Projet

### 📖 Guide Complet d'Apprentissage

1. **Lisez le guide étape par étape** : [`STEP_BY_STEP_GUIDE.md`](./STEP_BY_STEP_GUIDE.md)
2. **Ouvrez le template** : [`my_rag_system_starter.py`](./my_rag_system_starter.py)
3. **Suivez les 13 TODOs** dans l'ordre pour apprendre

### 🎯 Progression d'Apprentissage

```bash
# 1. Installer et configurer
pip install langchain langchain-openai langchain-community chromadb langgraph pypdf
cp .env.example .env  # Ajouter votre OPENAI_API_KEY

# 2. Lancer le template
python my_rag_system_starter.py

# 3. Suivre les TODOs dans l'ordre :
#    TODO 1-2: Setup et imports
#    TODO 3-4: Architecture et métriques  
#    TODO 5-6: Initialisation
#    TODO 7-8: Pipeline RAG
#    TODO 9-10: Workflow LangGraph
#    TODO 11-13: Query et monitoring
```

### 📚 Ce que Vous Apprendrez

| TODO | Concept | Durée |
|------|---------|-------|
| 1-2 | **Écosystème LangChain** - Imports et architecture | 5 min |
| 3-4 | **États et métriques** - Workflows stateful | 10 min |
| 5-6 | **Configuration** - Services IA et documents | 12 min |
| 7-8 | **Pipeline RAG** - Ingestion et chaînes | 25 min |
| 9-10 | **LangGraph** - Workflows et monitoring | 20 min |
| 11-13 | **Production** - Query et métriques | 15 min |

## 🎬 Votre Système RAG en Action

### 🤖 **Ce que Votre Système LangChain Fera Concrètement**

**Démonstration avec documents techniques** :

```
📄 DOCUMENTS INGÉRÉS:
- "Guide_IA_2024.pdf" (45 pages)
- "Best_Practices_ML.txt" (12 pages)  
- "Architecture_Agents.md" (8 pages)

👤 USER: "Comment optimiser les performances d'un agent IA ?"

🔍 SYSTÈME RAG LANGCHAIN:

📊 Analyse complexité: "Question technique avancée → Workflow complexe"

🔎 Recherche vectorielle:
   ✅ Trouvé 4 passages pertinents dans Guide_IA_2024.pdf (pages 23-25)
   ✅ Trouvé 2 passages dans Best_Practices_ML.txt (section Performance)
   
🧠 LangGraph Workflow:
   1. Route → Analyse complexe
   2. Enrichissement → Sources multiples 
   3. Synthèse → Réponse structurée
   4. Validation → Score qualité: 94%

🎯 RÉPONSE GÉNÉRÉE:
"Pour optimiser les performances d'un agent IA, voici les approches clés:

## 🚀 Optimisations Techniques
1. **Prompts optimisés**: Réduire de 40% les tokens (Guide_IA_2024.pdf, p.23)
2. **Caching intelligent**: Mise en cache des requêtes fréquentes
3. **Modèles adaptés**: Choisir le bon modèle par tâche

## 📊 Métriques de Performance  
- Latence cible: <3s par requête
- Accuracy: >90% sur votre domaine
- Coût: Optimisation token/réponse

**Sources citées:**
- Guide_IA_2024.pdf, pages 23-25 ✅
- Best_Practices_ML.txt, section Performance ✅"

📊 MÉTRIQUES AUTOMATIQUES:
⏱️ Temps réponse: 4.2s | 💰 Coût: $0.003 | 🎯 Score qualité: 94%
📈 Monitoring: conversation_metrics.json mis à jour
```

### 🏆 **Résultat Final Concret**

À la fin, vous aurez un **système RAG production-ready** qui :
- **Ingestion automatique** : PDF/TXT → vectorisation → base de connaissances
- **Q&A intelligent** : Questions → recherche sémantique → réponses avec sources
- **Routage adaptatif** : Simple/complexe → workflow LangGraph optimisé
- **Monitoring temps réel** : Latence, coûts, qualité → métriques JSON
- **Production ready** : Gestion erreurs, retry logic, observabilité

## 🎓 Validation des Compétences

### ✅ **Critères de Réussite**

Votre projet est réussi quand vous avez complété **tous les TODOs** et votre système :

#### 📊 **Performance** :
- Répond en < 5s par requête
- Ingère des documents sans erreur
- Affiche des métriques temps réel

#### 🎯 **Fonctionnalités** :
- Pipeline RAG complet (ingestion → vectorisation → Q&A)
- Workflow LangGraph avec routage intelligent 
- Monitoring avec métriques de coûts et performance
- Documentation générée automatiquement

#### 🎬 **Démonstration** :
Votre système doit réussir la démonstration automatique avec les 5 questions test du `run_demo()`.

### 📁 **Fichiers Générés**

Après complétion des TODOs, vous aurez créé :
```
langchain-langgraph/
├── my_rag_system_starter.py     # ✅ Votre implémentation complète
├── documents/                   # ✅ Documents d'exemple
├── chroma_db/                   # ✅ Base vectorielle persistante  
├── metrics.json                 # ✅ Métriques de performance
└── STEP_BY_STEP_GUIDE.md        # 📖 Guide de référence
```

### 🏆 **Validation Finale**

Pour valider vos acquis, vous devez pouvoir :
- [ ] Expliquer le pipeline RAG end-to-end
- [ ] Modifier les prompts pour votre domaine
- [ ] Ajouter de nouveaux types de documents
- [ ] Comprendre les métriques de performance
- [ ] Adapter le routage LangGraph pour vos besoins

## 🚀 Personnalisation et Extensions

### 🎯 **Adapter à Votre Domaine**

Une fois les TODOs complétés, personnalisez votre système :

#### 📄 **Vos Documents** :
```bash
# Remplacez les documents d'exemple
rm -rf documents/*
# Ajoutez vos PDF/TXT dans documents/
cp ~/mes-docs/* documents/
```

#### 🎨 **Prompts Spécialisés** :
```python
# Dans TODO 8, modifiez le template
template = """Tu es un expert en [VOTRE DOMAINE].
Utilise le contexte pour répondre avec l'expertise de [VOTRE SECTEUR].

Contexte: {context}
Question: {question}

Réponse d'expert :"""
```

#### 🔄 **Routage Personnalisé** :
```python
# Dans TODO 9, adaptez la logique de complexité
def analyze_query(state):
    question = state["question"]
    # Votre logique métier spécifique
    if "technique" in question.lower():
        state["routing_decision"] = "complex"
    return state
```

### ⚡ **Optimisations Avancées**

#### 📈 **Performance** :
- Caching des embeddings fréquents
- Chunking optimisé pour votre type de documents
- Recherche hybride (semantic + keyword)

#### 💰 **Coûts** :
- Modèles locaux avec Ollama
- Embeddings moins chers (text-embedding-3-small)
- Rate limiting intelligent

#### 🔍 **Qualité** :
- Évaluation automatique des réponses
- Feedback utilisateur intégré
- Re-ranking des résultats

## 🔧 Patterns avancés

### Pattern Agent avec outils
```python
from langchain.agents import create_openai_functions_agent
from langchain.tools import Tool

# Définir des outils
tools = [
    Tool(name="Calculator", func=calculator, description="Calculs mathématiques"),
    Tool(name="Search", func=search, description="Recherche web")
]

# Créer l'agent
agent = create_openai_functions_agent(llm, tools, prompt)
```

### Pattern RAG avec filtres
```python
# Filtrage par métadonnées
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 4,
        "filter": {"source": "documentation"}
    }
)
```

### Pattern Streaming
```python
# Réponses en streaming
for chunk in chain.stream({"input": "Question"}):
    print(chunk, end="", flush=True)
```

## 📈 Métriques de performance

### Temps de réponse cibles :
- **Chaînes simples** : < 2s
- **RAG queries** : < 5s  
- **Workflows complexes** : < 10s

### Qualité RAG :
- **Relevance score** : > 0.7
- **Context utilization** : > 80%
- **Answer accuracy** : > 90%

## 🚨 Troubleshooting

### Erreurs courantes :

**❌ "API Key not found"**
```bash
# Vérifiez votre .env
echo $OPENAI_API_KEY
```

**❌ "Chroma database locked"**
```bash
# Supprimez le dossier de la DB
rm -rf ./chroma_db
```

**❌ "Rate limit exceeded"**
```python
# Ajoutez des délais
import time
time.sleep(1)  # Entre les appels
```

**❌ "Memory usage high"**
```python
# Limitez la taille des chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Plus petit
    chunk_overlap=50
)
```

## 🔗 Ressources complémentaires

### Documentation officielle :
- [LangChain Docs](https://docs.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [LangSmith Platform](https://smith.langchain.com/)

### Tutoriels vidéo :
- [LangChain Crash Course](https://www.youtube.com/watch?v=lG7Uxts9SXs)
- [RAG from Scratch](https://www.youtube.com/watch?v=wd7TZ4w1mSw)

### Communauté :
- [Discord LangChain](https://discord.gg/langchain) (50K+ membres)
- [GitHub Discussions](https://github.com/langchain-ai/langchain/discussions)

## 💡 Conseils pour la production

### 🔒 Sécurité :
- Ne jamais exposer les clés API
- Valider toutes les entrées utilisateur
- Implémenter des rate limits

### ⚡ Performance :
- Utiliser le caching pour les embeddings
- Optimiser la taille des chunks RAG
- Implémenter le streaming pour l'UX

### 📊 Monitoring :
- Tracker toutes les métriques importantes
- Alertes sur les échecs/lenteurs
- Logs détaillés pour le debugging

### 🧪 Testing :
- Tests unitaires pour chaque composant
- Tests d'intégration end-to-end
- Tests de charge pour la scalabilité

---

🎯 **Objectif final** : Maîtriser LangChain pour créer des applications IA robustes et scalables en production !