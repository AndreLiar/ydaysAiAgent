#!/usr/bin/env python3
"""
🎯 PROJET INTELLIGENT AGENT - STARTER TEMPLATE
Apprenez Semantic Kernel en construisant un agent intelligent avec mémoire !

📚 Ce fichier est votre template de démarrage. Suivez les TODO pour apprendre.
🚀 À la fin, vous aurez un assistant personnel avec planification et mémoire long-terme.

Temps estimé: 15 minutes
Difficulté: ⭐⭐⭐ (Intermédiaire)
"""

import os
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass
import json
from pathlib import Path

# TODO 1: Installer les dépendances
# pip install semantic-kernel openai python-dotenv

# TODO 2: Importer les modules nécessaires
# 💡 APPRENTISSAGE: Comprendre l'écosystème Semantic Kernel
from dotenv import load_dotenv
# Ajouter vos imports ici:
# import semantic_kernel as sk
# from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
# from semantic_kernel.planning import BasicPlanner
# from semantic_kernel.memory import SemanticTextMemory
# from semantic_kernel.connectors.ai.open_ai import OpenAITextEmbedding

load_dotenv()

# TODO 3: Définir l'état de l'agent intelligent
# 💡 APPRENTISSAGE: Mémoire et préférences utilisateur
@dataclass
class AgentState:
    """État persistant de l'agent intelligent"""
    # Définir les champs d'état ici
    pass

# TODO 4: Créer le système de plugins
# 💡 APPRENTISSAGE: Extensibilité avec plugins
class PluginRegistry:
    """Registre de plugins personnalisés"""
    
    def __init__(self):
        # TODO: Initialiser le registre
        pass
    
    def create_time_plugin(self):
        """Plugin pour gestion du temps"""
        # TODO: Implémenter le plugin temps
        pass
    
    def create_preference_plugin(self):
        """Plugin pour gestion des préférences"""
        # TODO: Implémenter le plugin préférences
        pass

class IntelligentAgentSystem:
    """
    🎯 VOTRE AGENT INTELLIGENT COMPLET
    
    Objectifs d'apprentissage:
    1. 🔷 Maîtriser les concepts Semantic Kernel
    2. 🔌 Créer et intégrer des plugins personnalisés
    3. 🧠 Implémenter une mémoire persistante
    4. 📋 Utiliser la planification automatique
    5. 🎯 Construire un assistant adaptatif
    """
    
    def __init__(self):
        """
        TODO 5: Initialiser votre agent intelligent
        💡 APPRENTISSAGE: Configuration Semantic Kernel
        
        À faire:
        - Créer le kernel principal
        - Configurer les services AI
        - Initialiser la mémoire sémantique
        - Préparer le système de plugins
        """
        print("🚀 Initialisation de votre agent intelligent...")
        
        # Vérifier la clé API
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
        
        # TODO: Créer le kernel Semantic Kernel
        # self.kernel = sk.Kernel()
        
        # TODO: Configurer le service AI
        # self.kernel.add_text_completion_service(
        #     "gpt-4",
        #     OpenAIChatCompletion("gpt-4", api_key)
        # )
        
        # TODO: Configurer les embeddings pour la mémoire
        # self.kernel.add_text_embedding_generation_service(
        #     "text-embedding-ada-002",
        #     OpenAITextEmbedding("text-embedding-ada-002", api_key)
        # )
        
        # TODO: Initialiser la mémoire sémantique
        # self.kernel.register_memory_store(SemanticTextMemory())
        
        # TODO: Initialiser vos variables d'instance
        # self.plugins = PluginRegistry()
        # self.planner = None
        # self.agent_state = AgentState()
        # self.conversation_history = []
        
        print("✅ Configuration de base terminée")
    
    def create_custom_plugins(self):
        """
        TODO 6: Créer des plugins personnalisés
        💡 APPRENTISSAGE: Système de plugins Semantic Kernel
        
        Plugins à créer:
        1. TimePlugin - Gestion du temps et planning
        2. PreferencePlugin - Préférences utilisateur
        3. MemoryPlugin - Gestion de la mémoire
        4. TaskPlugin - Gestion des tâches
        
        Concepts clés:
        - @sk_function decorator
        - Plugin registration
        - Function calling
        - Parameter handling
        """
        print("\\n🔌 ÉTAPE: Création de plugins personnalisés")
        print("=" * 60)
        
        # TODO: Créer le plugin Time
        # time_plugin = self.plugins.create_time_plugin()
        # self.kernel.import_plugin(time_plugin, "TimePlugin")
        
        # TODO: Créer le plugin Preference
        # preference_plugin = self.plugins.create_preference_plugin()
        # self.kernel.import_plugin(preference_plugin, "PreferencePlugin")
        
        # TODO: Exemple de plugin simple inline
        # @sk_function(
        #     description="Get the current weather for a location",
        #     name="get_weather"
        # )
        # def get_weather(location: str) -> str:
        #     # Simulation - en réalité, appel à API météo
        #     return f"The weather in {location} is sunny, 22°C"
        
        # TODO: Enregistrer le plugin inline
        # weather_plugin = sk.KernelPlugin.from_object(self, "WeatherPlugin")
        # self.kernel.import_plugin(weather_plugin)
        
        print("✅ TODO 6: Implémentez la création de plugins")
        return False
    
    def setup_semantic_memory(self):
        """
        TODO 7: Configurer la mémoire sémantique
        💡 APPRENTISSAGE: Mémoire persistante et recherche sémantique
        
        Fonctionnalités mémoire:
        - Stockage de conversations passées
        - Mémorisation des préférences
        - Recherche sémantique d'informations
        - Contexte long-terme
        
        Concepts:
        - Memory stores
        - Semantic search
        - Vector embeddings
        - Memory collections
        """
        print("\\n🧠 ÉTAPE: Configuration de la mémoire sémantique")
        print("=" * 60)
        
        # TODO: Créer les collections de mémoire
        # memory_collections = [
        #     "conversations",    # Historique des conversations
        #     "preferences",      # Préférences utilisateur
        #     "knowledge",        # Base de connaissances
        #     "tasks"            # Historique des tâches
        # ]
        
        # TODO: Initialiser les collections
        # for collection in memory_collections:
        #     try:
        #         await self.kernel.memory.create_collection_async(collection)
        #     except Exception:
        #         pass  # Collection existe déjà
        
        # TODO: Charger la mémoire existante
        # self._load_persistent_memory()
        
        print("✅ TODO 7: Implémentez la configuration de mémoire")
        return False
    
    def create_automatic_planner(self):
        """
        TODO 8: Créer le planificateur automatique
        💡 APPRENTISSAGE: Planification et orchestration automatique
        
        Capacités du planner:
        - Décomposition automatique de tâches complexes
        - Sélection de plugins appropriés
        - Orchestration multi-étapes
        - Adaptation en cas d'erreur
        
        Concepts:
        - BasicPlanner
        - Function calling
        - Plan execution
        - Error handling
        """
        print("\\n📋 ÉTAPE: Création du planificateur automatique")
        print("=" * 60)
        
        # TODO: Créer le planner
        # self.planner = BasicPlanner()
        
        # TODO: Configurer les capacités de planification
        # planning_config = {
        #     "max_tokens": 1000,
        #     "temperature": 0.3,
        #     "max_iterations": 5
        # }
        
        # TODO: Créer des exemples de plans
        # example_plans = [
        #     "Schedule a meeting for next week",
        #     "Find information about AI trends and save to memory",
        #     "Set user preference for morning reminders",
        #     "Plan a productive day based on user preferences"
        # ]
        
        print("✅ TODO 8: Implémentez le planificateur automatique")
        return False
    
    def implement_conversation_with_memory(self, user_input: str):
        """
        TODO 9: Implémenter la conversation avec mémoire
        💡 APPRENTISSAGE: Intégration mémoire et conversation
        
        Workflow conversationnel:
        1. Analyse de l'entrée utilisateur
        2. Recherche dans la mémoire sémantique
        3. Planification automatique si nécessaire
        4. Exécution avec plugins
        5. Mémorisation de la conversation
        """
        print(f"\\n💬 ÉTAPE: Conversation avec mémoire - '{user_input}'")
        print("=" * 60)
        
        start_time = datetime.now()
        
        try:
            # TODO: Rechercher le contexte dans la mémoire
            # relevant_memories = await self.kernel.memory.search_async(
            #     "conversations", user_input, limit=3
            # )
            
            # TODO: Construire le prompt avec contexte
            # context_prompt = self._build_context_prompt(user_input, relevant_memories)
            
            # TODO: Décider si planification nécessaire
            # needs_planning = self._analyze_complexity(user_input)
            
            # if needs_planning:
            #     # Utiliser le planner pour tâches complexes
            #     plan = await self.planner.create_plan_async(user_input, self.kernel)
            #     result = await plan.invoke_async()
            # else:
            #     # Réponse directe
            #     response_function = self.kernel.create_semantic_function(
            #         context_prompt,
            #         max_tokens=500,
            #         temperature=0.7
            #     )
            #     result = await response_function.invoke_async(user_input)
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            # TODO: Mémoriser la conversation
            # await self.kernel.memory.save_information_async(
            #     "conversations",
            #     f"User: {user_input}\\nAssistant: {result}",
            #     f"conversation_{datetime.now().isoformat()}"
            # )
            
            # TODO: Mettre à jour l'état de l'agent
            # self.agent_state.last_interaction = datetime.now().isoformat()
            # self.conversation_history.append({
            #     "user": user_input,
            #     "assistant": result,
            #     "timestamp": start_time.isoformat(),
            #     "execution_time": execution_time
            # })
            
            print("✅ TODO 9: Implémentez la conversation avec mémoire")
            return {
                "user_input": user_input,
                "response": "TODO 9: Réponse à implémenter",
                "execution_time": execution_time,
                "used_memory": True,
                "used_planning": False,  # À déterminer avec vraie logique
                "timestamp": start_time.isoformat()
            }
            
        except Exception as e:
            print(f"❌ Erreur durant la conversation: {e}")
            return None
    
    def manage_user_preferences(self, preference_type: str, value: Any):
        """
        TODO 10: Gérer les préférences utilisateur
        💡 APPRENTISSAGE: Personnalisation et adaptation
        
        Types de préférences:
        - Communication style
        - Notification settings
        - Task priorities
        - Personal information
        """
        print(f"\\n⚙️ ÉTAPE: Gestion des préférences - {preference_type}")
        print("=" * 60)
        
        # TODO: Valider le type de préférence
        # valid_preferences = [
        #     "communication_style",
        #     "notification_time",
        #     "task_priority",
        #     "personal_info",
        #     "language",
        #     "timezone"
        # ]
        
        # if preference_type not in valid_preferences:
        #     print(f"❌ Type de préférence invalide: {preference_type}")
        #     return False
        
        # TODO: Sauvegarder dans la mémoire sémantique
        # await self.kernel.memory.save_information_async(
        #     "preferences",
        #     f"{preference_type}: {value}",
        #     f"pref_{preference_type}"
        # )
        
        # TODO: Mettre à jour l'état local
        # setattr(self.agent_state, preference_type, value)
        
        print("✅ TODO 10: Implémentez la gestion des préférences")
        return False
    
    def demonstrate_planning_capabilities(self):
        """
        TODO 11: Démontrer les capacités de planification
        💡 APPRENTISSAGE: Planification complexe et adaptation
        
        Scénarios de planification:
        1. Planification de journée productive
        2. Organisation d'un projet
        3. Apprentissage d'un nouveau sujet
        4. Résolution de problème complexe
        """
        print("\\n🎯 ÉTAPE: Démonstration des capacités de planification")
        print("=" * 60)
        
        demo_scenarios = [
            "Plan me a productive day based on my preferences",
            "Help me organize a project to learn machine learning",
            "Create a strategy to improve my work-life balance",
            "Plan a research approach for AI agent frameworks"
        ]
        
        print("📋 Scénarios de planification:")
        for i, scenario in enumerate(demo_scenarios, 1):
            print(f"  {i}. {scenario}")
        
        # TODO: Exécuter les scénarios de planification
        # for scenario in demo_scenarios:
        #     print(f"\\n🎯 Scénario: {scenario}")
        #     print("-" * 40)
        #     
        #     # Créer et exécuter le plan
        #     plan = await self.planner.create_plan_async(scenario, self.kernel)
        #     result = await plan.invoke_async()
        #     
        #     print(f"📝 Plan généré: {plan}")
        #     print(f"✅ Résultat: {result}")
        
        print("✅ TODO 11: Implémentez la démonstration de planification")
    
    def save_agent_state(self):
        """
        TODO 12: Sauvegarder l'état de l'agent
        💡 APPRENTISSAGE: Persistance et continuité
        """
        print("\\n💾 ÉTAPE: Sauvegarde de l'état de l'agent")
        print("=" * 60)
        
        # TODO: Préparer les données d'état
        # state_data = {
        #     "agent_info": {
        #         "created_at": getattr(self.agent_state, 'created_at', datetime.now().isoformat()),
        #         "last_interaction": getattr(self.agent_state, 'last_interaction', None),
        #         "total_conversations": len(self.conversation_history),
        #         "version": "1.0.0"
        #     },
        #     "preferences": {
        #         # Extraire depuis la mémoire sémantique
        #     },
        #     "conversation_summary": {
        #         "recent_topics": [],  # Analyser depuis l'historique
        #         "user_interests": [],  # Déduire des conversations
        #         "recurring_tasks": []  # Identifier des patterns
        #     },
        #     "performance_metrics": {
        #         "avg_response_time": 0,  # Calculer depuis l'historique
        #         "successful_plans": 0,   # Compter les plans réussis
        #         "memory_usage": 0        # Estimer l'utilisation mémoire
        #     }
        # }
        
        # TODO: Sauvegarder dans memory_state.json
        # with open("memory_state.json", "w", encoding="utf-8") as f:
        #     json.dump(state_data, f, indent=2, ensure_ascii=False)
        
        print("✅ TODO 12: Implémentez la sauvegarde d'état")
    
    def run_demo(self):
        """
        TODO 13: Créer une démonstration complète
        💡 APPRENTISSAGE: Test end-to-end du système
        """
        print("\\n🎬 DÉMONSTRATION DE VOTRE AGENT INTELLIGENT")
        print("=" * 60)
        
        # Interactions de démonstration
        demo_interactions = [
            "Hello! I'm new here. Can you introduce yourself?",
            "I prefer formal communication style",
            "What's the weather like today?",
            "Help me plan a productive morning routine",
            "Remember that I'm interested in AI and machine learning"
        ]
        
        print("💬 Interactions de démonstration:")
        for i, interaction in enumerate(demo_interactions, 1):
            print(f"  {i}. {interaction}")
        
        print("\\n📋 Processus de démonstration:")
        print("  1. 🔌 Création des plugins personnalisés")
        print("  2. 🧠 Configuration de la mémoire sémantique")
        print("  3. 📋 Création du planificateur automatique")
        print("  4. 💬 Conversations avec mémoire")
        print("  5. ⚙️ Gestion des préférences")
        print("  6. 🎯 Démonstration de planification")
        print("  7. 💾 Sauvegarde de l'état")
        
        # TODO: Exécuter la démonstration complète
        # print("\\n⚡ Lancement de la démonstration...")
        
        # if self.create_custom_plugins():
        #     if self.setup_semantic_memory():
        #         if self.create_automatic_planner():
        #             # Exécuter les interactions
        #             for interaction in demo_interactions:
        #                 result = self.implement_conversation_with_memory(interaction)
        #                 if result:
        #                     print(f"💬 {interaction}")
        #                     print(f"🤖 {result['response']}")
        #                     print()
        #             
        #             self.demonstrate_planning_capabilities()
        #             self.save_agent_state()
        #             print("\\n🏆 Démonstration terminée avec succès!")
        #             print("💾 Consultez memory_state.json pour l'état de l'agent")
        #         else:
        #             print("❌ Échec de la création du planner")
        #     else:
        #         print("❌ Échec de la configuration mémoire")
        # else:
        #     print("❌ Échec de la création des plugins")
        
        print("\\n✅ TODO 13: Implémentez la démonstration complète")
    
    def _build_context_prompt(self, user_input: str, memories: List) -> str:
        """Construire un prompt avec contexte mémoire"""
        # TODO: Implémenter la construction de prompt
        return f"Context: {memories}\\nUser: {user_input}\\nAssistant:"
    
    def _analyze_complexity(self, user_input: str) -> bool:
        """Analyser si la requête nécessite planification"""
        # TODO: Implémenter l'analyse de complexité
        complex_keywords = ["plan", "organize", "strategy", "help me", "how to"]
        return any(keyword in user_input.lower() for keyword in complex_keywords)
    
    def _load_persistent_memory(self):
        """Charger la mémoire persistante"""
        # TODO: Implémenter le chargement de mémoire
        pass

def main():
    """
    🎯 FONCTION PRINCIPALE - VOTRE PARCOURS D'APPRENTISSAGE
    
    Suivez cette progression pour maîtriser Semantic Kernel:
    """
    print("🚀 BIENVENUE DANS VOTRE PROJET INTELLIGENT AGENT !")
    print("=" * 60)
    print("📚 Vous allez apprendre en construisant un assistant intelligent")
    print("🎯 Objectif: Agent avec planification et mémoire long-terme")
    print("⏱️ Temps estimé: 15 minutes")
    print("\\n📋 PROGRESSION:")
    print("  1. ✅ Configuration de base")
    print("  2. 🔌 Plugins personnalisés")
    print("  3. 🧠 Mémoire sémantique")
    print("  4. 📋 Planification automatique")
    print("  5. 💬 Conversation intelligente")
    print("  6. ⚙️ Préférences utilisateur")
    print("  7. 🎯 Démonstration planification")
    print("  8. 💾 Persistance état")
    
    try:
        # Initialiser l'agent
        agent_system = IntelligentAgentSystem()
        
        # Message d'encouragement
        print("\\n🎓 PRÊT À COMMENCER ?")
        print("👆 Suivez les TODO dans le code pour apprendre !")
        print("💡 Chaque TODO vous enseigne un concept important de Semantic Kernel")
        
        # TODO: Décommenter quand vous avez implémenté les méthodes
        # agent_system.run_demo()
        
        print("\\n🏆 Quand vous aurez terminé tous les TODO:")
        print("   - Vous maîtriserez Semantic Kernel")
        print("   - Vous aurez un assistant personnel intelligent")
        print("   - Vous comprendrez la planification automatique")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        print("💡 Vérifiez votre configuration (clé API, dépendances)")

if __name__ == "__main__":
    main()