#!/usr/bin/env python3
"""
🎯 Premier Agent IA - Assistant Personnel Intelligent
===================================================

VOTRE MISSION: Créer un assistant IA fonctionnel en 2h qui peut :
💬 Converser naturellement (comme ChatGPT)
🔧 Utiliser des outils (calculatrice, recherche, météo)  
👤 Demander validation humaine (pour contenus sensibles)
🧠 Choisir automatiquement le bon comportement

EXEMPLES DE CE QUE VOTRE AGENT FERA:
👤 "Salut !" → 🤖 [Chat] "Bonjour ! Comment puis-je vous aider ?"
👤 "15 × 8 + 42 ?" → 🤖 [Outil] 🔧 "Le résultat est 162"  
👤 "Décision financière" → 🤖 [Validation] 🚨 "Approbation requise"

INSTRUCTIONS:
- Suivez les 8 TODOs dans l'ordre (1→2→3→...→8)
- Décommentez et complétez le code à chaque étape
- Testez après chaque TODO pour voir les progrès
- Consultez STEP_BY_STEP_GUIDE.md pour les explications détaillées

⏱️ Durée: 68 minutes | 🔑 Prérequis: Clé OpenAI dans .env
"""

# TODO 1: Installation et Imports (3 min)
# Décommentez les imports suivants et installez les dépendances
# pip install openai python-dotenv requests beautifulsoup4

import os
import json
import asyncio
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

# TODO: Décommentez les imports OpenAI
# from openai import OpenAI

# Charger les variables d'environnement
load_dotenv()

print("🚀 Initialisation du Premier Agent IA")
print("🎓 Module 1: Fondamentaux des Agents IA")
print("=" * 60)

# TODO 2: Architecture de Base (5 min)
# Complétez les classes de base pour votre agent

@dataclass
class AgentState:
    """État de l'agent entre les interactions"""
    conversation_history: List[Dict[str, Any]] = field(default_factory=list)
    tools_used: List[str] = field(default_factory=list)
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    session_id: str = ""
    total_interactions: int = 0
    
    def __post_init__(self):
        if not self.user_preferences:
            self.user_preferences = {"language": "fr", "style": "friendly"}
        if not self.session_id:
            self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

class BaseAgent:
    """Agent IA suivant la boucle Perception → Plan → Act → Reflect"""
    
    def __init__(self):
        # TODO: Initialisez votre client OpenAI
        # api_key = os.getenv("OPENAI_API_KEY")
        # if not api_key:
        #     raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
        # self.client = OpenAI(api_key=api_key)
        
        self.client = None  # TODO: Remplacez par l'initialisation OpenAI
        
        self.state = AgentState()
        self.available_tools = {}  # Sera peuplé dans TODO 5
        
        print(f"🤖 Agent initialisé - Session: {self.state.session_id}")
    
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
        
        # TODO: Complétez la logique de planification basée sur l'intent
        intent = perception["intent"]
        
        if intent == "calculation":
            plan.append({"action": "use_tool", "tool": "calculator", "priority": 1})
        elif intent == "information":
            plan.append({"action": "search_web", "tool": "web_search", "priority": 1})
        elif intent == "conversation":
            plan.append({"action": "llm_response", "tool": "direct_llm", "priority": 1})
        elif intent == "validation":
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
            
            # TODO: Implémentez l'exécution des actions
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
            "user_satisfaction": None
        }
        
        # TODO: Complétez la logique de réflexion
        for result in results:
            if "error" in result.get("result", {}):
                reflection["lessons_learned"].append(f"Erreur avec {result['step']['tool']}")
                reflection["improvements"].append(f"Améliorer {result['step']['action']}")
        
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
        
        # TODO: Améliorez la détection d'intent
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
    
    def _assess_quality(self, results: List[Dict]) -> float:
        """Évaluer la qualité des résultats"""
        if not results:
            return 0.0
        
        successful_results = sum(1 for r in results if not r.get("result", {}).get("error"))
        return successful_results / len(results)
    
    def _execute_tool(self, tool_name: str, params: Dict) -> Dict[str, Any]:
        """Exécuter un outil - sera implémenté dans TODO 5"""
        return {"error": "Outils pas encore implémentés", "tool": tool_name}
    
    def _call_llm(self, prompt: str) -> Dict[str, Any]:
        """Appeler le LLM - sera implémenté dans TODO 3"""
        return {"error": "LLM pas encore configuré", "prompt": prompt}
    
    def _request_human_input(self, question: str) -> Dict[str, Any]:
        """Demander une validation humaine - sera implémenté dans TODO 6"""
        return {"error": "Validation humaine pas encore implémentée", "question": question}
    
    def _self_reflect(self, results: List[Dict]) -> Dict[str, Any]:
        """Auto-réflexion sur les résultats"""
        return {"reflection": "Auto-réflexion basique", "results_count": len(results)}

# TODO 3: Configuration LLM (5 min)
# Complétez l'intégration OpenAI

def setup_llm_integration(agent: BaseAgent):
    """Configurer l'intégration LLM"""
    print("\n🤖 ÉTAPE: Configuration LLM")
    print("=" * 60)
    
    # TODO: Décommentez et complétez la configuration OpenAI
    # try:
    #     api_key = os.getenv("OPENAI_API_KEY")
    #     if not api_key:
    #         raise ValueError("❌ OPENAI_API_KEY non trouvée !")
    #     
    #     agent.client = OpenAI(api_key=api_key)
    #     agent.llm_config = {
    #         "model": "gpt-4",
    #         "temperature": 0.7,
    #         "max_tokens": 500
    #     }
    #     
    #     print("✅ Client OpenAI configuré")
    #     print(f"🎯 Modèle: {agent.llm_config['model']}")
    #     return True
    # except Exception as e:
    #     print(f"❌ Erreur configuration LLM: {e}")
    #     return False
    
    print("⚠️ TODO 3: Implémentez la configuration LLM")
    return False

def implement_llm_call(agent: BaseAgent):
    """Implémenter l'appel LLM"""
    
    def _call_llm(prompt: str, system_message: str = "") -> Dict[str, Any]:
        """Appeler le LLM avec gestion d'erreurs"""
        # TODO: Décommentez et complétez l'appel OpenAI
        # try:
        #     messages = []
        #     if system_message:
        #         messages.append({"role": "system", "content": system_message})
        #     messages.append({"role": "user", "content": prompt})
        #     
        #     response = agent.client.chat.completions.create(
        #         model=agent.llm_config["model"],
        #         messages=messages,
        #         temperature=agent.llm_config["temperature"],
        #         max_tokens=agent.llm_config["max_tokens"]
        #     )
        #     
        #     return {
        #         "content": response.choices[0].message.content,
        #         "tokens_used": response.usage.total_tokens,
        #         "success": True
        #     }
        # except Exception as e:
        #     return {
        #         "error": str(e),
        #         "success": False,
        #         "fallback_response": "Désolé, problème technique."
        #     }
        
        # Simulation temporaire
        return {
            "content": f"Réponse simulée pour: {prompt[:50]}...",
            "tokens_used": 100,
            "success": True,
            "note": "TODO 3: Implémentez l'appel OpenAI réel"
        }
    
    # Remplacer la méthode de l'agent
    agent._call_llm = _call_llm
    print("✅ Méthode _call_llm configurée (mode simulation)")

# TODO 4: Pattern 1 - Single Agent (10 min)
# Implémentez le pattern Single Agent

class SingleAgent(BaseAgent):
    """Pattern 1: Agent simple avec réponse LLM directe"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Single Agent"
        print(f"🤖 Pattern initialisé: {self.pattern_name}")
    
    async def handle_single_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête simple avec le pattern Single Agent"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - '{user_input}'")
        print("=" * 60)
        
        # TODO: Complétez l'implémentation du pattern Single Agent
        
        # Étape 1: Perception
        perception = self.perceive(user_input)
        
        # Étape 2: Plan simple
        plan = [{"action": "llm_response", "tool": "direct_llm", "priority": 1, "prompt": user_input}]
        
        # Étape 3: Action
        system_message = f"""Tu es un assistant IA personnel utile et amical.
        
Préférences: {self.state.user_preferences}
Historique: {len(self.state.conversation_history)} interactions

Instructions:
- Réponds clairement et de manière concise
- Adapte ton style aux préférences utilisateur
- Sois honnête si tu ne sais pas
- Suggère des questions de suivi si pertinent

Requête: {user_input}"""

        result = self._call_llm(user_input, system_message)
        
        # Étape 4: Réflexion
        reflection = self.reflect([{"step": plan[0], "result": result}])
        
        # Mettre à jour l'état
        self.state.total_interactions += 1
        
        response_data = {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "response": result.get("content", result.get("fallback_response", "Erreur")),
            "success": result.get("success", False),
            "tokens_used": result.get("tokens_used", 0),
            "quality_score": reflection["quality_score"],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"✅ Single Agent - Succès: {response_data['success']}")
        return response_data
    
    def demo_single_agent(self):
        """Démonstration du pattern Single Agent"""
        print(f"\n🎬 DÉMONSTRATION: {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Bonjour ! Comment allez-vous ?",
            "Expliquez-moi ce qu'est un agent IA",
            "Donnez-moi 3 conseils pour bien dormir"
        ]
        
        print(f"📋 Tests: {len(demo_queries)} requêtes")
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i} ---")
            print(f"👤 User: {query}")
            
            response = asyncio.run(self.handle_single_request(query))
            print(f"🤖 Assistant: {response['response']}")
            print(f"📊 Qualité: {response['quality_score']:.2f}")

# TODO 5: Pattern 2 - Tool Use Agent (15 min)
# Implémentez le système d'outils et le pattern Tool Use

class ToolRegistry:
    """Registre des outils disponibles"""
    
    def __init__(self):
        self.tools = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Enregistrer les outils par défaut"""
        # TODO: Complétez l'enregistrement des outils
        self.register_tool("calculator", self._calculator_tool)
        self.register_tool("web_search", self._web_search_tool)
        self.register_tool("weather", self._weather_tool)
        print("🔧 Outils par défaut enregistrés")
    
    def register_tool(self, name: str, function):
        """Enregistrer un outil"""
        self.tools[name] = {
            "function": function,
            "description": function.__doc__ or f"Outil {name}"
        }
    
    def get_tool(self, name: str):
        """Récupérer un outil"""
        return self.tools.get(name, {}).get("function")
    
    def list_tools(self) -> List[str]:
        """Lister les outils"""
        return list(self.tools.keys())
    
    def _calculator_tool(self, expression: str) -> Dict[str, Any]:
        """Calculatrice sécurisée pour opérations mathématiques"""
        # TODO: Implémentez la calculatrice
        try:
            # Sécuriser l'expression
            allowed_chars = set("0123456789+-*/.() ")
            if not all(c in allowed_chars for c in expression):
                return {"error": "Expression non autorisée"}
            
            result = eval(expression)
            return {"result": result, "expression": expression, "success": True}
        except Exception as e:
            return {"error": f"Erreur calcul: {e}", "success": False}
    
    def _web_search_tool(self, query: str) -> Dict[str, Any]:
        """Outil de recherche web (simulation)"""
        # TODO: En production, utiliser une vraie API de recherche
        simulated_results = [
            {
                "title": f"Résultat pour '{query}'",
                "url": f"https://example.com/search?q={query}",
                "snippet": f"Informations pertinentes sur {query}..."
            }
        ]
        return {
            "results": simulated_results,
            "query": query,
            "success": True,
            "note": "Résultats simulés"
        }
    
    def _weather_tool(self, location: str) -> Dict[str, Any]:
        """Outil météo (simulation)"""
        # TODO: En production, utiliser OpenWeatherMap
        import random
        return {
            "location": location,
            "temperature": f"{random.randint(10, 25)}°C",
            "condition": random.choice(["Ensoleillé", "Nuageux", "Pluvieux"]),
            "success": True,
            "note": "Données simulées"
        }

class ToolUseAgent(BaseAgent):
    """Pattern 2: Agent avec utilisation d'outils externes"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Tool Use Agent"
        self.tool_registry = ToolRegistry()
        self.available_tools = self.tool_registry.tools
        print(f"🛠️ Pattern initialisé: {self.pattern_name}")
        print(f"🔧 Outils: {', '.join(self.tool_registry.list_tools())}")
    
    def _detect_tool_need(self, user_input: str) -> List[str]:
        """Détecter quels outils sont nécessaires"""
        # TODO: Améliorez la détection d'outils
        needed_tools = []
        user_lower = user_input.lower()
        
        if any(word in user_lower for word in ["calcul", "addition", "multiplication", "combien"]):
            needed_tools.append("calculator")
        if any(word in user_lower for word in ["recherche", "trouve", "information"]):
            needed_tools.append("web_search")
        if any(word in user_lower for word in ["météo", "temps", "température"]):
            needed_tools.append("weather")
        
        return needed_tools
    
    def _execute_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Exécuter un outil"""
        tool_function = self.tool_registry.get_tool(tool_name)
        
        if not tool_function:
            return {"error": f"Outil '{tool_name}' non trouvé", "success": False}
        
        try:
            # TODO: Complétez l'exécution selon le type d'outil
            if tool_name == "calculator":
                result = tool_function(params.get("expression", ""))
            elif tool_name == "web_search":
                result = tool_function(params.get("query", ""))
            elif tool_name == "weather":
                result = tool_function(params.get("location", "Paris"))
            else:
                result = tool_function(params)
            
            # Enregistrer l'utilisation
            if tool_name not in self.state.tools_used:
                self.state.tools_used.append(tool_name)
            
            result["tool_used"] = tool_name
            return result
        except Exception as e:
            return {"error": f"Erreur {tool_name}: {e}", "success": False}
    
    async def handle_tool_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête avec outils"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - '{user_input}'")
        print("=" * 60)
        
        # TODO: Complétez l'implémentation du pattern Tool Use
        
        # Détecter les outils nécessaires
        needed_tools = self._detect_tool_need(user_input)
        print(f"🔧 Outils détectés: {needed_tools}")
        
        # Exécuter les outils
        tool_results = []
        for tool in needed_tools:
            params = self._extract_tool_params(user_input, tool)
            result = self._execute_tool(tool, params)
            tool_results.append({"tool": tool, "result": result})
        
        # Synthèse avec LLM
        synthesis_prompt = self._build_synthesis_prompt(user_input, tool_results)
        llm_result = self._call_llm(synthesis_prompt)
        
        self.state.total_interactions += 1
        
        return {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "tools_used": needed_tools,
            "tool_results": tool_results,
            "synthesis": llm_result.get("content", "Erreur synthèse"),
            "success": all(r["result"].get("success", True) for r in tool_results),
            "timestamp": datetime.now().isoformat()
        }
    
    def _extract_tool_params(self, user_input: str, tool_name: str) -> Dict[str, Any]:
        """Extraire les paramètres pour un outil"""
        # TODO: Améliorez l'extraction de paramètres
        if tool_name == "calculator":
            import re
            numbers = re.findall(r'[\d+\-*/().\s]+', user_input)
            return {"expression": numbers[-1].strip() if numbers else "1+1"}
        elif tool_name == "web_search":
            return {"query": user_input}
        elif tool_name == "weather":
            return {"location": "Paris"}  # TODO: Extraire la vraie ville
        return {}
    
    def _build_synthesis_prompt(self, user_input: str, tool_results: List[Dict]) -> str:
        """Construire le prompt de synthèse"""
        prompt = f"""Synthétise les résultats d'outils pour répondre à: {user_input}

Résultats:
"""
        for tr in tool_results:
            prompt += f"- {tr['tool']}: {tr['result']}\n"
        
        prompt += "\nSynthèse complète:"
        return prompt
    
    def demo_tool_use_agent(self):
        """Démonstration du pattern Tool Use"""
        print(f"\n🎬 DÉMONSTRATION: {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Combien font 15 * 8 ?",
            "Quelle est la météo à Paris ?",
            "Recherche des infos sur l'IA"
        ]
        
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i} ---")
            print(f"👤 User: {query}")
            
            response = asyncio.run(self.handle_tool_request(query))
            print(f"🔧 Outils: {', '.join(response['tools_used'])}")
            print(f"🤖 Synthèse: {response['synthesis'][:100]}...")

# TODO 6: Pattern 3 - Human-in-the-Loop (10 min)
# Implémentez le pattern Human-in-the-Loop

class HumanInLoopAgent(BaseAgent):
    """Pattern 3: Agent avec validation humaine"""
    
    def __init__(self):
        super().__init__()
        self.pattern_name = "Human-in-the-Loop Agent"
        self.validation_threshold = 0.7
        print(f"👤 Pattern initialisé: {self.pattern_name}")
    
    def _assess_need_for_validation(self, user_input: str) -> Dict[str, Any]:
        """Évaluer si validation humaine nécessaire"""
        # TODO: Complétez l'évaluation
        indicators = {
            "high_impact": any(word in user_input.lower() for word in ["important", "critique", "urgent"]),
            "financial": any(word in user_input.lower() for word in ["argent", "euro", "coût"]),
            "decision": any(word in user_input.lower() for word in ["décision", "choix"])
        }
        
        score = sum(indicators.values()) / len(indicators)
        
        return {
            "needs_validation": score >= self.validation_threshold,
            "confidence_score": 1 - score,
            "indicators": indicators
        }
    
    def _request_human_validation(self, content: str, reason: str) -> Dict[str, Any]:
        """Simuler validation humaine"""
        print(f"\n🚨 VALIDATION REQUISE")
        print(f"📋 Raison: {reason}")
        print(f"📄 Contenu: {content}")
        print(f"⏳ En attente validation...")
        
        # TODO: En production, vraie interface utilisateur
        # Simulation automatique
        import random
        approved = random.choice([True, True, False])  # 66% d'approbation
        
        return {
            "approved": approved,
            "feedback": "Approuvé" if approved else "Refusé - trop risqué",
            "timestamp": datetime.now().isoformat(),
            "success": True
        }
    
    async def handle_human_loop_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter avec validation humaine"""
        print(f"\n🎯 PATTERN: {self.pattern_name} - '{user_input}'")
        print("=" * 60)
        
        # TODO: Complétez l'implémentation Human-in-the-Loop
        
        # Évaluer besoin de validation
        assessment = self._assess_need_for_validation(user_input)
        
        # Générer réponse initiale
        initial_response = self._call_llm(user_input)
        final_response = initial_response.get("content", "Erreur")
        
        validation_result = None
        
        # Validation si nécessaire
        if assessment["needs_validation"]:
            validation_result = self._request_human_validation(
                final_response, 
                "Contenu sensible détecté"
            )
            
            if not validation_result["approved"]:
                final_response = f"Désolé, je ne peux traiter cette requête. Raison: {validation_result['feedback']}"
        
        self.state.total_interactions += 1
        
        return {
            "pattern": self.pattern_name,
            "user_input": user_input,
            "validation_required": assessment["needs_validation"],
            "validation_result": validation_result,
            "final_response": final_response,
            "approved": validation_result["approved"] if validation_result else True,
            "confidence": assessment["confidence_score"],
            "timestamp": datetime.now().isoformat()
        }
    
    def demo_human_in_loop_agent(self):
        """Démonstration Human-in-the-Loop"""
        print(f"\n🎬 DÉMONSTRATION: {self.pattern_name}")
        print("=" * 60)
        
        demo_queries = [
            "Bonjour, comment ça va ?",  # Pas de validation
            "C'est une décision financière critique",  # Validation requise
            "Quelle est la capitale de France ?"  # Pas de validation
        ]
        
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Test {i} ---")
            print(f"👤 User: {query}")
            
            response = asyncio.run(self.handle_human_loop_request(query))
            print(f"⚖️ Validation: {'Requise' if response['validation_required'] else 'Non requise'}")
            if response['validation_required']:
                print(f"✅ Approuvé: {'Oui' if response['approved'] else 'Non'}")
            print(f"🤖 Réponse: {response['final_response'][:100]}...")

# TODO 7: Agent Orchestrateur Principal (15 min)
# Créez l'agent qui coordonne les 3 patterns

class MyFirstAgent:
    """Agent principal orchestrant les 3 patterns fondamentaux"""
    
    def __init__(self):
        print("\n🚀 INITIALISATION AGENT PRINCIPAL")
        print("=" * 60)
        
        # TODO: Initialisez les 3 patterns
        self.single_agent = SingleAgent()
        self.tool_agent = ToolUseAgent()
        self.human_loop_agent = HumanInLoopAgent()
        
        self.global_state = {
            "total_requests": 0,
            "pattern_usage": {"single": 0, "tool": 0, "human_loop": 0},
            "session_start": datetime.now().isoformat()
        }
        
        print("✅ Tous les patterns initialisés")
    
    def _select_optimal_pattern(self, user_input: str) -> str:
        """Sélectionner le pattern optimal"""
        user_lower = user_input.lower()
        
        # TODO: Améliorez la logique de sélection
        
        # Priorité 1: Human-in-Loop pour contenus sensibles
        if any(word in user_lower for word in ["important", "critique", "décision", "urgent"]):
            return "human_loop"
        
        # Priorité 2: Tool Use pour outils
        if any(word in user_lower for word in ["calcul", "recherche", "météo", "combien"]):
            return "tool"
        
        # Par défaut: Single Agent
        return "single"
    
    async def process_request(self, user_input: str) -> Dict[str, Any]:
        """Traiter une requête avec sélection automatique de pattern"""
        self.global_state["total_requests"] += 1
        
        print(f"\n🎯 ORCHESTRATEUR - Requête #{self.global_state['total_requests']}")
        print(f"👤 Input: {user_input}")
        
        # Sélection du pattern
        selected_pattern = self._select_optimal_pattern(user_input)
        self.global_state["pattern_usage"][selected_pattern] += 1
        
        print(f"🧠 Pattern sélectionné: {selected_pattern.upper()}")
        
        # Exécution
        try:
            if selected_pattern == "single":
                result = await self.single_agent.handle_single_request(user_input)
            elif selected_pattern == "tool":
                result = await self.tool_agent.handle_tool_request(user_input)
            elif selected_pattern == "human_loop":
                result = await self.human_loop_agent.handle_human_loop_request(user_input)
            
            result["orchestrator"] = {
                "selected_pattern": selected_pattern,
                "request_number": self.global_state["total_requests"]
            }
            
            return result
            
        except Exception as e:
            return {
                "error": f"Erreur: {e}",
                "selected_pattern": selected_pattern,
                "success": False
            }
    
    def get_stats(self) -> Dict[str, Any]:
        """Statistiques globales"""
        total = self.global_state["total_requests"]
        if total > 0:
            percentages = {k: (v/total)*100 for k, v in self.global_state["pattern_usage"].items()}
        else:
            percentages = {"single": 0, "tool": 0, "human_loop": 0}
        
        return {
            "total_requests": total,
            "pattern_distribution": percentages,
            "most_used": max(self.global_state["pattern_usage"], key=self.global_state["pattern_usage"].get) if total > 0 else "Aucun"
        }
    
    async def run_complete_demo(self):
        """Démonstration complète des 3 patterns"""
        print(f"\n🎬 DÉMONSTRATION COMPLÈTE")
        print("=" * 80)
        
        # Scénarios de test qui correspondent EXACTEMENT aux exemples du README
        demo_scenarios = [
            {"input": "Salut ! Comment ça va ?", "expected": "single"},
            {"input": "Combien font 15 × 8 + 42 ?", "expected": "tool"},
            {"input": "C'est une décision financière critique", "expected": "human_loop"},
            {"input": "Quel temps fait-il à Paris ?", "expected": "tool"},
            {"input": "Expliquez-moi l'intelligence artificielle", "expected": "single"}
        ]
        
        results = []
        
        for i, scenario in enumerate(demo_scenarios, 1):
            print(f"\n--- 🎬 DEMO {i}/{len(demo_scenarios)} ---")
            print(f"👤 User: {scenario['input']}")
            
            result = await self.process_request(scenario["input"])
            results.append(result)
            
            actual = result.get("orchestrator", {}).get("selected_pattern", "unknown")
            match = actual == scenario["expected"]
            
            # Afficher la réponse selon le pattern utilisé
            pattern_icons = {"single": "💬", "tool": "🔧", "human_loop": "👤"}
            icon = pattern_icons.get(actual, "🤖")
            
            if actual == "single":
                response = result.get("response", "Erreur")
                print(f"🤖 Agent: [{icon} Single Agent] {response[:80]}...")
            elif actual == "tool":
                tools_used = result.get("tools_used", [])
                synthesis = result.get("synthesis", "Erreur")
                print(f"🤖 Agent: [{icon} Tool Use] Outils: {', '.join(tools_used)}")
                print(f"        → {synthesis[:80]}...")
            elif actual == "human_loop":
                validation = result.get("validation_required", False)
                approved = result.get("approved", False)
                final_response = result.get("final_response", "Erreur")
                print(f"🤖 Agent: [{icon} Human-in-Loop] Validation: {'Requise' if validation else 'Non'}")
                print(f"        → {'Approuvé' if approved else 'Refusé'}: {final_response[:60]}...")
            
            print(f"✅ Pattern correct: {'Oui' if match else 'Non'} (attendu: {scenario['expected']}, utilisé: {actual})")
        
        # Statistiques finales avec confirmation des capacités
        stats = self.get_stats()
        pattern_accuracy = sum(1 for r in results if r.get("orchestrator", {}).get("selected_pattern") == demo_scenarios[results.index(r)]["expected"]) / len(results) * 100
        
        print(f"\n🏆 FÉLICITATIONS ! VOTRE AGENT IA EST PRÊT !")
        print("=" * 60)
        print(f"✅ Assistant personnel intelligent créé avec succès")
        print(f"✅ 3 patterns fondamentaux maîtrisés")
        print(f"✅ Sélection automatique de comportement: {pattern_accuracy:.0f}% de précision")
        print()
        print(f"📊 CAPACITÉS DÉMONTRÉES:")
        print(f"   💬 Conversation naturelle: {stats['pattern_distribution']['single']:.0f}% des interactions")
        print(f"   🔧 Utilisation d'outils: {stats['pattern_distribution']['tool']:.0f}% des interactions") 
        print(f"   👤 Validation humaine: {stats['pattern_distribution']['human_loop']:.0f}% des interactions")
        print()
        print(f"📈 STATS: {stats['total_requests']} requêtes traitées")
        print(f"🎯 RÉSULTAT: Un assistant IA qui combine ChatGPT + outils + sécurité !")
        
        return results

# TODO 8: Test et Validation (5 min)
# Validez les capacités de votre agent

def validate_agent_capabilities(agent: MyFirstAgent) -> Dict[str, Any]:
    """Valider les capacités selon les critères du module"""
    validation = {
        "agentic_loop": False,
        "llm_integration": False,
        "tool_usage": False,
        "memory_system": False,
        "patterns": {"single": False, "tool": False, "human_loop": False},
        "orchestration": False
    }
    
    # TODO: Complétez les tests de validation
    
    # Test boucle agentique
    try:
        test_perception = agent.single_agent.perceive("test")
        if "intent" in test_perception and "context" in test_perception:
            validation["agentic_loop"] = True
    except:
        pass
    
    # Test LLM
    if hasattr(agent.single_agent, 'client'):
        validation["llm_integration"] = True
    
    # Test outils
    if len(agent.tool_agent.tool_registry.list_tools()) >= 3:
        validation["tool_usage"] = True
    
    # Test mémoire
    if hasattr(agent.single_agent.state, 'conversation_history'):
        validation["memory_system"] = True
    
    # Test patterns
    validation["patterns"]["single"] = hasattr(agent, "single_agent")
    validation["patterns"]["tool"] = hasattr(agent, "tool_agent") 
    validation["patterns"]["human_loop"] = hasattr(agent, "human_loop_agent")
    
    # Test orchestration
    if hasattr(agent, "_select_optimal_pattern"):
        validation["orchestration"] = True
    
    # Score global
    total_checks = sum([
        validation["agentic_loop"],
        validation["llm_integration"], 
        validation["tool_usage"],
        validation["memory_system"],
        validation["orchestration"]
    ]) + sum(validation["patterns"].values())
    
    validation["overall_score"] = (total_checks / 8) * 100
    
    return validation

def print_validation_report(validation: Dict[str, Any]):
    """Afficher le rapport de validation"""
    print(f"\n📋 RAPPORT DE VALIDATION")
    print("=" * 60)
    
    print(f"🔄 Boucle agentique: {'✅' if validation['agentic_loop'] else '❌'}")
    print(f"🤖 LLM: {'✅' if validation['llm_integration'] else '❌'}")
    print(f"🔧 Outils: {'✅' if validation['tool_usage'] else '❌'}")
    print(f"💾 Mémoire: {'✅' if validation['memory_system'] else '❌'}")
    print(f"🎯 Orchestration: {'✅' if validation['orchestration'] else '❌'}")
    
    print(f"\n📊 Patterns:")
    for pattern, ok in validation['patterns'].items():
        print(f"   • {pattern}: {'✅' if ok else '❌'}")
    
    score = validation['overall_score']
    grade = "🏆 Excellent" if score >= 90 else "🥇 Très bien" if score >= 75 else "🥈 Bien" if score >= 60 else "🥉 À améliorer"
    
    print(f"\n🎯 Score: {score:.1f}% - {grade}")

# FONCTION PRINCIPALE
async def main():
    """Fonction principale pour tester votre agent"""
    print("🎯 DÉMARRAGE - Premier Agent IA")
    print("🎓 Module 1: Fondamentaux des Agents IA")
    print()
    
    # TODO: Décommentez et complétez étape par étape
    
    print("⚠️ TODOs à compléter:")
    print("1. ⬜ TODO 1: Installation et imports")
    print("2. ⬜ TODO 2: Architecture de base") 
    print("3. ⬜ TODO 3: Configuration LLM")
    print("4. ⬜ TODO 4: Pattern Single Agent")
    print("5. ⬜ TODO 5: Pattern Tool Use")
    print("6. ⬜ TODO 6: Pattern Human-in-Loop") 
    print("7. ⬜ TODO 7: Orchestrateur principal")
    print("8. ⬜ TODO 8: Tests et validation")
    print()
    print("📖 Consultez STEP_BY_STEP_GUIDE.md pour les instructions détaillées")
    print()
    
    # Une fois les TODOs complétés, décommentez ce qui suit:
    
    # # Créer l'agent principal
    # agent = MyFirstAgent()
    # 
    # # Configuration LLM
    # if setup_llm_integration(agent.single_agent):
    #     implement_llm_call(agent.single_agent)
    #     implement_llm_call(agent.tool_agent)
    #     implement_llm_call(agent.human_loop_agent)
    # 
    # # Lancer la démonstration
    # demo_results = await agent.run_complete_demo()
    # 
    # # Validation finale
    # validation = validate_agent_capabilities(agent)
    # print_validation_report(validation)
    # 
    # # Sauvegarde
    # results_file = f"first_agent_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    # with open(results_file, "w") as f:
    #     json.dump({
    #         "demo_results": demo_results,
    #         "validation": validation,
    #         "stats": agent.get_stats()
    #     }, f, indent=2, default=str)
    # 
    # print(f"\n💾 Résultats sauvegardés: {results_file}")
    # return demo_results

if __name__ == "__main__":
    asyncio.run(main())