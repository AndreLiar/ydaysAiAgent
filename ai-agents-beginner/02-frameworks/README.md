# 🔧 Module 2: Frameworks Modernes d'Agents IA

## 🎯 Objectifs d'Apprentissage (3h)

À la fin de ce module, vous maîtriserez :
- ✅ **LangChain/LangGraph** : Orchestration et workflows complexes
- ✅ **AutoGen** : Conversations multi-agents naturelles  
- ✅ **CrewAI** : Teams d'agents spécialisés
- ✅ **Semantic Kernel** : L'approche Microsoft

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

### **🦜 LangChain/LangGraph** - Orchestration Avancée
```
langchain-langgraph/
├── simple-chain.py          # Chaînes basiques
├── rag-pipeline.py          # Retrieval-Augmented Generation
├── langgraph-workflow.py    # Workflows avec états
└── monitoring-demo.py       # Observabilité intégrée
```

**Cas d'usage** : RAG complexe, workflows multi-étapes, intégration APIs

### **🤖 AutoGen** - Conversations Multi-Agents
```
autogen-dialogue/
├── two-agent-chat.py        # Dialogue simple
├── group-conversation.py    # Discussion de groupe
├── human-in-loop.py         # Intégration humaine
└── specialized-roles.py     # Agents avec rôles spécialisés
```

**Cas d'usage** : Brainstorming, code review, analyse collaborative

### **⚓ CrewAI** - Teams d'Agents
```
crewai-teams/
├── basic-crew.py           # Équipe simple
├── hierarchical-crew.py    # Structure hiérarchique
├── research-team.py        # Équipe de recherche
└── production-crew.py      # Déploiement production
```

**Cas d'usage** : Projets complexes, spécialisation métier, coordination

### **🔷 Semantic Kernel** - L'Approche Microsoft
```
semantic-kernel/
├── kernel-basics.py        # Concepts fondamentaux
├── plugins-demo.py         # Système de plugins
├── planners.py            # Planification automatique
└── memory-integration.py   # Intégration mémoire
```

**Cas d'usage** : Intégration Microsoft 365, planification, plugins

## 📊 Comparatif des Frameworks

| Framework | Complexité | Learning Curve | Production Ready | Ecosystem |
|-----------|------------|----------------|------------------|-----------|
| **LangChain** | ⭐⭐⭐⭐ | Steep | ✅ Excellent | 🔥 Huge |
| **AutoGen** | ⭐⭐⭐ | Medium | ✅ Good | 📈 Growing |
| **CrewAI** | ⭐⭐ | Easy | ✅ Good | 🌱 Emerging |
| **Semantic Kernel** | ⭐⭐⭐ | Medium | ✅ Enterprise | 🏢 Microsoft |

## 🎓 Exercices Pratiques

### **Exercice 1: RAG avec LangChain (45min)**
Créez un système RAG qui :
- Ingère des documents PDF
- Répond à des questions avec citations
- Intègre monitoring et métriques

### **Exercice 2: Équipe AutoGen (30min)**
Implémentez une conversation entre :
- Agent Researcher (collecte d'infos)
- Agent Analyst (analyse des données)  
- Agent Writer (rédaction du rapport)

### **Exercice 3: CrewAI Production (30min)**
Déployez une équipe qui :
- Surveille les actualités tech
- Analyse l'impact sur votre secteur
- Génère un brief quotidien

### **Exercice 4: Semantic Kernel (15min)**
Testez l'intégration avec :
- Planification automatique
- Plugins personnalisés
- Mémoire persistante

## ✅ Validation des Compétences

À la fin du module, vous devrez :
- [ ] Implémenter un pipeline RAG complet avec LangChain
- [ ] Orchestrer une conversation à 3+ agents avec AutoGen
- [ ] Déployer une crew CrewAI avec rôles spécialisés
- [ ] Intégrer un planner Semantic Kernel

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

## 🚀 Next Steps

Une fois ce module maîtrisé, passez au **Module 3: Design Patterns** pour apprendre à choisir le bon pattern selon votre cas d'usage.

---

💡 **Pro Tip**: Commencez par CrewAI (le plus simple), puis AutoGen, LangChain, et enfin Semantic Kernel. Chaque framework a sa philosophie - testez-les tous pour trouver votre préféré !