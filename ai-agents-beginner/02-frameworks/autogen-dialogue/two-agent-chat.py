#!/usr/bin/env python3
"""
AutoGen - Conversations Multi-Agents
Démonstration de dialogues naturels entre agents spécialisés
"""

import os
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

# Dependencies: pip install autogen-agentchat
from autogen import ConversableAgent, GroupChat, GroupChatManager

load_dotenv()

class AutoGenDemo:
    """Démonstration des conversations AutoGen"""
    
    def __init__(self):
        # Configuration LLM pour AutoGen
        self.llm_config = {
            "model": "gpt-4",
            "api_key": os.getenv("OPENAI_API_KEY"),
            "temperature": 0.7
        }
        
        print("🤖 AutoGen Demo initialisé")
    
    def demo_simple_dialogue(self):
        """Dialogue simple entre 2 agents"""
        print("\n💬 DEMO 1: Dialogue Simple (Expert + Assistant)")
        print("=" * 50)
        
        # Agent Expert
        expert = ConversableAgent(
            name="AI_Expert",
            system_message="""
            Tu es un expert en agents IA avec 10 ans d'expérience.
            Tu donnes des conseils techniques précis et pratiques.
            Tu poses des questions pertinentes pour clarifier les besoins.
            Réponds de manière concise et actionnable.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=3
        )
        
        # Agent Assistant/Questionneur
        assistant = ConversableAgent(
            name="Curious_Developer",
            system_message="""
            Tu es un développeur curieux qui apprend les agents IA.
            Tu poses des questions pratiques et demandes des exemples concrets.
            Tu creuses les sujets pour vraiment comprendre.
            Tu valides ta compréhension en reformulant.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            max_consecutive_auto_reply=3
        )
        
        # Lancer la conversation
        print("\n🚀 Lancement du dialogue...")
        
        # L'assistant initie avec une question
        result = assistant.initiate_chat(
            expert,
            message="""
            Salut ! Je développe ma première application avec des agents IA.
            J'hésite entre LangChain, CrewAI et AutoGen. 
            Peux-tu m'expliquer les principales différences et quand utiliser chacun ?
            """,
            max_turns=6
        )
        
        return result
    
    def demo_group_brainstorm(self):
        """Brainstorming en groupe avec 4 agents"""
        print("\n🧠 DEMO 2: Brainstorming de Groupe (4 Agents)")
        print("=" * 50)
        
        # Agent Product Manager
        product_manager = ConversableAgent(
            name="Product_Manager",
            system_message="""
            Tu es un Product Manager expérimenté dans l'IA.
            Tu penses business value, user experience, et faisabilité.
            Tu poses les bonnes questions produit et priorises les features.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Agent Tech Lead
        tech_lead = ConversableAgent(
            name="Tech_Lead", 
            system_message="""
            Tu es Tech Lead avec expertise en agents IA.
            Tu évalues la faisabilité technique et l'architecture.
            Tu identifies les risques et propose des solutions robustes.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Agent UX Designer
        ux_designer = ConversableAgent(
            name="UX_Designer",
            system_message="""
            Tu es UX Designer spécialisé dans les interfaces IA.
            Tu penses user journey, accessibilité, et simplicité.
            Tu proposes des solutions centrées utilisateur.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Agent Data Scientist
        data_scientist = ConversableAgent(
            name="Data_Scientist",
            system_message="""
            Tu es Data Scientist expert en ML/IA.
            Tu évalues les besoins en données, modèles, et métriques.
            Tu anticipes les challenges liés à la performance des modèles.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Créer le groupe de discussion
        group_chat = GroupChat(
            agents=[product_manager, tech_lead, ux_designer, data_scientist],
            messages=[],
            max_round=12,  # Nombre maximum de tours
            speaker_selection_method="auto"  # Sélection automatique du speaker
        )
        
        # Manager du groupe
        manager = GroupChatManager(
            groupchat=group_chat,
            llm_config=self.llm_config,
            system_message="""
            Tu coordonnes la discussion de brainstorming.
            Assure-toi que chaque perspective (produit, tech, UX, data) est entendue.
            Guide vers une solution équilibrée et réalisable.
            """
        )
        
        print("\n🚀 Lancement du brainstorming...")
        
        # Initier le brainstorming
        result = product_manager.initiate_chat(
            manager,
            message="""
            🎯 BRAINSTORMING SESSION: Customer Service AI Agent
            
            Nous voulons créer un agent IA pour le support client qui:
            - Résout 70% des tickets automatiquement
            - S'intègre avec notre CRM existant
            - Escalade intelligemment vers les humains
            - Apprend des interactions passées
            
            Budget: 6 mois, équipe de 4 devs.
            
            Chacun, donnez votre perspective et vos recommandations!
            """,
            max_turns=12
        )
        
        return result
    
    def demo_code_review(self):
        """Session de code review collaborative"""
        print("\n👨‍💻 DEMO 3: Code Review Collaborative")
        print("=" * 50)
        
        # Agent Senior Developer
        senior_dev = ConversableAgent(
            name="Senior_Developer",
            system_message="""
            Tu es un Senior Developer avec expertise en Python et agents IA.
            Tu reviews le code pour: performance, sécurité, maintenabilité.
            Tu donnes des suggestions constructives avec des exemples.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Agent Security Specialist  
        security_expert = ConversableAgent(
            name="Security_Expert",
            system_message="""
            Tu es expert en sécurité des applications IA.
            Tu identifies les vulnérabilités, les fuites de données potentielles.
            Tu proposes des améliorations sécurisées.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Agent Performance Specialist
        performance_expert = ConversableAgent(
            name="Performance_Expert", 
            system_message="""
            Tu es spécialisé dans l'optimisation des performances.
            Tu identifies les bottlenecks, problèmes de scalabilité.
            Tu proposes des optimisations concrètes.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        # Groupe de code review
        code_review_group = GroupChat(
            agents=[senior_dev, security_expert, performance_expert],
            messages=[],
            max_round=10,
            speaker_selection_method="round_robin"  # Chacun son tour
        )
        
        code_review_manager = GroupChatManager(
            groupchat=code_review_group,
            llm_config=self.llm_config
        )
        
        # Code à reviewer (exemple realistic)
        code_to_review = '''
class AIAgent:
    def __init__(self, api_key):
        self.api_key = api_key  # Stored in plain text
        self.client = OpenAI(api_key=api_key)
        self.chat_history = []  # Unlimited growth
    
    def process_request(self, user_input):
        # No input validation
        self.chat_history.append(user_input)
        
        # Synchronous call - blocks everything
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}],
            timeout=None  # No timeout
        )
        
        result = response.choices[0].message.content
        self.chat_history.append(result)
        
        # Log everything including sensitive data
        print(f"User: {user_input}, API Key: {self.api_key}, Response: {result}")
        
        return result
    
    def get_history(self):
        return self.chat_history  # No access control
        '''
        
        print("\n🚀 Lancement du code review...")
        
        result = senior_dev.initiate_chat(
            code_review_manager,
            message=f"""
            📋 CODE REVIEW REQUEST
            
            Voici un code d'agent IA à reviewer:
            
            ```python
            {code_to_review}
            ```
            
            Chaque expert, donnez votre analyse:
            - Points problématiques
            - Suggestions d'amélioration  
            - Code alternatif si nécessaire
            
            Focus sur la production-readiness!
            """,
            max_turns=10
        )
        
        return result
    
    def demo_human_in_loop(self):
        """Démonstration avec intervention humaine"""
        print("\n👤 DEMO 4: Human-in-the-Loop")
        print("=" * 50)
        
        # Agent qui peut demander validation humaine
        consultant = ConversableAgent(
            name="AI_Consultant",
            system_message="""
            Tu es consultant en agents IA. 
            Pour les décisions importantes, tu demandes validation humaine.
            Tu présentes clairement les options et leurs implications.
            """,
            llm_config=self.llm_config,
            human_input_mode="ALWAYS",  # Intervention humaine activée
            max_consecutive_auto_reply=2
        )
        
        # Agent client
        client = ConversableAgent(
            name="Business_Client",
            system_message="""
            Tu représentes une entreprise qui veut implémenter des agents IA.
            Tu poses des questions business et veux des recommandations claires.
            """,
            llm_config=self.llm_config,
            human_input_mode="NEVER"
        )
        
        print("💡 Dans cette démo, le consultant demandera votre avis!")
        print("   Tapez vos réponses quand demandé, 'exit' pour terminer\n")
        
        try:
            result = client.initiate_chat(
                consultant,
                message="""
                Nous sommes une entreprise de 200 employés dans la logistique.
                Nous voulons automatiser notre support client avec des agents IA.
                
                Questions:
                1. Par où commencer?
                2. Quel budget prévoir?
                3. Quels risques anticiper?
                4. Timeline réaliste?
                
                Nous avons besoin de recommandations concrètes!
                """,
                max_turns=8
            )
        except KeyboardInterrupt:
            print("\n⏹️ Session human-in-the-loop interrompue")
            result = None
        
        return result


def main():
    """Démonstration complète AutoGen"""
    
    print("🤖 AutoGen Multi-Agent Conversations Demo")
    print("=" * 60)
    
    # Vérifier les prérequis
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY manquante!")
        print("   Ajoutez votre clé dans le fichier .env")
        return
    
    demo = AutoGenDemo()
    
    try:
        print("🎯 Choisissez une démo:")
        print("1. Dialogue Simple (2 agents)")
        print("2. Brainstorming de Groupe (4 agents)")
        print("3. Code Review Collaboratif (3 experts)")
        print("4. Human-in-the-Loop (avec interaction)")
        print("5. Toutes les démos (sauf human-in-loop)")
        
        choice = input("\n📝 Votre choix (1-5): ").strip()
        
        if choice == "1":
            demo.demo_simple_dialogue()
        elif choice == "2":
            demo.demo_group_brainstorm()
        elif choice == "3":
            demo.demo_code_review()
        elif choice == "4":
            demo.demo_human_in_loop()
        elif choice == "5":
            demo.demo_simple_dialogue()
            print("\n" + "="*60)
            demo.demo_group_brainstorm()
            print("\n" + "="*60)
            demo.demo_code_review()
        else:
            print("❌ Choix invalide, lancement dialogue simple par défaut")
            demo.demo_simple_dialogue()
        
        print(f"\n🎉 Démonstrations AutoGen terminées!")
        print(f"\n💡 Points clés AutoGen:")
        print(f"   ✅ Conversations naturelles entre agents")
        print(f"   ✅ Gestion automatique des tours de parole")
        print(f"   ✅ GroupChat pour discussions multi-agents")
        print(f"   ✅ Human-in-the-loop pour validation")
        print(f"   ✅ Orchestration flexible et adaptable")
        
    except KeyboardInterrupt:
        print(f"\n⏹️ Démo interrompue par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur pendant la démo: {e}")


if __name__ == "__main__":
    main()