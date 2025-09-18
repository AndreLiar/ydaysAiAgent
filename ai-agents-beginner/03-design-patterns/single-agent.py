#!/usr/bin/env python3
"""
Pattern 1: Single Agent - L'approche la plus simple
Un seul agent gère la tâche de bout en bout

Cas d'usage: FAQ, résumé, classification, Q&A simple
Avantages: Simplicité, rapidité, facilité de debug
Inconvénients: Limité pour tâches complexes
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

@dataclass
class SingleAgentResult:
    """Résultat standardisé d'un agent simple"""
    input_query: str
    output: str
    confidence: float
    processing_time: float
    metadata: Dict[str, Any]
    timestamp: str

class SingleAgent:
    """
    Agent simple - Pattern le plus basique
    Un agent, une tâche, un résultat
    """
    
    def __init__(self, role: str, system_prompt: str, model: str = "gpt-4"):
        self.role = role
        self.system_prompt = system_prompt
        self.model = model
        self.client = OpenAI()
        self.stats = {
            "total_queries": 0,
            "successful_queries": 0,
            "average_confidence": 0.0,
            "average_response_time": 0.0
        }
    
    def process(self, query: str, context: Optional[Dict] = None) -> SingleAgentResult:
        """Traiter une requête avec l'agent simple"""
        
        start_time = datetime.now()
        
        try:
            # Construire le prompt complet
            messages = [
                {"role": "system", "content": self.system_prompt}
            ]
            
            # Ajouter contexte si fourni
            if context:
                context_str = f"\nContexte: {json.dumps(context, indent=2)}"
                query = query + context_str
            
            messages.append({"role": "user", "content": query})
            
            # Appel LLM
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
                max_tokens=1000
            )
            
            output = response.choices[0].message.content
            processing_time = (datetime.now() - start_time).total_seconds()
            
            # Évaluer la confiance (simple heuristique)
            confidence = self._evaluate_confidence(query, output)
            
            # Créer le résultat
            result = SingleAgentResult(
                input_query=query,
                output=output,
                confidence=confidence,
                processing_time=processing_time,
                metadata={
                    "model": self.model,
                    "role": self.role,
                    "tokens_used": response.usage.total_tokens if response.usage else 0,
                    "context_provided": context is not None
                },
                timestamp=datetime.now().isoformat()
            )
            
            # Mettre à jour les stats
            self._update_stats(result)
            
            return result
            
        except Exception as e:
            # Gérer les erreurs gracieusement
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return SingleAgentResult(
                input_query=query,
                output=f"Erreur: {str(e)}",
                confidence=0.0,
                processing_time=processing_time,
                metadata={"error": True, "error_type": type(e).__name__},
                timestamp=datetime.now().isoformat()
            )
    
    def _evaluate_confidence(self, query: str, output: str) -> float:
        """Évaluer la confiance dans la réponse (heuristique simple)"""
        
        # Facteurs de confiance
        confidence_score = 0.5  # Base
        
        # Longueur de réponse appropriée
        if 50 <= len(output) <= 500:
            confidence_score += 0.2
        
        # Pas d'indication d'incertitude
        uncertainty_words = ["je ne sais pas", "peut-être", "possiblement", "incertain"]
        if not any(word in output.lower() for word in uncertainty_words):
            confidence_score += 0.2
        
        # Structure cohérente
        if output.count('.') >= 2:  # Au moins 2 phrases
            confidence_score += 0.1
        
        return min(1.0, confidence_score)
    
    def _update_stats(self, result: SingleAgentResult):
        """Mettre à jour les statistiques"""
        self.stats["total_queries"] += 1
        
        if result.confidence >= 0.6:
            self.stats["successful_queries"] += 1
        
        # Moyennes mobiles
        n = self.stats["total_queries"]
        
        # Confiance moyenne
        current_conf_avg = self.stats["average_confidence"]
        self.stats["average_confidence"] = (current_conf_avg * (n-1) + result.confidence) / n
        
        # Temps de réponse moyen
        current_time_avg = self.stats["average_response_time"]
        self.stats["average_response_time"] = (current_time_avg * (n-1) + result.processing_time) / n
    
    def get_stats(self) -> Dict[str, Any]:
        """Obtenir les statistiques de performance"""
        total = self.stats["total_queries"]
        success_rate = (self.stats["successful_queries"] / total * 100) if total > 0 else 0
        
        return {
            **self.stats,
            "success_rate": f"{success_rate:.1f}%",
            "average_confidence_percent": f"{self.stats['average_confidence']*100:.1f}%",
            "average_response_time_formatted": f"{self.stats['average_response_time']:.2f}s"
        }

class SpecializedSingleAgents:
    """Collection d'agents simples spécialisés"""
    
    def __init__(self):
        # Agent FAQ
        self.faq_agent = SingleAgent(
            role="FAQ_Assistant",
            system_prompt="""
            Tu es un assistant FAQ expert. Tu réponds aux questions fréquentes
            de manière claire, concise et actionnable.
            
            Format de réponse:
            1. Réponse directe en 1-2 phrases
            2. Étapes détaillées si nécessaire
            3. Ressources additionnelles si pertinentes
            
            Si tu ne connais pas la réponse, dis-le clairement et suggère qui contacter.
            """
        )
        
        # Agent Résumé
        self.summarizer_agent = SingleAgent(
            role="Content_Summarizer",
            system_prompt="""
            Tu es expert en résumé de contenu. Tu extrais les points clés
            et les présentes de manière structurée.
            
            Format de résumé:
            🎯 Point principal: [1 phrase]
            
            📋 Points clés:
            • Point 1
            • Point 2
            • Point 3
            
            💡 Implications: [1-2 phrases]
            
            Garde un ton professionnel et objectif.
            """
        )
        
        # Agent Classification
        self.classifier_agent = SingleAgent(
            role="Content_Classifier",
            system_prompt="""
            Tu es expert en classification de contenu. Tu analyses le texte
            et le catégorises selon des critères précis.
            
            Format de classification:
            📂 Catégorie: [catégorie principale]
            🏷️ Tags: [tag1, tag2, tag3]
            📊 Confiance: [pourcentage]
            💬 Justification: [explication courte]
            
            Sois précis dans tes classifications.
            """
        )
        
        # Agent Q&A Technique
        self.tech_qa_agent = SingleAgent(
            role="Technical_QA_Expert",
            system_prompt="""
            Tu es expert technique en développement et agents IA.
            Tu réponds aux questions techniques avec précision.
            
            Format de réponse:
            🎯 Réponse courte: [réponse directe]
            
            📝 Explication détaillée:
            [explication technique]
            
            💻 Exemple de code:
            ```python
            # Code exemple si pertinent
            ```
            
            ⚠️ Points d'attention:
            • Point 1
            • Point 2
            
            Sois précis et actionnable.
            """
        )

def demo_single_agents():
    """Démonstration des agents simples spécialisés"""
    
    print("🎯 Démonstration: Single Agent Pattern")
    print("=" * 60)
    
    agents = SpecializedSingleAgents()
    
    # Test cases pour chaque agent
    test_cases = [
        {
            "agent": agents.faq_agent,
            "name": "FAQ Assistant",
            "queries": [
                "Comment réinitialiser mon mot de passe?",
                "Quels sont vos horaires d'ouverture?",
                "Comment contacter le support technique?"
            ]
        },
        {
            "agent": agents.summarizer_agent,
            "name": "Content Summarizer", 
            "queries": [
                """
                Les agents IA révolutionnent le développement logiciel en automatisant des tâches complexes
                qui nécessitaient auparavant une intervention humaine directe. Contrairement aux chatbots
                traditionnels, les agents IA peuvent percevoir leur environnement, planifier des actions,
                exécuter des tâches et réfléchir sur leurs résultats. Cette capacité leur permet de gérer
                des workflows multi-étapes, d'intégrer différents outils et APIs, et de s'adapter aux
                situations changeantes. Les frameworks comme LangChain, AutoGen et CrewAI facilitent
                le développement d'agents collaboratifs qui peuvent travailler ensemble sur des projets
                complexes, chacun apportant ses spécialisations. L'impact sur la productivité est considérable:
                les développeurs rapportent une amélioration de 40% de leur efficacité lors de l'utilisation
                d'agents IA pour des tâches comme la génération de code, les tests automatisés et la
                documentation. Cependant, l'adoption nécessite une formation et une adaptation des processus
                existants pour maximiser les bénéfices.
                """
            ]
        },
        {
            "agent": agents.classifier_agent,
            "name": "Content Classifier",
            "queries": [
                "Je n'arrive pas à installer les dépendances Python pour mon projet d'agents IA",
                "Félicitations pour votre excellent travail sur ce projet!",
                "URGENT: Le serveur de production est en panne depuis 2 heures"
            ]
        },
        {
            "agent": agents.tech_qa_agent,
            "name": "Technical Q&A",
            "queries": [
                "Comment implémenter un système RAG avec LangChain?",
                "Quelle différence entre AutoGen et CrewAI?",
                "Comment gérer la mémoire dans un agent conversationnel?"
            ]
        }
    ]
    
    # Tester chaque agent
    all_results = []
    
    for test_case in test_cases:
        agent = test_case["agent"]
        name = test_case["name"]
        
        print(f"\n🤖 Agent: {name}")
        print("-" * 40)
        
        for i, query in enumerate(test_case["queries"], 1):
            print(f"\n📝 Test {i}: {query[:60]}...")
            
            result = agent.process(query)
            
            print(f"⏱️  Temps: {result.processing_time:.2f}s")
            print(f"🎯 Confiance: {result.confidence*100:.1f}%")
            print(f"💬 Réponse: {result.output[:200]}...")
            
            all_results.append(result)
        
        # Stats de l'agent
        stats = agent.get_stats()
        print(f"\n📊 Stats {name}:")
        print(f"   Requêtes: {stats['total_queries']}")
        print(f"   Succès: {stats['success_rate']}")
        print(f"   Confiance moy.: {stats['average_confidence_percent']}")
        print(f"   Temps moy.: {stats['average_response_time_formatted']}")
    
    # Statistiques globales
    print(f"\n📈 STATISTIQUES GLOBALES")
    print("=" * 40)
    
    total_queries = len(all_results)
    avg_confidence = sum(r.confidence for r in all_results) / total_queries
    avg_time = sum(r.processing_time for r in all_results) / total_queries
    high_confidence_count = sum(1 for r in all_results if r.confidence >= 0.8)
    
    print(f"Total requêtes traitées: {total_queries}")
    print(f"Confiance moyenne: {avg_confidence*100:.1f}%")
    print(f"Temps moyen: {avg_time:.2f}s")
    print(f"Haute confiance (>80%): {high_confidence_count}/{total_queries}")
    
    return all_results

def interactive_single_agent():
    """Mode interactif pour tester les agents"""
    
    print(f"\n🎮 Mode Interactif - Single Agent Pattern")
    print("=" * 50)
    
    agents = SpecializedSingleAgents()
    
    agent_choices = {
        "1": ("FAQ Assistant", agents.faq_agent),
        "2": ("Content Summarizer", agents.summarizer_agent), 
        "3": ("Content Classifier", agents.classifier_agent),
        "4": ("Technical Q&A", agents.tech_qa_agent)
    }
    
    print("Choisissez un agent:")
    for key, (name, _) in agent_choices.items():
        print(f"  {key}. {name}")
    
    choice = input(f"\nVotre choix (1-4): ").strip()
    
    if choice not in agent_choices:
        print("❌ Choix invalide")
        return
    
    agent_name, agent = agent_choices[choice]
    print(f"\n🤖 Vous utilisez: {agent_name}")
    print("Tapez 'quit' pour quitter\n")
    
    while True:
        query = input("💬 Votre question: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
            
        if query:
            result = agent.process(query)
            
            print(f"\n🎯 Réponse:")
            print(result.output)
            print(f"\n⏱️ Temps: {result.processing_time:.2f}s | Confiance: {result.confidence*100:.1f}%")
            print("-" * 50)
    
    # Afficher les stats finales
    stats = agent.get_stats()
    print(f"\n📊 Stats de votre session:")
    print(f"   Requêtes: {stats['total_queries']}")
    print(f"   Taux de succès: {stats['success_rate']}")
    print(f"   Confiance moyenne: {stats['average_confidence_percent']}")

def main():
    """Démonstration complète du Single Agent Pattern"""
    
    print("🎯 Single Agent Design Pattern")
    print("=" * 60)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY manquante!")
        print("   Ajoutez votre clé dans le fichier .env")
        return
    
    print("🎯 Choisissez une option:")
    print("1. Démonstration automatique (tous les agents)")
    print("2. Mode interactif (tester un agent)")
    
    choice = input("\nVotre choix (1-2): ").strip()
    
    if choice == "1":
        demo_single_agents()
    elif choice == "2":
        interactive_single_agent()
    else:
        print("❌ Choix invalide, lancement démo automatique")
        demo_single_agents()
    
    print(f"\n💡 Points Clés - Single Agent Pattern:")
    print(f"   ✅ Simplicité maximale")
    print(f"   ✅ Rapidité d'exécution") 
    print(f"   ✅ Facilité de debug")
    print(f"   ✅ Idéal pour tâches bien définies")
    print(f"   ⚠️  Limité pour tâches complexes")
    
    print(f"\n🔄 Next: Passez au Multi-Agent Collaboration pour tâches complexes!")

if __name__ == "__main__":
    main()