# 🤖 AI Agents Cheatsheet

### 🧩 Definition

**AI Agent = LLM + Tools + Memory → Perform Task**

Frameworks: `Microsoft Semantic Kernel`, `LangChain / LangGraph`, `LlamaIndex`, `CrewAI`, `AutoGen`

---

##  🔄  Boucle Agentique Fondamentale

Perception → Planification → Action → Réflexion

Perception : recevoir une entrée (prompt, fichier, données d’API).

Planification : décomposer en étapes, choisir les actions à entreprendre.

Action : appeler des outils ou des API, exécuter les étapes.

Réflexion : évaluer les résultats, ajuster le plan si nécessaire.

---

## Bien sûr ! Voici la traduction en français :

---

## 🎨 **Modèles de Conception Agentique**

1. **Agent Unique**  
   - Un seul agent gère entièrement la tâche.  
   - ✅ Idéal pour : questions simples, résumés.

2. **Collaboration Multi-Agents**  
   - Un orchestrateur + des agents spécialisés (recherche, code, rédaction).  
   - ✅ Idéal pour : projets complexes à étapes multiples.

3. **Humain dans la Boucle**  
   - Pause pour validation humaine à des points de contrôle.  
   - ✅ Idéal pour : tâches sensibles, créatives ou à fort enjeu.

4. **Auto-Correction**  
   - L’agent réfléchit à son propre travail et corrige ses erreurs.  
   - ✅ Idéal pour : génération de code, nettoyage de données.

5. **Utilisation d’Outils**  
   - Le LLM sélectionne et appelle des outils externes (API, bases de données, scripts).  
   - Boucle : **Raisonner → Sélectionner l’outil → Agir → Observer → Affiner**  
   - ✅ Idéal pour : récupération d’informations en temps réel, automatisation de workflows, analyses.

6. **Agent RAG (Génération Augmentée par la Recherche)**  
   - Va au-delà du RAG statique → l’agent *planifie dynamiquement la récupération*.  
   - ✅ Idéal pour : support client, recherche scientifique, analyse de données.

7. **Agent Planificateur**  
   - Décompose les tâches en feuille de route avant d’agir.  
   - ✅ Idéal pour : objectifs multi-étapes (plan marketing, synthèse de recherche).

8. **Système Multi-Agents**  
   - Plusieurs rôles spécialisés (Chercheur, Rédacteur, Éditeur).  
   - Modèles de collaboration :  
     - *Hiérarchique* (le manager délègue).  
     - *Basé sur le dialogue* (les agents échangent).  
   - ✅ Frameworks : `CrewAI`, `AutoGen`

---


## ⚙️ **Construire des Agents Efficaces**

1. **Définir le Rôle et la Mission**  
   → Plus c’est spécifique, meilleures sont les performances.

2. **Équiper en Outils**  
   - Recherche, calcul, communication, opérations sur fichiers.

3. **Utiliser le LLM comme Cerveau**  
   - Modèles puissants (OpenAI, Anthropic) pour le raisonnement et la planification.

4. **Choisir un Framework**  
   - `LangGraph` → boucles et workflows complexes  
   - `AutoGen` → dialogue entre agents  
   - `CrewAI` → orchestration d’équipe
   - `LangChain` → agents séquentiels, accès à outils et données
   - `Semantic Kernel` → orchestration modulaire avec fonctions codées
   - `LlamaIndex` → accès intelligent à des données privées (documents, bases)

5. **Itérer**  
   - Tester → Corriger → Améliorer les prompts et outils → Affiner le workflow

---

## 📈 **Apprentissage et Amélioration**

- **Auto-réflexion / Auto-correction** → « Ai-je atteint l’objectif ? »  
- **RLHF (Retour Humain)** → récompenser les bons comportements  
- **Apprentissage de l’environnement** → s’adapter via les sorties d’outils et la mémoire  
- **Frameworks** : LangGraph et AutoGen permettent des boucles réflexives

---


## 🚀 Deployment Guide

**Phase 1: Preparation**

- Finalize logic, choose framework, secure API keys.

**Phase 2: Infrastructure**

- Separate envs, vector DB (Pinecone/Weaviate/pgvector), CI/CD pipeline.

**Phase 3: Containerization**

- Dockerize → Deploy (Cloud Run, Azure Container Apps, Lambda, Kubernetes).

**Phase 4: Monitoring**

- Logging, metrics (latency, cost, errors), versioning (blue-green deploys).

---

## 📡 Communication Protocols (Conceptual)

- **MCP (Message Communication Protocol):** structure/rules for agent messages.
- **A2A (Agent-to-Agent):** dialogue & collaboration rules.
- **NLWeb:** natural language navigation/interaction with the web.

---

## 💼 Real-World Applications

### Customer Service
AI agents handle support tickets, chat with users, reset passwords, and even process refunds.
- **Impact**: 70% ticket auto-resolution
- **ROI**: $100K/year savings in support costs

### Sales & Marketing
They generate leads, personalize outreach, analyze competitors, and run campaigns.
- **Impact**: 40% better conversion rates
- **ROI**: 25% increase in qualified leads

### E-commerce
Agents track orders, suggest products, recover abandoned carts, and manage inventory.
- **Impact**: 25% revenue increase
- **ROI**: 15% reduction in cart abandonment

### Healthcare
AI agents assist in diagnostics, schedule appointments, and monitor patient data.
- **Impact**: 50% admin time saved
- **ROI**: 30% more patient appointments per day

---

## 🔧 Quick Implementation Guide

### 1. Simple Agent (5 minutes)
```python
from openai import OpenAI

class SimpleAgent:
    def __init__(self, role="Assistant"):
        self.role = role
        self.client = OpenAI()
    
    def perceive(self, input_data):
        return {"user_input": input_data, "context": self.role}
    
    def plan(self, perception):
        return [{"action": "respond", "data": perception}]
    
    def act(self, plan):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": plan[0]["data"]["user_input"]}]
        )
        return response.choices[0].message.content
    
    def reflect(self, result):
        return {"success": True, "output": result}
```

### 2. Tool-Using Agent (15 minutes)
```python
from langchain.agents import create_openai_functions_agent
from langchain.tools import DuckDuckGoSearchRun

tools = [DuckDuckGoSearchRun()]
agent = create_openai_functions_agent(llm, tools, prompt)
```

### 3. Multi-Agent System (30 minutes)
```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments',
    tools=[search_tool]
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content',
    tools=[write_tool]
)

crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
```

---

✅ **TL;DR**:

AI Agents = **LLM (brain) + Tools (hands) + Memory (context)** running in a loop (**Perceive → Plan → Act → Reflect**), organized via **design patterns** (single, multi, human-in-loop, self-correcting, RAG, planning), powered by **frameworks** (LangGraph, AutoGen, CrewAI), and deployed with **DevOps best practices** (Docker, CI/CD, monitoring).

**Build portfolio-ready projects that demonstrate real business value!**