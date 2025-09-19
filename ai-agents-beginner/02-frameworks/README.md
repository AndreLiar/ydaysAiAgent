# 🔧 Module 2: Frameworks Modernes d'Agents IA

## 🎯 Objectifs d'Apprentissage (5h)

À la fin de ce module, vous maîtriserez :
- ✅ **LangChain/LangGraph** : Orchestration et workflows complexes
- ✅ **AutoGen** : Conversations multi-agents naturelles  
- ✅ **CrewAI** : Teams d'agents spécialisés
- ✅ **Semantic Kernel** : L'approche Microsoft

## 📋 Prérequis Techniques

Avant de commencer ce module, assurez-vous d'avoir :

### ✅ **Niveau Python Requis**
- **Python avancé** : Classes, héritage, async/await, decorators
- **Frameworks** : Expérience avec au moins un framework Python
- **Gestion dépendances** : pip, requirements.txt, virtual environments
- **Debugging** : Lecture de stack traces, utilisation debugger

### ✅ **Connaissances Recommandées**  
- **Module 1 complété** : Patterns de base (Single Agent, Tool Use, Human-in-Loop)
- **APIs REST avancées** : Authentication, webhooks, rate limiting
- **Bases de données** : SQL/NoSQL, vectorielles (concepts)
- **Docker** : Concepts de base (optionnel mais utile)

### ⚠️ **Prérequis Obligatoires**
- ✅ **Module 1 terminé** avec score ≥75%
- ✅ **Python 3.9+** avec expérience frameworks
- ✅ **Clé API OpenAI** active avec crédits
- ✅ **16GB RAM minimum** pour les embeddings vectoriels

### 🛠️ **Setup Technique Avancé**
- **Multiple APIs** : OpenAI, potentially Anthropic, Google
- **Base vectorielle** : ChromaDB, FAISS
- **Processing** : Capacité de traitement documents volumineux
- **Network** : Connexion stable pour APIs externes

### 📚 **Ressources de Rattrapage**
Si Module 1 non complété ou niveau Python insuffisant :
- Revenir au [Module 1](../01-fondamentaux/) d'abord
- [Advanced Python](https://realpython.com/python-async-await/) pour async/await
- [Vector Databases](https://www.pinecone.io/learn/vector-database/) pour concepts RAG

## 🚀 Pourquoi Ces Frameworks?

### **Production-Ready**
Ces frameworks sont utilisés par:
- **OpenAI** → patterns LangChain dans GPTs
- **Microsoft** → Semantic Kernel dans Copilot
- **Google** → AutoGen pour Bard
- **Startups** → CrewAI pour agents collaboratifs

### **Avantages vs Code from Scratch**
- ✅ **Robustesse** : gestion d'erreurs, retry logic, monitoring
- ✅ **Intégrations** : 100+ outils/APIs pré-connectés
- ✅ **Patterns** : workflows éprouvés en production
- ✅ **Community** : support, docs, écosystème

## 📂 Structure du Module

### **🦜 LangChain/LangGraph** - Système RAG Production
```
langchain-langgraph/
├── my_rag_system_starter.py    # 🎯 Template principal avec TODOs
└── STEP_BY_STEP_GUIDE.md       # 📖 Guide d'apprentissage
```

**🎯 Ce que vous construirez** : Système Q&A intelligent avec documents
- 📄 Ingestion PDF/TXT → vectorisation → base de connaissances  
- 🔍 Questions → recherche sémantique → réponses avec sources citées
- ⚡ Workflow LangGraph adaptatif selon complexité (simple/avancé)
- 📊 Monitoring temps réel : latence, coûts, qualité

### **🤖 AutoGen** - Équipe Collaborative
```
autogen-dialogue/
├── my_research_team_starter.py  # 🎯 Template principal avec TODOs
└── STEP_BY_STEP_GUIDE.md        # 📖 Guide d'apprentissage
```

**🎯 Ce que vous construirez** : Équipe d'agents qui collabore naturellement
- 👥 4 agents spécialisés : Researcher → Analyst → Writer → Human Validator
- 💬 Conversation collaborative structurée (8-12 tours optimisés)
- 📝 Rapport professionnel automatique (15+ pages markdown)
- 👤 Validation humaine intégrée à 3+ points stratégiques

### **⚓ CrewAI** - Système de Veille 24/7
```
crewai-teams/
├── my_production_crew_starter.py  # 🎯 Template principal avec TODOs  
└── STEP_BY_STEP_GUIDE.md          # 📖 Guide d'apprentissage
```

**🎯 Ce que vous construirez** : Veille technologique automatisée
- 🔍 Crew hiérarchique : Manager → Data Collector → Web Researcher → Analyst
- 📊 Collecte automatisée multi-sources (ArXiv, TechCrunch, GitHub)
- 📈 Alertes intelligentes + scores de tendances (0-100)
- 📄 Rapports executives PDF + dashboards JSON temps réel

### **🔷 Semantic Kernel** - Assistant Personnel Intelligent
```
semantic-kernel/
├── my_intelligent_agent_starter.py  # 🎯 Template principal avec TODOs
└── STEP_BY_STEP_GUIDE.md            # 📖 Guide d'apprentissage
```

**🎯 Ce que vous construirez** : Agent avec mémoire et planification auto
- 🧠 Planification automatique : demande → décomposition → plugins → exécution
- 🔌 Plugins modulaires : Memory, Research, Strategy, Budget, Timeline
- 💾 Mémoire persistante : contexte utilisateur + préférences entre sessions
- 🏢 Intégration Microsoft : Office 365, Teams, SharePoint ready

## 📊 Comparatif des Frameworks

| Framework | Complexité | Learning Curve | Production Ready | Ecosystem |
|-----------|------------|----------------|------------------|-----------|
| **LangChain** | ⭐⭐⭐⭐ | Steep | ✅ Excellent | 🔥 Huge |
| **AutoGen** | ⭐⭐⭐ | Medium | ✅ Good | 📈 Growing |
| **CrewAI** | ⭐⭐ | Easy | ✅ Good | 🌱 Emerging |
| **Semantic Kernel** | ⭐⭐⭐ | Medium | ✅ Enterprise | 🏢 Microsoft |

## 🎓 Exercices Pratiques

### **Projet 1: Système RAG LangChain (2h10)**
**🎯 Mission** : Construire un Q&A intelligent avec documents techniques
**📋 Livrables concrets** :
- ✅ **Pipeline complet** : PDF "Guide_IA_2024.pdf" → vectorisation → réponses intelligentes
- ✅ **Q&A avancé** : "Comment optimiser un agent ?" → recherche sémantique → réponse avec sources  
- ✅ **Workflow adaptatif** : Questions simples/complexes → LangGraph routing automatique
- ✅ **Monitoring production** : Latence <5s, coût <$0.01/requête, qualité >90%
- 📄 **Démonstration** : 5 questions techniques → réponses parfaites avec sources citées
- 📁 **Fichiers générés** : `my_rag_system_starter.py` + `chroma_db/` + `metrics.json`

### **Projet 2: Équipe Collaborative AutoGen (2h05)**  
**🎯 Mission** : Orchestrer une équipe qui analyse "Impact IA sur l'éducation"
**📋 Livrables concrets** :
- ✅ **4 agents spécialisés** : Researcher → Analyst → Writer → Human Validator naturellement
- ✅ **Conversation fluide** : 8-12 tours optimisés → pas de boucles → consensus atteint
- ✅ **Rapport exécutif** : "Rapport_IA_Education_2024.md" (15+ pages structurées)
- ✅ **Validation experte** : 3+ points de contrôle humain → feedback intégré
- 📄 **Démonstration** : Sujet complexe → équipe collaborative → rapport professionnel  
- 📁 **Fichiers générés** : `my_research_team_starter.py` + `final_report.md` + `conversation_log.md`

### **Projet 3: Veille CrewAI 24/7 (2h05)**
**🎯 Mission** : Déployer surveillance "Tendances IA Q4 2024" automatisée  
**📋 Livrables concrets** :
- ✅ **Crew hiérarchique** : Manager → Data Collector → Web Researcher → Trend Analyst
- ✅ **Sources automatisées** : ArXiv, TechCrunch, GitHub → extraction → analyse → alertes
- ✅ **Intelligence temps réel** : "GPT-5 announcement imminent" → Score 94/100 → Action recommandée  
- ✅ **Rapports executives** : "Tendances_IA_Q4_2024_ExecutiveBrief.pdf" + dashboard JSON
- 📄 **Démonstration** : Processus 24/7 → détection nouveautés → rapports automatiques
- 📁 **Fichiers générés** : `my_production_crew_starter.py` + `daily_brief.md` + `metrics_dashboard.json`

### **Projet 4: Agent Semantic Kernel (1h15)**
**🎯 Mission** : Créer assistant "Stratégie Marketing Q1 2025" avec mémoire
**📋 Livrables concrets** :
- ✅ **Planification auto** : Demande → 6 étapes décomposées → plugins orchestrés automatiquement
- ✅ **Plugins intelligents** : Memory + Research + Strategy + Budget + Timeline modulaires
- ✅ **Mémoire persistante** : Contexte "SaaS B2B €50k" → préférences sauvegardées entre sessions
- ✅ **Livrables business** : "Marketing_Strategy_Q1_2025.pdf" + "Budget_Allocation_Optimized.xlsx"
- 📄 **Démonstration** : Demande complexe → planification → exécution → mémoire mise à jour
- 📁 **Fichiers générés** : `my_intelligent_agent_starter.py` + `plugins/` + `memory_state.json`

## ✅ Validation des Compétences

À la fin du module, vous devrez présenter 4 projets fonctionnels :

### 🦜 **Projet LangChain** - Système RAG Complet
- [ ] **Pipeline RAG** : Ingestion → Vectorisation → Q&A
- [ ] **Interface utilisateur** : Recherche intuitive avec sources
- [ ] **Monitoring** : Métriques temps réel et alertes
- [ ] **Performance** : < 5s par requête, >85% précision
- 📋 **Demo** : Répondre à 5 questions complexes avec sources

### 🤖 **Projet AutoGen** - Équipe Collaborative
- [ ] **Agents spécialisés** : 3+ rôles complémentaires
- [ ] **Conversation naturelle** : Tours de parole fluides
- [ ] **Validation humaine** : Points de contrôle stratégiques
- [ ] **Rapport structuré** : Synthèse professionnelle
- 📋 **Demo** : Analyse collaborative d'un sujet complexe

### ⚓ **Projet CrewAI** - Production Ready
- [ ] **Crew hiérarchique** : Délégation et coordination
- [ ] **Monitoring avancé** : Métriques et alertes temps réel
- [ ] **Scalabilité** : Gestion de charge et optimisation
- [ ] **Automatisation** : Processus end-to-end sans intervention
- 📋 **Demo** : Système de veille opérationnel 24/7

### 🔷 **Projet Semantic Kernel** - Agent Intelligent
- [ ] **Planification automatique** : Orchestration multi-étapes
- [ ] **Plugins modulaires** : Extensions réutilisables
- [ ] **Mémoire persistante** : Contexte entre sessions
- [ ] **Adaptation** : Apprentissage et amélioration continue
- 📋 **Demo** : Assistant personnel avec mémoire long-terme

## 🔗 Ressources Complémentaires

**Documentation Officielle** :
- [LangChain Docs](https://docs.langchain.com/) - Guides complets
- [AutoGen GitHub](https://github.com/microsoft/autogen) - Examples et tutorials
- [CrewAI Docs](https://docs.crewai.com/) - Getting started
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) - Microsoft Learn

**Communautés** :
- Discord LangChain (50K+ membres)
- AutoGen Discussions GitHub
- CrewAI Community Slack
- Semantic Kernel GitHub Issues

## 🚨 Troubleshooting - Erreurs Frameworks

### ❌ **LangChain: "Chroma database locked"**
**Symptôme** : `chromadb.errors.InvalidDimensionException` ou DB locked
**Solution** :
```bash
# Supprimez la base corrompue
rm -rf ./chroma_db
# Recréez avec embedding correct
embedding = OpenAIEmbeddings(model="text-embedding-3-small")
```

### ❌ **AutoGen: "Conversation stuck in loop"**
**Symptôme** : Agents tournent en boucle sans fin
**Solution** :
```python
# Limitez les tours automatiques
groupchat = GroupChat(
    max_round=8,  # Maximum 8 tours
    speaker_selection_method="round_robin",
    allow_repeat_speaker=False  # Évite répétitions
)
```

### ❌ **CrewAI: "Agent execution timeout"**
**Symptôme** : Tasks qui ne finissent jamais
**Solution** :
```python
# Ajoutez timeouts explicites
agent = Agent(
    role="Researcher",
    max_execution_time=300,  # 5 minutes max
    allow_delegation=False   # Évite délégations infinies
)
```

### ❌ **Semantic Kernel: "Plugin not found"**
**Symptôme** : `PluginNotFoundError` ou skill import fail
**Solution** :
```python
# Vérifiez l'import du plugin
kernel.import_semantic_skill_from_directory("./plugins", "MySkill")
# Ou enregistrez manuellement
kernel.add_function("my_function", my_function)
```

### ❌ **Memory/RAM issues avec embeddings**
**Symptôme** : `MemoryError` ou système qui lag
**Solution** :
```python
# Réduisez la taille des chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # Plus petit
    chunk_overlap=50
)
# Processez par batches
for batch in chunks[::100]:  # 100 par 100
    vectorstore.add_texts(batch)
```

### ❌ **API costs exploding**
**Symptôme** : Facture OpenAI élevée inattendue
**Solution** :
```python
# Monitoring des coûts
import tiktoken
encoder = tiktoken.get_encoding("cl100k_base")
tokens = len(encoder.encode(text))
cost = tokens * 0.0001  # Prix approximatif

# Rate limiting
import time
time.sleep(2)  # Entre requests
```

### 🆘 **Debug Framework-Specific**

#### 🦜 **LangChain Debug**
```python
# Activez debug verbose
llm = ChatOpenAI(temperature=0, verbose=True)
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
```

#### 🤖 **AutoGen Debug**
```python
# Loggez les messages
def message_callback(sender, recipient, message):
    print(f"{sender.name} → {recipient.name}: {message}")

# Ajoutez callback aux agents
agent.register("receive", message_callback)
```

#### ⚓ **CrewAI Debug**
```python
# Mode debug crew
crew = Crew(
    agents=[agent1, agent2],
    tasks=[task1, task2],
    verbose=True,  # Active debug
    debug=True     # Extra détails
)
```

### 🔧 **Performance Optimization**

#### 💾 **Mémoire**
- Limitez les embeddings simultanés
- Utilisez `gc.collect()` après gros processings
- Préférez streaming pour gros documents

#### ⚡ **Vitesse**
- Cachez les embeddings calculés
- Utilisez async pour appels parallèles
- Réduisez la température pour réponses plus rapides

#### 💰 **Coûts**
- Modèles moins chers: `gpt-3.5-turbo` pour tests
- Embeddings: `text-embedding-3-small` au lieu de `large`
- Batch les requêtes similaires

## 🚀 Next Steps

Une fois ce module maîtrisé, passez au **Module 3: Design Patterns** pour apprendre à choisir le bon pattern selon votre cas d'usage.

---

💡 **Pro Tip**: Commencez par CrewAI (le plus simple), puis AutoGen, LangChain, et enfin Semantic Kernel. Chaque framework a sa philosophie - testez-les tous pour trouver votre préféré !