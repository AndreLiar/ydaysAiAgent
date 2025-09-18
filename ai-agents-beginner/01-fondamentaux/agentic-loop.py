#!/usr/bin/env python3
"""
Fondamentaux - Boucle Agentique Universelle
Implémentation du pattern Perception → Plan → Act → Reflect
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class BaseAgent:
    """
    Agent de base implémentant la boucle agentique universelle
    Perception → Plan → Act → Reflect
    """
    
    def __init__(self, role: str = "Assistant", model: str = "gpt-4"):
        self.role = role
        self.model = model
        self.client = OpenAI()
        self.execution_history = []
        self.stats = {
            "total_runs": 0,
            "successful_runs": 0,
            "average_reflection_score": 0.0
        }
    
    def perceive(self, input_data: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        PERCEPTION: Analyser l'input utilisateur et le contexte
        """
        print("🔍 PERCEPTION - Analyse de l'input...")
        
        perception = {
            "user_input": input_data,
            "timestamp": datetime.now().isoformat(),
            "context": context or {},
            "input_type": self._classify_input(input_data),
            "complexity": self._estimate_complexity(input_data),
            "role": self.role
        }
        
        print(f"   Type: {perception['input_type']}")
        print(f"   Complexité: {perception['complexity']}/5")
        
        return perception
    
    def plan(self, perception: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        PLAN: Créer un plan d'action basé sur la perception
        """
        print("📋 PLAN - Création du plan d'action...")
        
        planning_prompt = f"""
        Tu es un {self.role}. Analyse cette demande et crée un plan d'action.
        
        Demande: {perception['user_input']}
        Type: {perception['input_type']}
        Complexité: {perception['complexity']}/5
        
        Réponds UNIQUEMENT avec un JSON contenant:
        {{
            "steps": [
                {{"action": "action_name", "description": "what to do", "priority": 1}},
                ...
            ],
            "estimated_time": "temps estimé",
            "approach": "approche choisie"
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": planning_prompt}],
                temperature=0.3
            )
            
            plan_json = json.loads(response.choices[0].message.content)
            
            print(f"   Approche: {plan_json.get('approach', 'Standard')}")
            print(f"   Étapes: {len(plan_json.get('steps', []))}")
            print(f"   Temps estimé: {plan_json.get('estimated_time', 'Non estimé')}")
            
            return plan_json.get('steps', [])
            
        except Exception as e:
            print(f"   ⚠️  Erreur de planification: {e}")
            # Plan de fallback
            return [{"action": "respond", "description": "Répondre directement", "priority": 1}]
    
    def act(self, plan: List[Dict[str, Any]], perception: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        ACT: Exécuter chaque étape du plan
        """
        print("⚡ ACTION - Exécution du plan...")
        
        results = []
        
        for i, step in enumerate(plan, 1):
            print(f"   Étape {i}: {step.get('description', step.get('action'))}")
            
            if step.get('action') == 'respond':
                # Action principale: générer une réponse
                response = self._generate_response(perception['user_input'])
                results.append({
                    "step": i,
                    "action": step.get('action'),
                    "result": response,
                    "success": True,
                    "timestamp": datetime.now().isoformat()
                })
                
            elif step.get('action') == 'search':
                # Simulation d'une recherche
                results.append({
                    "step": i,
                    "action": step.get('action'),
                    "result": f"Recherche effectuée pour: {perception['user_input'][:50]}...",
                    "success": True,
                    "timestamp": datetime.now().isoformat()
                })
                
            else:
                # Action générique
                results.append({
                    "step": i,
                    "action": step.get('action'),
                    "result": f"Action '{step.get('action')}' exécutée",
                    "success": True,
                    "timestamp": datetime.now().isoformat()
                })
        
        print(f"   ✅ {len(results)} actions exécutées")
        return results
    
    def reflect(self, results: List[Dict[str, Any]], expected_outcome: Optional[str] = None) -> Dict[str, Any]:
        """
        REFLECT: Évaluer les résultats et identifier les améliorations
        """
        print("🤔 REFLECTION - Évaluation des résultats...")
        
        # Calcul des métriques de base
        successful_steps = sum(1 for r in results if r.get('success', False))
        total_steps = len(results)
        success_rate = successful_steps / total_steps if total_steps > 0 else 0
        
        # Auto-évaluation avec le LLM
        reflection_prompt = f"""
        Évalue cette exécution d'agent sur une échelle de 1-5:
        
        Résultats: {json.dumps(results, indent=2)}
        Objectif attendu: {expected_outcome or "Non spécifié"}
        
        Réponds UNIQUEMENT avec un JSON:
        {{
            "quality_score": 4.2,
            "strengths": ["point fort 1", "point fort 2"],
            "improvements": ["amélioration 1", "amélioration 2"],
            "confidence": 0.85,
            "next_actions": ["action 1", "action 2"]
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": reflection_prompt}],
                temperature=0.2
            )
            
            auto_reflection = json.loads(response.choices[0].message.content)
            
        except Exception as e:
            print(f"   ⚠️  Erreur d'auto-réflection: {e}")
            auto_reflection = {
                "quality_score": 3.0,
                "strengths": ["Exécution complète"],
                "improvements": ["Gestion d'erreurs"],
                "confidence": 0.5,
                "next_actions": ["Améliorer la robustesse"]
            }
        
        reflection = {
            "success_rate": success_rate,
            "total_steps": total_steps,
            "quality_score": auto_reflection.get("quality_score", 3.0),
            "strengths": auto_reflection.get("strengths", []),
            "improvements": auto_reflection.get("improvements", []),
            "confidence": auto_reflection.get("confidence", 0.5),
            "next_actions": auto_reflection.get("next_actions", []),
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"   Score qualité: {reflection['quality_score']}/5")
        print(f"   Taux de succès: {reflection['success_rate']*100:.1f}%")
        print(f"   Points forts: {', '.join(reflection['strengths'][:2])}")
        
        return reflection
    
    def run_loop(self, input_data: str, expected_outcome: Optional[str] = None) -> Dict[str, Any]:
        """
        Exécuter la boucle agentique complète
        Perception → Plan → Act → Reflect
        """
        print(f"🤖 Démarrage de la boucle agentique - {self.role}")
        print("=" * 60)
        
        # 1. PERCEPTION
        perception = self.perceive(input_data)
        
        # 2. PLAN
        plan = self.plan(perception)
        
        # 3. ACT
        results = self.act(plan, perception)
        
        # 4. REFLECT
        reflection = self.reflect(results, expected_outcome)
        
        # Enregistrer l'exécution
        execution = {
            "input": input_data,
            "perception": perception,
            "plan": plan,
            "results": results,
            "reflection": reflection,
            "final_output": results[-1].get('result') if results else "Aucun résultat"
        }
        
        self.execution_history.append(execution)
        
        # Mettre à jour les statistiques
        self._update_stats(reflection)
        
        print("=" * 60)
        print(f"✅ Boucle terminée - Score: {reflection['quality_score']}/5")
        
        return execution
    
    def _classify_input(self, input_data: str) -> str:
        """Classifier le type d'input"""
        if "?" in input_data:
            return "question"
        elif any(word in input_data.lower() for word in ["créer", "générer", "faire", "implémenter"]):
            return "creation"
        elif any(word in input_data.lower() for word in ["analyser", "examiner", "étudier"]):
            return "analysis"
        else:
            return "general"
    
    def _estimate_complexity(self, input_data: str) -> int:
        """Estimer la complexité sur 5"""
        words = len(input_data.split())
        if words < 10:
            return 1
        elif words < 20:
            return 2
        elif words < 40:
            return 3
        elif words < 80:
            return 4
        else:
            return 5
    
    def _generate_response(self, input_data: str) -> str:
        """Générer une réponse avec le LLM"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"Tu es un {self.role} expert et utile."},
                    {"role": "user", "content": input_data}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erreur lors de la génération: {e}"
    
    def _update_stats(self, reflection: Dict[str, Any]):
        """Mettre à jour les statistiques de performance"""
        self.stats["total_runs"] += 1
        if reflection["quality_score"] >= 3.0:
            self.stats["successful_runs"] += 1
        
        # Moyenne mobile du score de réflection
        current_avg = self.stats["average_reflection_score"]
        new_score = reflection["quality_score"]
        n = self.stats["total_runs"]
        self.stats["average_reflection_score"] = (current_avg * (n-1) + new_score) / n
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtenir les statistiques de performance"""
        return self.stats.copy()
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """Obtenir l'historique des exécutions"""
        return self.execution_history.copy()


def demo_agentic_loop():
    """Démonstration de la boucle agentique"""
    
    print("🚀 Démonstration de la Boucle Agentique")
    print("=" * 60)
    
    # Créer un agent
    agent = BaseAgent(role="Expert en IA", model="gpt-4")
    
    # Test 1: Question simple
    print("\n📝 Test 1: Question Simple")
    result1 = agent.run_loop(
        "Qu'est-ce qu'un agent IA?",
        expected_outcome="Définition claire et concise d'un agent IA"
    )
    
    # Test 2: Tâche complexe
    print("\n📝 Test 2: Tâche de Création")
    result2 = agent.run_loop(
        "Créer un plan de développement pour une application mobile de e-commerce avec des agents IA intégrés",
        expected_outcome="Plan détaillé avec étapes, technologies et timeline"
    )
    
    # Test 3: Analyse
    print("\n📝 Test 3: Tâche d'Analyse")
    result3 = agent.run_loop(
        "Analyser les avantages et inconvénients des différents frameworks d'agents IA: LangChain, AutoGen, CrewAI",
        expected_outcome="Comparaison détaillée avec recommandations"
    )
    
    # Afficher les statistiques
    print("\n📊 Statistiques de Performance")
    stats = agent.get_stats()
    print(f"   Exécutions totales: {stats['total_runs']}")
    print(f"   Exécutions réussies: {stats['successful_runs']}")
    print(f"   Taux de succès: {stats['successful_runs']/stats['total_runs']*100:.1f}%")
    print(f"   Score moyen: {stats['average_reflection_score']:.2f}/5")
    
    return agent


if __name__ == "__main__":
    # Vérifier la clé API
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY manquante!")
        print("   Ajoutez votre clé dans le fichier .env")
        print("   Ou utilisez: export OPENAI_API_KEY='your-key-here'")
        exit(1)
    
    # Lancer la démonstration
    agent = demo_agentic_loop()
    
    # Mode interactif
    print("\n🎮 Mode Interactif - Testez votre agent!")
    print("   Tapez 'quit' pour quitter")
    
    while True:
        user_input = input("\n💬 Votre question/tâche: ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if user_input.strip():
            result = agent.run_loop(user_input)
            print(f"\n🎯 Réponse finale:")
            print(f"   {result['final_output']}")
    
    print("\n👋 Merci d'avoir testé la boucle agentique!")
    print(f"   Statistiques finales: {agent.get_stats()}")