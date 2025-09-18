#!/usr/bin/env python3
"""
CrewAI - Équipes d'Agents Collaboratifs
Démonstration de crews d'agents spécialisés qui travaillent ensemble
"""

import os
from typing import Dict, List, Any
from dotenv import load_dotenv

# Dependencies: pip install crewai langchain-openai
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

load_dotenv()

class CrewAIDemo:
    """Démonstration des équipes CrewAI"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )
        print("⚓ CrewAI Demo initialisé")
    
    def demo_research_crew(self):
        """Équipe de recherche: Researcher + Analyst + Writer"""
        print("\n🔬 DEMO 1: Équipe de Recherche Collaborative")
        print("=" * 50)
        
        # 1. Définir les agents avec rôles spécialisés
        researcher = Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments in AI agents',
            backstory="""
            You're a seasoned researcher with a knack for uncovering the latest 
            developments in AI and machine learning. You're known for your ability 
            to find the most relevant information and present it clearly.
            """,
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
        
        analyst = Agent(
            role='Tech Content Strategist', 
            goal='Craft compelling content on tech advancements',
            backstory="""
            You're a renowned Content Strategist, known for your insightful 
            and engaging articles on technology and AI. You transform complex 
            concepts into accessible, compelling narratives.
            """,
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
        
        writer = Agent(
            role='Content Writer',
            goal='Write engaging blog posts about AI developments',
            backstory="""
            You're a skilled writer with a talent for making complex topics 
            accessible to a broad audience. You have a knack for storytelling 
            and creating content that resonates with readers.
            """,
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
        
        # 2. Définir les tâches séquentielles
        research_task = Task(
            description="""
            Conduct a comprehensive analysis of the latest advancements in AI agents.
            Identify the next big trend, key players, and potential industry impacts.
            Your final answer MUST be a full analysis report.
            """,
            agent=researcher,
            expected_output="A comprehensive research report on AI agents trends"
        )
        
        analysis_task = Task(
            description="""
            Using the research report from the researcher, develop a compelling 
            angle for a blog post about AI agents. Focus on practical applications 
            and business impact. Your final answer MUST be a content strategy outline.
            """,
            agent=analyst,
            expected_output="A detailed content strategy outline",
            dependencies=[research_task]
        )
        
        writing_task = Task(
            description="""
            Using the content strategy outline, write an engaging blog post 
            about AI agents developments. Make it accessible to business leaders 
            and developers alike. Include actionable insights.
            Your final answer MUST be a complete blog post.
            """,
            agent=writer,
            expected_output="A complete, engaging blog post about AI agents",
            dependencies=[analysis_task]
        )
        
        # 3. Créer et exécuter l'équipe
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("\n🚀 Lancement de l'équipe de recherche...")
        result = crew.kickoff()
        
        print(f"\n📄 Article Final Généré:")
        print("=" * 60)
        print(result)
        print("=" * 60)
        
        return result
    
    def demo_marketing_crew(self):
        """Équipe marketing: Market Researcher + Copywriter + Designer"""
        print("\n📈 DEMO 2: Équipe Marketing Collaborative")
        print("=" * 50)
        
        # Agents spécialisés en marketing
        market_researcher = Agent(
            role='Market Research Specialist',
            goal='Analyze market trends and customer needs for AI products',
            backstory="""
            You're an expert market researcher specializing in AI and tech products.
            You excel at understanding customer pain points, market gaps, and 
            competitive landscapes.
            """,
            verbose=True,
            llm=self.llm
        )
        
        copywriter = Agent(
            role='Senior Copywriter',
            goal='Create compelling marketing copy that converts',
            backstory="""
            You're a master of persuasive writing with 10 years of experience 
            in tech marketing. You know how to translate features into benefits 
            and create copy that drives action.
            """,
            verbose=True,
            llm=self.llm
        )
        
        strategist = Agent(
            role='Marketing Strategist',
            goal='Develop comprehensive marketing campaigns',
            backstory="""
            You're a strategic thinker who sees the big picture. You excel at 
            creating marketing campaigns that align with business goals and 
            resonate with target audiences.
            """,
            verbose=True,
            llm=self.llm
        )
        
        # Tâches marketing collaboratives
        market_research_task = Task(
            description="""
            Research the market for AI agent development tools. Identify:
            1. Target audience segments (developers, businesses, startups)
            2. Key pain points and needs
            3. Competitor analysis
            4. Market opportunities
            Your final answer MUST be a comprehensive market research report.
            """,
            agent=market_researcher,
            expected_output="Detailed market research report with actionable insights"
        )
        
        copy_task = Task(
            description="""
            Based on the market research, create compelling marketing copy for 
            an AI agent development platform. Include:
            1. Main value proposition
            2. Feature benefits (not just features)
            3. Call-to-action messages
            4. Different copy variants for different segments
            Your final answer MUST be complete marketing copy.
            """,
            agent=copywriter,
            expected_output="Complete marketing copy with multiple variants",
            dependencies=[market_research_task]
        )
        
        strategy_task = Task(
            description="""
            Using the market research and marketing copy, develop a comprehensive 
            go-to-market strategy. Include:
            1. Target audience prioritization
            2. Channel strategy (content, ads, partnerships)
            3. Launch timeline and milestones
            4. Success metrics and KPIs
            Your final answer MUST be a complete marketing strategy.
            """,
            agent=strategist,
            expected_output="Comprehensive go-to-market strategy document",
            dependencies=[market_research_task, copy_task]
        )
        
        # Équipe marketing
        marketing_crew = Crew(
            agents=[market_researcher, copywriter, strategist],
            tasks=[market_research_task, copy_task, strategy_task],
            process=Process.sequential,
            verbose=True
        )
        
        print("\n🚀 Lancement de l'équipe marketing...")
        result = marketing_crew.kickoff()
        
        print(f"\n📊 Stratégie Marketing Complète:")
        print("=" * 60)
        print(result)
        print("=" * 60)
        
        return result
    
    def demo_parallel_crew(self):
        """Équipe avec traitement parallèle"""
        print("\n⚡ DEMO 3: Équipe avec Traitement Parallèle")
        print("=" * 50)
        
        # Agents qui peuvent travailler en parallèle
        frontend_dev = Agent(
            role='Frontend Developer',
            goal='Create user-friendly interfaces for AI applications',
            backstory="Expert in React, UX/UI, and modern frontend technologies",
            verbose=True,
            llm=self.llm
        )
        
        backend_dev = Agent(
            role='Backend Developer', 
            goal='Build robust APIs and infrastructure for AI systems',
            backstory="Expert in Python, FastAPI, databases, and cloud deployment",
            verbose=True,
            llm=self.llm
        )
        
        devops_engineer = Agent(
            role='DevOps Engineer',
            goal='Ensure reliable deployment and monitoring of AI applications', 
            backstory="Expert in Docker, Kubernetes, CI/CD, and monitoring systems",
            verbose=True,
            llm=self.llm
        )
        
        # Tâches parallèles
        frontend_task = Task(
            description="""
            Design a user interface for an AI agent management dashboard.
            Include components for:
            1. Agent monitoring and status
            2. Task management and queues
            3. Performance metrics visualization
            4. User interaction history
            Provide detailed UI/UX specifications.
            """,
            agent=frontend_dev,
            expected_output="Complete UI/UX specification document"
        )
        
        backend_task = Task(
            description="""
            Design the backend architecture for an AI agent management system.
            Include:
            1. API endpoints and data models
            2. Database schema for agents, tasks, and results
            3. Authentication and authorization
            4. Scalability considerations
            Provide detailed technical specifications.
            """,
            agent=backend_dev,
            expected_output="Complete backend architecture document"
        )
        
        deployment_task = Task(
            description="""
            Create a deployment strategy for an AI agent platform.
            Include:
            1. Containerization with Docker
            2. Kubernetes orchestration
            3. CI/CD pipeline setup
            4. Monitoring and alerting strategy
            Provide step-by-step deployment guide.
            """,
            agent=devops_engineer,
            expected_output="Complete deployment strategy and guide"
        )
        
        # Équipe parallèle (note: CrewAI peut optimiser l'exécution)
        parallel_crew = Crew(
            agents=[frontend_dev, backend_dev, devops_engineer],
            tasks=[frontend_task, backend_task, deployment_task],
            process=Process.sequential,  # CrewAI optimise automatiquement
            verbose=True
        )
        
        print("\n🚀 Lancement de l'équipe de développement...")
        result = parallel_crew.kickoff()
        
        print(f"\n💻 Spécifications Techniques Complètes:")
        print("=" * 60)
        print(result)
        print("=" * 60)
        
        return result


def main():
    """Démonstration complète CrewAI"""
    
    print("⚓ CrewAI Teams Framework Demo")
    print("=" * 60)
    
    # Vérifier les prérequis
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY manquante!")
        print("   Ajoutez votre clé dans le fichier .env")
        return
    
    demo = CrewAIDemo()
    
    try:
        print("🎯 Choisissez une démo:")
        print("1. Équipe de Recherche (Researcher + Analyst + Writer)")
        print("2. Équipe Marketing (Market Research + Copy + Strategy)")
        print("3. Équipe Dev Parallèle (Frontend + Backend + DevOps)")
        print("4. Toutes les démos")
        
        choice = input("\n📝 Votre choix (1-4): ").strip()
        
        if choice == "1":
            demo.demo_research_crew()
        elif choice == "2":
            demo.demo_marketing_crew()
        elif choice == "3":
            demo.demo_parallel_crew()
        elif choice == "4":
            demo.demo_research_crew()
            demo.demo_marketing_crew()
            demo.demo_parallel_crew()
        else:
            print("❌ Choix invalide, lancement de la démo recherche par défaut")
            demo.demo_research_crew()
        
        print(f"\n🎉 Démonstrations CrewAI terminées!")
        print(f"\n💡 Points clés CrewAI:")
        print(f"   ✅ Agents avec rôles et backstories spécialisés")
        print(f"   ✅ Tâches séquentielles avec dépendances")
        print(f"   ✅ Collaboration naturelle entre agents")
        print(f"   ✅ Orchestration automatique des workflows")
        
    except KeyboardInterrupt:
        print(f"\n⏹️ Démo interrompue par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur pendant la démo: {e}")


if __name__ == "__main__":
    main()