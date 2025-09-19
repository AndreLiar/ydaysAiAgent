# 🎯 Guide Étape par Étape - Assistant Personnel Intelligent

## 📚 Vue d'Ensemble du Projet

Ce guide vous accompagne dans la construction de votre **assistant IA personnel** qui combine ChatGPT + outils + sécurité. Vous apprendrez en faisant - chaque étape vous enseigne des concepts clés tout en construisant un agent fonctionnel.

### 🎯 Votre Mission
Créer un assistant IA qui peut :
- **💬 Converser naturellement** comme ChatGPT
- **🔧 Utiliser des outils** (calculatrice, recherche, météo)
- **👤 Demander validation** pour contenus sensibles
- **🧠 Choisir automatiquement** le bon comportement

### 🎬 Exemples Concrets de Votre Agent Final
```
👤 "Salut ! Comment ça va ?"
🤖 [💬 Single Agent] "Bonjour ! Je vais très bien, merci de demander..."

👤 "Combien font 15 × 8 + 42 ?"  
🤖 [🔧 Tool Use] Calculatrice → "Le résultat est 162"

👤 "C'est une décision financière critique"
🤖 [👤 Human-in-Loop] 🚨 "Validation requise" → Demande votre accord

👤 "Quel temps fait-il à Paris ?"
🤖 [🔧 Tool Use] Météo → "À Paris : Ensoleillé, 22°C"
```

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
pip install openai python-dotenv requests

# 2. Configurer votre clé API
cp .env.example .env
# Ajouter votre OPENAI_API_KEY dans le fichier .env

# 3. Lancer le projet starter
python my_first_agent_starter.py
```

## 📋 Progression Étape par Étape

### ✅ TODO 1: Installation et Setup (3 min)

**Concepts appris**: Environnement de développement et dépendances

```bash
pip install openai python-dotenv requests beautifulsoup4
```

**Pourquoi ces packages ?**
- `openai`: Client officiel pour GPT-4 et modèles OpenAI
- `python-dotenv`: Gestion sécurisée des clés API
- `requests`: Appels HTTP pour intégrations externes
- `beautifulsoup4`: Parsing HTML pour agents web

### ✅ TODO 2: Architecture de Base (5 min)

**Concepts appris**: Fondements théoriques et boucle agentique

Implémentez la classe `BaseAgent` avec la boucle universelle:

```python
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
from datetime import datetime
import json

@dataclass
class AgentState:
    """État de l'agent entre les interactions"""
    conversation_history: List[Dict[str, Any]]
    tools_used: List[str]
    user_preferences: Dict[str, Any]
    session_id: str
    total_interactions: int = 0
    
    def __post_init__(self):
        if not self.conversation_history:
            self.conversation_history = []
        if not self.tools_used:
            self.tools_used = []
        if not self.user_preferences:
            self.user_preferences = {"language": "fr", "style": "friendly"}

class BaseAgent:
    """Agent IA suivant la boucle Perception → Plan → Act → Reflect"""
    
    def __init__(self):
        self.client = None  # Client OpenAI (TODO 3)
        self.state = AgentState(
            conversation_history=[],
            tools_used=[],
            user_preferences={},
            session_id=f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        self.available_tools = {}  # Registre des outils (TODO 5)
    
    def perceive(self, user_input: str) -> Dict[str, Any]:
        """Étape 1: Analyser l'input et le contexte"""
        perception = {
            "user_input": user_input,
            "timestamp": datetime.now().isoformat(),
            "input_length": len(user_input.split()),
            "intent": self._analyze_intent(user_input),
            "context": self._get_relevant_context(),
            "complexity": self._assess_complexity(user_input)
        }
        
        print(f"🔍 PERCEPTION: {perception['intent']} (complexité: {perception['complexity']})")
        return perception
    
    def plan(self, perception: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Étape 2: Créer un plan d'action"""
        plan = []
        
        # Planification basée sur l'intent détecté
        if perception["intent"] == "calculation":
            plan.append({"action": "use_tool", "tool": "calculator", "priority": 1})
        elif perception["intent"] == "information":
            plan.append({"action": "search_web", "tool": "web_search", "priority": 1})
        elif perception["intent"] == "conversation":
            plan.append({"action": "llm_response", "tool": "direct_llm", "priority": 1})
        elif perception["intent"] == "validation":
            plan.append({"action": "human_input", "tool": "human_loop", "priority": 1})
        
        # Toujours inclure une étape de réflexion
        plan.append({"action": "reflect", "tool": "self_assessment", "priority": 2})
        
        print(f"📋 PLAN: {len(plan)} étapes planifiées")
        return plan
    
    def act(self, plan: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Étape 3: Exécuter les actions planifiées"""
        results = []
        
        for step in sorted(plan, key=lambda x: x["priority"]):
            print(f"⚡ EXÉCUTION: {step['action']} avec {step['tool']}")
            
            if step["action"] == "use_tool":
                result = self._execute_tool(step["tool"], step.get("params", {}))
            elif step["action"] == "llm_response":
                result = self._call_llm(step.get("prompt", ""))
            elif step["action"] == "human_input":
                result = self._request_human_input(step.get("question", ""))
            elif step["action"] == "reflect":
                result = self._self_reflect(results)
            else:
                result = {"error": f"Action inconnue: {step['action']}"}
            
            results.append({
                "step": step,
                "result": result,
                "timestamp": datetime.now().isoformat()
            })
        
        return results
    
    def reflect(self, results: List[Dict[str, Any]], expected_outcome: str = "") -> Dict[str, Any]:
        """Étape 4: Évaluer les résultats et s'améliorer"""
        reflection = {
            "success": all(r.get("result", {}).get("error") is None for r in results),
            "quality_score": self._assess_quality(results),
            "lessons_learned": [],
            "improvements": [],
            "user_satisfaction": None  # À implémenter avec feedback utilisateur
        }
        
        # Analyser chaque résultat
        for result in results:
            if "error" in result.get("result", {}):
                reflection["lessons_learned"].append(f"Erreur avec {result['step']['tool']}")
                reflection["improvements"].append(f"Améliorer la gestion d'erreur pour {result['step']['action']}")
        
        # Mémoriser pour futures interactions
        self.state.conversation_history.append({
            "perception": results[0].get("perception", {}),
            "plan": [r["step"] for r in results],
            "results": [r["result"] for r in results],
            "reflection": reflection,
            "timestamp": datetime.now().isoformat()
        })
        
        print(f"🤔 RÉFLEXION: Succès={reflection['success']}, Qualité={reflection['quality_score']:.2f}")
        return reflection
    
    def _analyze_intent(self, user_input: str) -> str:
        """Analyser l'intention de l'utilisateur"""
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ["calcul", "addition", "multiplication", "combien"]):
            return "calculation"
        elif any(word in user_lower for word in ["recherche", "trouve", "information", "qu'est-ce"]):
            return "information"
        elif any(word in user_lower for word in ["valide", "vérifie", "confirme", "approuve"]):
            return "validation"
        else:
            return "conversation"
    
    def _get_relevant_context(self) -> Dict[str, Any]:
        """Récupérer le contexte pertinent"""
        recent_history = self.state.conversation_history[-3:] if self.state.conversation_history else []
        return {
            "recent_interactions": len(recent_history),
            "tools_previously_used": list(set(self.state.tools_used[-5:])),
            "user_preferences": self.state.user_preferences
        }
    
    def _assess_complexity(self, user_input: str) -> str:
        """Évaluer la complexité de la demande"""
        complexity_indicators = len([
            word for word in user_input.lower().split() 
            if word in ["et", "puis", "ensuite", "aussi", "également", "après", "avant"]
        ])
        
        if complexity_indicators >= 2:
            return "high"
        elif complexity_indicators == 1:
            return "medium"
        else:
            return "low"
```

**Architecture de l'Agent**:
- **Perception**: Analyse de l'input et du contexte
- **Plan**: Stratégie d'action basée sur l'intent
- **Act**: Exécution coordonnée des actions
- **Reflect**: Auto-évaluation et apprentissage

### ✅ TODO 3: Configuration LLM (5 min)

**Concepts appris**: Intégration OpenAI et gestion des modèles

Complétez l'initialisation du client OpenAI:

```python
import os
from openai import OpenAI

def __init__(self):
    # Vérifier la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
    
    # Initialiser le client OpenAI
    self.client = OpenAI(api_key=api_key)
    
    # Configuration par défaut
    self.llm_config = {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 500,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }
    
    # Initialiser l'état
    self.state = AgentState(
        conversation_history=[],
        tools_used=[],
        user_preferences={},
        session_id=f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    self.available_tools = {}
    
    print("✅ Agent initialisé avec GPT-4")
    print(f"🆔 Session: {self.state.session_id}")

def _call_llm(self, prompt: str, system_message: str = "") -> Dict[str, Any]:
    """Appeler le LLM avec gestion d'erreurs"""
    try:
        # Construire les messages
        messages = []
        
        if system_message:
            messages.append({"role": "system", "content": system_message})
        
        # Ajouter le contexte des conversations précédentes
        for interaction in self.state.conversation_history[-2:]:  # 2 dernières interactions
            if "user_input" in interaction:
                messages.append({"role": "user", "content": interaction["user_input"]})
            if "response" in interaction:
                messages.append({"role": "assistant", "content": interaction["response"]})
        
        # Ajouter le prompt actuel
        messages.append({"role": "user", "content": prompt})
        
        # Appel API avec retry logic
        response = self.client.chat.completions.create(
            model=self.llm_config["model"],
            messages=messages,
            temperature=self.llm_config["temperature"],
            max_tokens=self.llm_config["max_tokens"],
            top_p=self.llm_config["top_p"],
            frequency_penalty=self.llm_config["frequency_penalty"],
            presence_penalty=self.llm_config["presence_penalty"]
        )
        
        return {
            "content": response.choices[0].message.content,
            "model": response.model,
            "tokens_used": response.usage.total_tokens,
            "cost_estimate": response.usage.total_tokens * 0.00003,  # Estimation GPT-4
            "success": True
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "success": False,
            "fallback_response": "Désolé, je rencontre un problème technique. Pouvez-vous reformuler votre demande ?"
        }
```

**Bonnes Pratiques LLM**:
- **Context management**: Historique limité pour performance
- **Error handling**: Fallback en cas d'échec API
- **Cost tracking**: Estimation des coûts en tokens
- **Configuration flexible**: Paramètres ajustables

### ✅ TODO 4: Pattern 1 - Single Agent (10 min)

**Concepts appris**: Agent simple avec LLM direct

Implémentez le pattern Single Agent:

```python
class SingleAgent(BaseAgent):
    """Pattern 1: Agent simple avec réponse LLM directe"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Single Agent"
        print(f"🤖 Initialisation du pattern: {self.pattern_name}")
    
    async def handle_single_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête simple avec le pattern Single Agent"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - Traitement de: '{user_input}'")
        print("=" * 60)
        
        # Étape 1: Perception
        perception = self.perceive(user_input)
        
        # Étape 2: Plan simple pour Single Agent
        plan = [
            {"action": "llm_response", "tool": "direct_llm", "priority": 1, "prompt": user_input}
        ]
        print(f"📋 PLAN: Réponse LLM directe")
        
        # Étape 3: Action
        system_message = f"""Tu es un assistant IA personnel utile et amical.
        
Préférences utilisateur: {self.state.user_preferences}
Historique récent: {len(self.state.conversation_history)} interactions précédentes

Instructions:
- Réponds de manière claire et concise
- Adapte ton style aux préférences utilisateur
- Si tu ne sais pas quelque chose, dis-le honnêtement
- Sois proactif en suggérant des actions ou questions de suivi

Requête utilisateur: {user_input}"""

        result = self._call_llm(user_input, system_message)
        
        # Étape 4: Réflexion
        reflection = self.reflect([{"step": plan[0], "result": result}])
        
        # Mettre à jour l'état
        self.state.total_interactions += 1
        
        response_data = {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "response": result.get("content", result.get("fallback_response", "Erreur de traitement")),
            "success": result.get("success", False),
            "tokens_used": result.get("tokens_used", 0),
            "cost_estimate": result.get("cost_estimate", 0),
            "quality_score": reflection["quality_score"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"✅ Réponse générée: {result.get('success', False)}")
        print(f"💰 Coût estimé: ${response_data['cost_estimate']:.4f}")
        
        return response_data
    
    def demo_single_agent(self):
        """Démonstration du pattern Single Agent"""
        print(f"\n🎬 DÉMONSTRATION: Pattern {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Bonjour ! Comment allez-vous ?",
            "Expliquez-moi ce qu'est un agent IA en termes simples",
            "Quels sont les avantages des voitures électriques ?",
            "Pouvez-vous me donner 3 conseils pour mieux dormir ?",
            "Résumez l'histoire de l'intelligence artificielle en 100 mots"
        ]
        
        print(f"📋 Requêtes de test: {len(demo_queries)}")
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i}/{len(demo_queries)} ---")
            print(f"👤 Utilisateur: {query}")
            
            import asyncio
            response = asyncio.run(self.handle_single_request(query))
            
            print(f"🤖 Assistant: {response['response']}")
            print(f"📊 Qualité: {response['quality_score']:.2f}, Tokens: {response['tokens_used']}")
        
        print(f"\n🏆 Démonstration terminée!")
        print(f"📈 Total interactions: {self.state.total_interactions}")
        print(f"💾 Historique: {len(self.state.conversation_history)} conversations")
```

**Cas d'Usage Single Agent**:
- Q&A simple et direct
- Résumés de texte
- Explications conceptuelles
- Conseils et recommandations
- Classification de contenu

### ✅ TODO 5: Pattern 2 - Tool Use Agent (15 min)

**Concepts appris**: Intégration d'outils externes et sélection dynamique

Implémentez le système d'outils et le pattern Tool Use:

```python
import requests
from datetime import datetime
import json
import re

class ToolRegistry:
    """Registre des outils disponibles pour l'agent"""
    
    def __init__(self):
        self.tools = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Enregistrer les outils par défaut"""
        self.register_tool("calculator", self._calculator_tool)
        self.register_tool("web_search", self._web_search_tool)
        self.register_tool("weather", self._weather_tool)
        self.register_tool("time", self._time_tool)
        self.register_tool("url_checker", self._url_checker_tool)
    
    def register_tool(self, name: str, function):
        """Enregistrer un nouvel outil"""
        self.tools[name] = {
            "function": function,
            "description": function.__doc__ or f"Outil {name}",
            "registered_at": datetime.now().isoformat()
        }
        print(f"🔧 Outil enregistré: {name}")
    
    def get_tool(self, name: str):
        """Récupérer un outil par son nom"""
        return self.tools.get(name, {}).get("function")
    
    def list_tools(self) -> List[str]:
        """Lister tous les outils disponibles"""
        return list(self.tools.keys())
    
    def _calculator_tool(self, expression: str) -> Dict[str, Any]:
        """Calculatrice sécurisée pour opérations mathématiques"""
        try:
            # Sécuriser l'expression (seulement opérations de base)
            allowed_chars = set("0123456789+-*/.() ")
            if not all(c in allowed_chars for c in expression):
                return {"error": "Expression contient des caractères non autorisés"}
            
            # Évaluer l'expression
            result = eval(expression)
            
            return {
                "result": result,
                "expression": expression,
                "type": "calculation",
                "success": True
            }
            
        except Exception as e:
            return {
                "error": f"Erreur de calcul: {str(e)}",
                "expression": expression,
                "success": False
            }
    
    def _web_search_tool(self, query: str, max_results: int = 3) -> Dict[str, Any]:
        """Outil de recherche web simple (simulation)"""
        try:
            # En production: utiliser une vraie API de recherche (Serper, Bing, etc.)
            # Ici: simulation de résultats
            
            simulated_results = [
                {
                    "title": f"Résultat 1 pour '{query}'",
                    "url": f"https://example.com/result1?q={query.replace(' ', '+')}",
                    "snippet": f"Informations pertinentes sur {query}. Voici un contenu détaillé qui répond à votre recherche..."
                },
                {
                    "title": f"Guide complet: {query}",
                    "url": f"https://guide.com/{query.replace(' ', '-')}",
                    "snippet": f"Guide détaillé concernant {query} avec des exemples pratiques et des conseils d'experts..."
                },
                {
                    "title": f"FAQ - {query}",
                    "url": f"https://faq.com/questions/{query.replace(' ', '_')}",
                    "snippet": f"Questions fréquemment posées sur {query} avec des réponses complètes et à jour..."
                }
            ]
            
            return {
                "results": simulated_results[:max_results],
                "query": query,
                "total_found": len(simulated_results),
                "success": True,
                "note": "Résultats simulés - en production, utiliser une vraie API de recherche"
            }
            
        except Exception as e:
            return {
                "error": f"Erreur de recherche: {str(e)}",
                "query": query,
                "success": False
            }
    
    def _weather_tool(self, location: str) -> Dict[str, Any]:
        """Outil météo (simulation)"""
        try:
            # En production: utiliser OpenWeatherMap ou API similaire
            import random
            
            weather_conditions = ["Ensoleillé", "Nuageux", "Pluvieux", "Partiellement nuageux"]
            temperature = random.randint(5, 30)
            condition = random.choice(weather_conditions)
            
            return {
                "location": location,
                "temperature": f"{temperature}°C",
                "condition": condition,
                "humidity": f"{random.randint(30, 80)}%",
                "wind": f"{random.randint(5, 25)} km/h",
                "success": True,
                "note": "Données simulées - en production, utiliser une vraie API météo"
            }
            
        except Exception as e:
            return {
                "error": f"Erreur météo: {str(e)}",
                "location": location,
                "success": False
            }
    
    def _time_tool(self, timezone: str = "Europe/Paris") -> Dict[str, Any]:
        """Outil de gestion du temps"""
        try:
            now = datetime.now()
            
            return {
                "current_time": now.strftime("%H:%M:%S"),
                "current_date": now.strftime("%Y-%m-%d"),
                "day_of_week": now.strftime("%A"),
                "timezone": timezone,
                "timestamp": now.isoformat(),
                "success": True
            }
            
        except Exception as e:
            return {
                "error": f"Erreur temporelle: {str(e)}",
                "success": False
            }
    
    def _url_checker_tool(self, url: str) -> Dict[str, Any]:
        """Vérifier si une URL est accessible"""
        try:
            response = requests.head(url, timeout=5)
            
            return {
                "url": url,
                "status_code": response.status_code,
                "accessible": response.status_code == 200,
                "response_time": "< 5s",
                "success": True
            }
            
        except Exception as e:
            return {
                "url": url,
                "error": f"URL non accessible: {str(e)}",
                "accessible": False,
                "success": False
            }

class ToolUseAgent(BaseAgent):
    """Pattern 2: Agent avec utilisation dynamique d'outils"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Tool Use Agent"
        self.tool_registry = ToolRegistry()
        self.available_tools = self.tool_registry.tools
        print(f"🛠️ Initialisation du pattern: {self.pattern_name}")
        print(f"🔧 Outils disponibles: {', '.join(self.tool_registry.list_tools())}")
    
    def _detect_tool_need(self, user_input: str) -> List[str]:
        """Détecter quels outils sont nécessaires"""
        needed_tools = []
        user_lower = user_input.lower()
        
        # Détection basée sur mots-clés
        if any(word in user_lower for word in ["calcul", "addition", "multiplication", "division", "combien", "résultat"]):
            needed_tools.append("calculator")
        
        if any(word in user_lower for word in ["recherche", "trouve", "information", "cherche", "google"]):
            needed_tools.append("web_search")
        
        if any(word in user_lower for word in ["météo", "temps", "pluie", "soleil", "température"]):
            needed_tools.append("weather")
        
        if any(word in user_lower for word in ["heure", "date", "maintenant", "aujourd'hui", "temps"]):
            needed_tools.append("time")
        
        if any(word in user_lower for word in ["url", "site", "website", "accessible", "lien"]):
            needed_tools.append("url_checker")
        
        return needed_tools
    
    def _execute_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Exécuter un outil avec gestion d'erreurs"""
        tool_function = self.tool_registry.get_tool(tool_name)
        
        if not tool_function:
            return {
                "error": f"Outil '{tool_name}' non trouvé",
                "available_tools": self.tool_registry.list_tools(),
                "success": False
            }
        
        try:
            # Extraire le paramètre principal selon l'outil
            if tool_name == "calculator":
                result = tool_function(params.get("expression", ""))
            elif tool_name == "web_search":
                result = tool_function(params.get("query", ""), params.get("max_results", 3))
            elif tool_name == "weather":
                result = tool_function(params.get("location", "Paris"))
            elif tool_name == "time":
                result = tool_function(params.get("timezone", "Europe/Paris"))
            elif tool_name == "url_checker":
                result = tool_function(params.get("url", ""))
            else:
                result = tool_function(params)
            
            # Enregistrer l'utilisation de l'outil
            if tool_name not in self.state.tools_used:
                self.state.tools_used.append(tool_name)
            
            result["tool_used"] = tool_name
            return result
            
        except Exception as e:
            return {
                "error": f"Erreur exécution {tool_name}: {str(e)}",
                "tool_used": tool_name,
                "success": False
            }
    
    async def handle_tool_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête avec le pattern Tool Use"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - Traitement de: '{user_input}'")
        print("=" * 60)
        
        # Étape 1: Perception
        perception = self.perceive(user_input)
        
        # Étape 2: Plan avec détection d'outils
        needed_tools = self._detect_tool_need(user_input)
        
        plan = []
        if needed_tools:
            for tool in needed_tools:
                plan.append({
                    "action": "use_tool",
                    "tool": tool,
                    "priority": 1,
                    "params": self._extract_tool_params(user_input, tool)
                })
        
        # Toujours ajouter une synthèse LLM
        plan.append({
            "action": "llm_synthesis",
            "tool": "direct_llm",
            "priority": 2,
            "context": "tool_results"
        })
        
        print(f"📋 PLAN: {len(needed_tools)} outils + synthèse LLM")
        print(f"🔧 Outils sélectionnés: {', '.join(needed_tools) if needed_tools else 'Aucun'}")
        
        # Étape 3: Action
        tool_results = []
        
        # Exécuter les outils
        for step in [s for s in plan if s["action"] == "use_tool"]:
            print(f"⚡ Exécution outil: {step['tool']}")
            result = self._execute_tool(step["tool"], step["params"])
            tool_results.append({"tool": step["tool"], "result": result})
        
        # Synthèse avec LLM
        synthesis_prompt = self._build_synthesis_prompt(user_input, tool_results)
        llm_result = self._call_llm(synthesis_prompt)
        
        # Étape 4: Réflexion
        all_results = tool_results + [{"tool": "llm_synthesis", "result": llm_result}]
        reflection = self.reflect([{"step": {"action": "complete_workflow"}, "result": all_results}])
        
        # Mettre à jour l'état
        self.state.total_interactions += 1
        
        response_data = {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "tools_used": needed_tools,
            "tool_results": tool_results,
            "synthesis": llm_result.get("content", "Erreur de synthèse"),
            "success": all(r["result"].get("success", True) for r in tool_results),
            "tokens_used": llm_result.get("tokens_used", 0),
            "quality_score": reflection["quality_score"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"✅ Traitement terminé: {response_data['success']}")
        print(f"🔧 Outils utilisés: {len(needed_tools)}")
        
        return response_data
    
    def _extract_tool_params(self, user_input: str, tool_name: str) -> Dict[str, Any]:
        """Extraire les paramètres pour un outil spécifique"""
        params = {}
        
        if tool_name == "calculator":
            # Chercher une expression mathématique
            math_pattern = r'[\d+\-*/().\s]+'
            matches = re.findall(math_pattern, user_input)
            if matches:
                params["expression"] = matches[-1].strip()
        
        elif tool_name == "web_search":
            # Utiliser tout l'input comme requête
            params["query"] = user_input
            params["max_results"] = 3
        
        elif tool_name == "weather":
            # Chercher un nom de ville
            user_lower = user_input.lower()
            cities = ["paris", "lyon", "marseille", "toulouse", "nice", "nantes", "montpellier", "strasbourg"]
            for city in cities:
                if city in user_lower:
                    params["location"] = city.capitalize()
                    break
            else:
                params["location"] = "Paris"  # Par défaut
        
        elif tool_name == "time":
            params["timezone"] = "Europe/Paris"  # Par défaut
        
        elif tool_name == "url_checker":
            # Chercher une URL
            url_pattern = r'https?://[^\s]+'
            matches = re.findall(url_pattern, user_input)
            if matches:
                params["url"] = matches[0]
        
        return params
    
    def _build_synthesis_prompt(self, user_input: str, tool_results: List[Dict]) -> str:
        """Construire le prompt de synthèse avec résultats d'outils"""
        synthesis_prompt = f"""Tu es un assistant IA qui doit synthétiser les résultats d'outils pour répondre à l'utilisateur.

Requête utilisateur: {user_input}

Résultats des outils utilisés:
"""
        
        for tool_result in tool_results:
            tool_name = tool_result["tool"]
            result = tool_result["result"]
            
            synthesis_prompt += f"\n--- {tool_name.upper()} ---\n"
            
            if result.get("success", False):
                if tool_name == "calculator":
                    synthesis_prompt += f"Calcul: {result.get('expression')} = {result.get('result')}\n"
                elif tool_name == "web_search":
                    synthesis_prompt += f"Recherche: {result.get('query')}\n"
                    for i, res in enumerate(result.get("results", []), 1):
                        synthesis_prompt += f"{i}. {res['title']}: {res['snippet'][:100]}...\n"
                elif tool_name == "weather":
                    synthesis_prompt += f"Météo à {result.get('location')}: {result.get('condition')}, {result.get('temperature')}\n"
                elif tool_name == "time":
                    synthesis_prompt += f"Heure actuelle: {result.get('current_time')} le {result.get('current_date')}\n"
                elif tool_name == "url_checker":
                    synthesis_prompt += f"URL {result.get('url')}: {'Accessible' if result.get('accessible') else 'Non accessible'}\n"
            else:
                synthesis_prompt += f"Erreur: {result.get('error', 'Échec de l\'outil')}\n"
        
        synthesis_prompt += f"""
Instructions pour la synthèse:
1. Analyse tous les résultats d'outils ci-dessus
2. Réponds de manière complète et utile à la requête originale
3. Intègre toutes les informations pertinentes
4. Si certains outils ont échoué, mentionne-le brièvement
5. Sois concis mais informatif
6. Propose des actions de suivi si pertinentes

Synthèse:"""
        
        return synthesis_prompt
    
    def demo_tool_use_agent(self):
        """Démonstration du pattern Tool Use Agent"""
        print(f"\n🎬 DÉMONSTRATION: Pattern {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Combien font 15 * 8 + 42 ?",
            "Quelle est la météo à Paris aujourd'hui ?",
            "Recherche des informations sur l'intelligence artificielle",
            "Quelle heure est-il maintenant ?",
            "Calcule 100 / 4 et recherche des informations sur les mathématiques"
        ]
        
        print(f"📋 Requêtes de test: {len(demo_queries)}")
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i}/{len(demo_queries)} ---")
            print(f"👤 Utilisateur: {query}")
            
            import asyncio
            response = asyncio.run(self.handle_tool_request(query))
            
            print(f"🔧 Outils utilisés: {', '.join(response['tools_used']) if response['tools_used'] else 'Aucun'}")
            print(f"🤖 Synthèse: {response['synthesis'][:200]}...")
            print(f"📊 Succès: {response['success']}, Qualité: {response['quality_score']:.2f}")
        
        print(f"\n🏆 Démonstration terminée!")
        print(f"📈 Total interactions: {self.state.total_interactions}")
        print(f"🔧 Outils expérimentés: {len(set(self.state.tools_used))}")
```

**Cas d'Usage Tool Use Agent**:
- Calculs mathématiques complexes
- Recherche d'informations en temps réel
- Vérification de données externes
- Intégration avec APIs et services
- Traitement multi-étapes avec outils

### ✅ TODO 6: Pattern 3 - Human-in-the-Loop (10 min)

**Concepts appris**: Validation humaine et points de contrôle

Implémentez le pattern Human-in-the-Loop:

```python
class HumanInLoopAgent(BaseAgent):
    """Pattern 3: Agent avec validation humaine aux points critiques"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Human-in-the-Loop Agent"
        self.validation_threshold = 0.7  # Seuil de confiance pour validation
        self.critical_domains = ["finance", "medical", "legal", "security"]
        print(f"👤 Initialisation du pattern: {self.pattern_name}")
        print(f"⚖️ Seuil de validation: {self.validation_threshold}")
    
    def _assess_need_for_validation(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Évaluer si une validation humaine est nécessaire"""
        validation_indicators = {
            "high_impact": any(word in user_input.lower() for word in ["important", "critique", "urgent", "danger"]),
            "critical_domain": any(domain in user_input.lower() for domain in self.critical_domains),
            "uncertainty": any(word in user_input.lower() for word in ["peut-être", "probablement", "incertain"]),
            "financial": any(word in user_input.lower() for word in ["argent", "euro", "coût", "prix", "budget"]),
            "decision_making": any(word in user_input.lower() for word in ["décide", "choix", "option", "alternative"])
        }
        
        score = sum(validation_indicators.values()) / len(validation_indicators)
        
        return {
            "needs_validation": score >= self.validation_threshold,
            "confidence_score": 1 - score,
            "indicators": validation_indicators,
            "reason": self._get_validation_reason(validation_indicators)
        }
    
    def _get_validation_reason(self, indicators: Dict[str, bool]) -> str:
        """Obtenir la raison de la validation"""
        reasons = []
        if indicators["high_impact"]:
            reasons.append("Impact potentiellement élevé")
        if indicators["critical_domain"]:
            reasons.append("Domaine critique détecté")
        if indicators["financial"]:
            reasons.append("Implications financières")
        if indicators["decision_making"]:
            reasons.append("Prise de décision requise")
        
        return "; ".join(reasons) if reasons else "Validation préventive"
    
    def _request_human_validation(self, content: str, reason: str, options: List[str] = None) -> Dict[str, Any]:
        """Simuler une demande de validation humaine"""
        print(f"\n🚨 VALIDATION HUMAINE REQUISE")
        print(f"📋 Raison: {reason}")
        print(f"📄 Contenu à valider:")
        print(f"   {content}")
        
        if options:
            print(f"🔘 Options disponibles:")
            for i, option in enumerate(options, 1):
                print(f"   {i}. {option}")
        
        # Simulation de l'interaction humaine
        print(f"\n⏳ En attente de validation humaine...")
        
        # En production: vraie interface utilisateur
        # Ici: simulation automatique pour démo
        
        import random
        simulated_responses = [
            {"approved": True, "feedback": "Validé - procédez"},
            {"approved": True, "feedback": "Approuvé avec modifications mineures"},
            {"approved": False, "feedback": "Refusé - trop risqué"},
            {"approved": False, "feedback": "Reporté - plus d'informations nécessaires"}
        ]
        
        response = random.choice(simulated_responses)
        
        print(f"✅ Réponse humaine reçue: {'Approuvé' if response['approved'] else 'Refusé'}")
        print(f"💬 Feedback: {response['feedback']}")
        
        return {
            "approved": response["approved"],
            "feedback": response["feedback"],
            "timestamp": datetime.now().isoformat(),
            "validation_time": "3.2s",  # Simulé
            "validator": "human_operator",
            "success": True
        }
    
    async def handle_human_loop_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête avec le pattern Human-in-the-Loop"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - Traitement de: '{user_input}'")
        print("=" * 60)
        
        # Étape 1: Perception
        perception = self.perceive(user_input)
        
        # Étape 2: Évaluation du besoin de validation
        validation_assessment = self._assess_need_for_validation(user_input, perception)
        
        print(f"⚖️ Évaluation validation: {'Requise' if validation_assessment['needs_validation'] else 'Non requise'}")
        print(f"🎯 Score de confiance: {validation_assessment['confidence_score']:.2f}")
        
        # Étape 3: Plan avec points de validation
        plan = []
        
        # Générer une réponse initiale
        plan.append({
            "action": "llm_response",
            "tool": "direct_llm",
            "priority": 1,
            "prompt": user_input
        })
        
        # Ajouter validation si nécessaire
        if validation_assessment["needs_validation"]:
            plan.append({
                "action": "human_validation",
                "tool": "human_loop",
                "priority": 2,
                "reason": validation_assessment["reason"]
            })
            
            plan.append({
                "action": "post_validation_action",
                "tool": "conditional_llm",
                "priority": 3
            })
        
        print(f"📋 PLAN: {len(plan)} étapes {'avec validation' if validation_assessment['needs_validation'] else 'sans validation'}")
        
        # Étape 4: Exécution
        
        # 1. Générer réponse initiale
        initial_response = self._call_llm(user_input, self._build_careful_system_message())
        
        workflow_results = [{
            "step": "initial_response",
            "result": initial_response
        }]
        
        final_response = initial_response.get("content", "Erreur de génération")
        validation_result = None
        
        # 2. Validation humaine si requise
        if validation_assessment["needs_validation"]:
            validation_result = self._request_human_validation(
                content=final_response,
                reason=validation_assessment["reason"],
                options=["Approuver", "Modifier", "Refuser", "Reporter"]
            )
            
            workflow_results.append({
                "step": "human_validation",
                "result": validation_result
            })
            
            # 3. Action post-validation
            if validation_result["approved"]:
                print("✅ Validation approuvée - réponse autorisée")
                if "modification" in validation_result["feedback"].lower():
                    # Régénérer avec feedback
                    modification_prompt = f"""Modifie cette réponse selon le feedback humain:

Réponse originale: {final_response}

Feedback humain: {validation_result['feedback']}

Réponse modifiée:"""
                    
                    modified_response = self._call_llm(modification_prompt)
                    final_response = modified_response.get("content", final_response)
                    
                    workflow_results.append({
                        "step": "post_validation_modification",
                        "result": modified_response
                    })
            else:
                print("❌ Validation refusée - réponse bloquée")
                final_response = f"Désolé, je ne peux pas traiter cette requête. Raison: {validation_result['feedback']}"
        
        # Étape 5: Réflexion
        reflection = self.reflect(workflow_results)
        
        # Mettre à jour l'état
        self.state.total_interactions += 1
        
        response_data = {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "validation_required": validation_assessment["needs_validation"],
            "validation_reason": validation_assessment.get("reason"),
            "validation_result": validation_result,
            "final_response": final_response,
            "confidence_score": validation_assessment["confidence_score"],
            "approved": validation_result["approved"] if validation_result else True,
            "workflow_steps": len(workflow_results),
            "quality_score": reflection["quality_score"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"✅ Traitement terminé: {'Approuvé' if response_data['approved'] else 'Refusé'}")
        print(f"🔄 Étapes workflow: {response_data['workflow_steps']}")
        
        return response_data
    
    def _build_careful_system_message(self) -> str:
        """Construire un message système pour réponses prudentes"""
        return """Tu es un assistant IA responsable qui doit être particulièrement prudent.

Instructions spéciales:
- Sois conscient que tes réponses peuvent avoir un impact important
- Indique clairement tes limites et incertitudes
- Pour les sujets critiques (finance, médical, légal), recommande de consulter un expert
- Utilise des formulations prudentes: "Il semble que", "D'après mes informations", "Je recommande de vérifier"
- Si tu n'es pas sûr, dis-le ouvertement
- Propose toujours de chercher des informations supplémentaires

Ton rôle est d'être utile tout en restant responsable et transparent sur tes limites."""
    
    def demo_human_in_loop_agent(self):
        """Démonstration du pattern Human-in-the-Loop"""
        print(f"\n🎬 DÉMONSTRATION: Pattern {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Bonjour, comment ça va ?",  # Pas de validation
            "Peux-tu m'aider à choisir un investissement financier important ?",  # Validation requise
            "Quel est le traitement médical pour une migraine ?",  # Validation requise
            "Quelle est la capitale de la France ?",  # Pas de validation
            "Je dois prendre une décision critique pour mon entreprise",  # Validation requise
        ]
        
        print(f"📋 Requêtes de test: {len(demo_queries)}")
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i}/{len(demo_queries)} ---")
            print(f"👤 Utilisateur: {query}")
            
            import asyncio
            response = asyncio.run(self.handle_human_loop_request(query))
            
            print(f"⚖️ Validation requise: {'Oui' if response['validation_required'] else 'Non'}")
            if response['validation_required']:
                print(f"📋 Raison: {response['validation_reason']}")
                print(f"✅ Approuvé: {'Oui' if response['approved'] else 'Non'}")
            print(f"🤖 Réponse finale: {response['final_response'][:150]}...")
            print(f"📊 Confiance: {response['confidence_score']:.2f}, Étapes: {response['workflow_steps']}")
        
        print(f"\n🏆 Démonstration terminée!")
        print(f"📈 Total interactions: {self.state.total_interactions}")
        print(f"👤 Validations humaines simulées")
```

**Cas d'Usage Human-in-the-Loop**:
- Décisions à fort impact
- Domaines réglementés (finance, médical, légal)
- Validation de contenu sensible
- Contrôle qualité pour production
- Apprentissage supervisé

### ✅ TODO 7: Agent Orchestrateur Principal (15 min)

**Concepts appris**: Coordination des patterns et sélection intelligente

Créez l'agent principal qui orchestre les 3 patterns:

```python
class MyFirstAgent:
    """Agent principal orchestrant les 3 patterns fondamentaux"""
    
    def __init__(self):
        print("🚀 Initialisation de votre Premier Agent IA")
        print("=" * 60)
        
        # Initialiser les 3 patterns
        self.single_agent = SingleAgent()
        self.tool_agent = ToolUseAgent()
        self.human_loop_agent = HumanInLoopAgent()
        
        # État global
        self.global_state = {
            "total_requests": 0,
            "pattern_usage": {"single": 0, "tool": 0, "human_loop": 0},
            "success_rate": 0.0,
            "session_start": datetime.now().isoformat()
        }
        
        print("✅ Tous les patterns initialisés")
        print("🎯 Agent prêt pour l'interaction")
    
    def _select_optimal_pattern(self, user_input: str) -> str:
        """Sélectionner le pattern optimal pour la requête"""
        user_lower = user_input.lower()
        
        # Priorité 1: Human-in-the-Loop pour contenus sensibles
        sensitive_keywords = ["important", "critique", "décision", "finance", "medical", "urgent"]
        if any(keyword in user_lower for keyword in sensitive_keywords):
            return "human_loop"
        
        # Priorité 2: Tool Use pour requêtes nécessitant des outils
        tool_keywords = ["calcul", "recherche", "météo", "heure", "information", "combien", "trouve"]
        if any(keyword in user_lower for keyword in tool_keywords):
            return "tool"
        
        # Par défaut: Single Agent pour conversation simple
        return "single"
    
    async def process_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête en sélectionnant le pattern optimal"""
        self.global_state["total_requests"] += 1
        
        print(f"\n🎯 ORCHESTRATEUR - Requête #{self.global_state['total_requests']}")
        print(f"👤 Input: {user_input}")
        print("=" * 60)
        
        # Sélection du pattern
        selected_pattern = self._select_optimal_pattern(user_input)
        self.global_state["pattern_usage"][selected_pattern] += 1
        
        print(f"🧠 Pattern sélectionné: {selected_pattern.upper()}")
        
        # Exécution selon le pattern
        try:
            if selected_pattern == "single":
                result = await self.single_agent.handle_single_request(user_input)
            elif selected_pattern == "tool":
                result = await self.tool_agent.handle_tool_request(user_input)
            elif selected_pattern == "human_loop":
                result = await self.human_loop_agent.handle_human_loop_request(user_input)
            else:
                raise ValueError(f"Pattern inconnu: {selected_pattern}")
            
            # Enrichir avec métadonnées orchestrateur
            result["orchestrator"] = {
                "selected_pattern": selected_pattern,
                "request_number": self.global_state["total_requests"],
                "global_state": self.global_state.copy()
            }
            
            return result
            
        except Exception as e:
            error_result = {
                "error": f"Erreur orchestrateur: {str(e)}",
                "selected_pattern": selected_pattern,
                "user_input": user_input,
                "success": False,
                "timestamp": datetime.now().isoformat()
            }
            return error_result
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtenir les statistiques globales"""
        total_requests = self.global_state["total_requests"]
        
        if total_requests > 0:
            pattern_percentages = {
                pattern: (count / total_requests) * 100 
                for pattern, count in self.global_state["pattern_usage"].items()
            }
        else:
            pattern_percentages = {"single": 0, "tool": 0, "human_loop": 0}
        
        return {
            "session_duration": f"Depuis {self.global_state['session_start']}",
            "total_requests": total_requests,
            "pattern_distribution": pattern_percentages,
            "most_used_pattern": max(self.global_state["pattern_usage"], key=self.global_state["pattern_usage"].get) if total_requests > 0 else "Aucun",
            "tools_available": len(self.tool_agent.tool_registry.list_tools()),
            "agents_active": 3
        }
    
    async def run_complete_demo(self):
        """Démonstration complète des 3 patterns"""
        print(f"\n🎬 DÉMONSTRATION COMPLÈTE - 3 Patterns Fondamentaux")
        print("=" * 80)
        
        # Scénarios diversifiés pour tester tous les patterns
        demo_scenarios = [
            # Single Agent
            {"input": "Bonjour ! Peux-tu te présenter ?", "expected_pattern": "single"},
            {"input": "Explique-moi ce qu'est un agent IA", "expected_pattern": "single"},
            
            # Tool Use
            {"input": "Combien font 15 * 8 + 42 ?", "expected_pattern": "tool"},
            {"input": "Recherche des informations sur Python", "expected_pattern": "tool"},
            {"input": "Quelle est la météo à Paris ?", "expected_pattern": "tool"},
            
            # Human-in-the-Loop
            {"input": "Aide-moi à prendre une décision financière importante", "expected_pattern": "human_loop"},
            {"input": "C'est un sujet médical critique", "expected_pattern": "human_loop"},
        ]
        
        print(f"📋 Scénarios de test: {len(demo_scenarios)}")
        
        results = []
        
        for i, scenario in enumerate(demo_scenarios, 1):
            print(f"\n--- Scénario {i}/{len(demo_scenarios)} ---")
            print(f"👤 Input: {scenario['input']}")
            print(f"🎯 Pattern attendu: {scenario['expected_pattern']}")
            
            result = await self.process_request(scenario["input"])
            
            actual_pattern = result.get("orchestrator", {}).get("selected_pattern", "unknown")
            pattern_match = actual_pattern == scenario["expected_pattern"]
            
            print(f"🤖 Pattern utilisé: {actual_pattern}")
            print(f"✅ Correspondance: {'Oui' if pattern_match else 'Non'}")
            
            # Afficher la réponse selon le pattern
            if actual_pattern == "single":
                print(f"💬 Réponse: {result.get('response', 'N/A')[:100]}...")
            elif actual_pattern == "tool":
                tools_used = result.get('tools_used', [])
                print(f"🔧 Outils: {', '.join(tools_used) if tools_used else 'Aucun'}")
                print(f"💬 Synthèse: {result.get('synthesis', 'N/A')[:100]}...")
            elif actual_pattern == "human_loop":
                validation = result.get('validation_required', False)
                approved = result.get('approved', False)
                print(f"👤 Validation: {'Requise' if validation else 'Non requise'}")
                print(f"✅ Approuvé: {'Oui' if approved else 'Non'}")
                print(f"💬 Réponse: {result.get('final_response', 'N/A')[:100]}...")
            
            results.append({
                "scenario": scenario,
                "result": result,
                "pattern_match": pattern_match
            })
        
        # Statistiques finales
        print(f"\n📊 STATISTIQUES FINALES")
        print("=" * 60)
        
        stats = self.get_stats()
        print(f"📈 Total requêtes: {stats['total_requests']}")
        print(f"🎯 Pattern le plus utilisé: {stats['most_used_pattern']}")
        print(f"📊 Distribution des patterns:")
        for pattern, percentage in stats['pattern_distribution'].items():
            print(f"   • {pattern}: {percentage:.1f}%")
        
        pattern_accuracy = sum(1 for r in results if r["pattern_match"]) / len(results) * 100
        print(f"🎯 Précision sélection pattern: {pattern_accuracy:.1f}%")
        
        success_rate = sum(1 for r in results if r["result"].get("success", True)) / len(results) * 100
        print(f"✅ Taux de succès global: {success_rate:.1f}%")
        
        return {
            "demo_results": results,
            "final_stats": stats,
            "pattern_accuracy": pattern_accuracy,
            "success_rate": success_rate
        }

# Point d'entrée principal
async def main():
    """Fonction principale pour tester l'agent"""
    print("🎯 Démarrage de votre Premier Agent IA")
    print("🎓 Module 1: Fondamentaux des Agents IA")
    print()
    
    # Créer l'agent principal
    agent = MyFirstAgent()
    
    # Lancer la démonstration complète
    demo_results = await agent.run_complete_demo()
    
    # Sauvegarde des résultats
    results_file = f"agent_demo_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(demo_results, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\n💾 Résultats sauvegardés: {results_file}")
    
    return demo_results

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### ✅ TODO 8: Test et Validation (5 min)

**Concepts appris**: Validation et métriques de performance

Ajoutez le système de tests:

```python
def validate_agent_capabilities(agent: MyFirstAgent) -> Dict[str, Any]:
    """Valider les capacités de l'agent selon les critères du module"""
    validation_results = {
        "agentic_loop": False,
        "llm_integration": False,
        "tool_usage": False,
        "memory_system": False,
        "pattern_implementation": {"single": False, "tool": False, "human_loop": False},
        "orchestration": False,
        "error_handling": False,
        "overall_score": 0.0
    }
    
    # Test de la boucle agentique
    try:
        test_input = "Test de validation"
        perception = agent.single_agent.perceive(test_input)
        plan = agent.single_agent.plan(perception)
        
        if all(key in perception for key in ["user_input", "intent", "context"]):
            validation_results["agentic_loop"] = True
        if len(plan) > 0 and all("action" in step for step in plan):
            validation_results["agentic_loop"] = True
    except:
        pass
    
    # Test d'intégration LLM
    try:
        if agent.single_agent.client is not None:
            validation_results["llm_integration"] = True
    except:
        pass
    
    # Test des outils
    try:
        tools = agent.tool_agent.tool_registry.list_tools()
        if len(tools) >= 3:  # Minimum 3 outils
            validation_results["tool_usage"] = True
    except:
        pass
    
    # Test de la mémoire
    try:
        if hasattr(agent.single_agent.state, "conversation_history"):
            validation_results["memory_system"] = True
    except:
        pass
    
    # Test des patterns
    validation_results["pattern_implementation"]["single"] = hasattr(agent, "single_agent")
    validation_results["pattern_implementation"]["tool"] = hasattr(agent, "tool_agent")
    validation_results["pattern_implementation"]["human_loop"] = hasattr(agent, "human_loop_agent")
    
    # Test d'orchestration
    try:
        if hasattr(agent, "_select_optimal_pattern") and hasattr(agent, "global_state"):
            validation_results["orchestration"] = True
    except:
        pass
    
    # Test de gestion d'erreurs
    try:
        # Tester avec input invalide
        import asyncio
        result = asyncio.run(agent.process_request(""))
        if "error" in result or result.get("success") is not None:
            validation_results["error_handling"] = True
    except:
        validation_results["error_handling"] = True  # Exception capturée = bonne gestion
    
    # Calculer le score global
    total_checks = 0
    passed_checks = 0
    
    for key, value in validation_results.items():
        if key == "pattern_implementation":
            for pattern_key, pattern_value in value.items():
                total_checks += 1
                if pattern_value:
                    passed_checks += 1
        elif key != "overall_score":
            total_checks += 1
            if value:
                passed_checks += 1
    
    validation_results["overall_score"] = (passed_checks / total_checks) * 100
    
    return validation_results

# Ajouter à la fin du main()
def print_validation_report(validation_results: Dict[str, Any]):
    """Afficher le rapport de validation"""
    print(f"\n📋 RAPPORT DE VALIDATION")
    print("=" * 60)
    
    print(f"🔄 Boucle agentique: {'✅' if validation_results['agentic_loop'] else '❌'}")
    print(f"🤖 Intégration LLM: {'✅' if validation_results['llm_integration'] else '❌'}")
    print(f"🔧 Système d'outils: {'✅' if validation_results['tool_usage'] else '❌'}")
    print(f"💾 Système mémoire: {'✅' if validation_results['memory_system'] else '❌'}")
    print(f"🎯 Orchestration: {'✅' if validation_results['orchestration'] else '❌'}")
    print(f"⚠️ Gestion d'erreurs: {'✅' if validation_results['error_handling'] else '❌'}")
    
    print(f"\n📊 Patterns implémentés:")
    for pattern, implemented in validation_results['pattern_implementation'].items():
        print(f"   • {pattern}: {'✅' if implemented else '❌'}")
    
    score = validation_results['overall_score']
    if score >= 90:
        grade = "🏆 Excellent"
    elif score >= 75:
        grade = "🥇 Très bien"
    elif score >= 60:
        grade = "🥈 Bien"
    else:
        grade = "🥉 À améliorer"
    
    print(f"\n🎯 Score global: {score:.1f}% - {grade}")
    
    if score < 100:
        print(f"\n💡 Points d'amélioration:")
        if not validation_results['agentic_loop']:
            print("   • Implémenter la boucle Perception → Plan → Act → Reflect")
        if not validation_results['llm_integration']:
            print("   • Configurer correctement l'intégration OpenAI")
        if not validation_results['tool_usage']:
            print("   • Ajouter au moins 3 outils fonctionnels")
        if not validation_results['memory_system']:
            print("   • Implémenter la persistance des conversations")
```

## 🎯 Résultat Final

Après avoir complété tous les TODOs, vous aurez créé :

### 📁 Fichiers Générés
- ✅ `my_first_agent_starter.py` - Votre agent complet avec 3 patterns
- ✅ `agent_demo_results_*.json` - Résultats des tests automatiques
- ✅ Historique des conversations en mémoire

### 🎓 Compétences Acquises
- **Boucle Agentique**: Perception → Plan → Act → Reflect
- **Patterns de Base**: Single Agent, Tool Use, Human-in-Loop
- **Orchestration**: Sélection intelligente de patterns
- **Intégration**: LLM + Tools + Memory = Agent

### 🚀 Applications Possibles
- Assistant personnel intelligent
- Agent de support client basique
- Système de validation avec contrôle humain
- Prototype d'agent métier simple

## 🎬 Démonstration

Lancez votre agent terminé :

```bash
python my_first_agent_starter.py
```

Le système exécutera automatiquement :
1. ✅ Test des 3 patterns fondamentaux
2. ✅ Démonstration de l'orchestration intelligente
3. ✅ Validation automatique des capacités
4. ✅ Génération de rapport de performance
5. ✅ Sauvegarde des résultats

## 🔧 Personnalisation

### Adapter à Votre Domaine
1. **Outils**: Ajoutez des outils spécifiques à votre métier
2. **Patterns**: Personnalisez les seuils de validation
3. **LLM**: Configurez les prompts selon votre contexte
4. **Mémoire**: Adaptez les préférences utilisateur

### Extensions Possibles
1. **Persistance**: Base de données pour mémoire long-terme
2. **Interface**: Web UI ou chat pour interaction
3. **Monitoring**: Métriques avancées et logs
4. **Sécurité**: Authentification et autorisation

## 🏆 Validation des Acquis

Vous maîtrisez le module si vous pouvez :
- [ ] Expliquer la boucle agentique et ses 4 étapes
- [ ] Implémenter les 3 patterns de base de zéro
- [ ] Orchestrer plusieurs patterns selon le contexte
- [ ] Intégrer LLM, outils et mémoire dans un agent cohérent
- [ ] Identifier quand utiliser chaque pattern

## 🔗 Ressources pour Aller Plus Loin

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Documentation](https://docs.langchain.com/) (préparation Module 2)

---

🎯 **Félicitations !** Vous avez maîtrisé les fondamentaux et êtes prêt pour les patterns avancés !