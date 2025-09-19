#!/usr/bin/env python3
"""
🎯 PROJET RAG SYSTEM - STARTER TEMPLATE
Apprenez LangChain et LangGraph en construisant un système RAG complet !

📚 Ce fichier est votre template de démarrage. Suivez les TODO pour apprendre.
🚀 À la fin, vous aurez un système RAG production-ready avec monitoring.

Temps estimé: 45 minutes
Difficulté: ⭐⭐⭐⭐ (Avancé)
"""

import os
from typing import Dict, List, Any, Optional, TypedDict, Annotated
from datetime import datetime
from dataclasses import dataclass
from pathlib import Path

# TODO 1: Installer les dépendances
# pip install langchain langchain-openai langchain-community chromadb langgraph pypdf

# TODO 2: Importer les modules nécessaires
# 💡 APPRENTISSAGE: Comprendre l'écosystème LangChain
from dotenv import load_dotenv
# Ajouter vos imports ici:
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langgraph.graph import StateGraph, END
# from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

# TODO 3: Définir l'état du workflow LangGraph
# 💡 APPRENTISSAGE: Les workflows stateful avec LangGraph
class RAGWorkflowState(TypedDict):
    """État partagé du workflow RAG"""
    # Définir les variables d'état ici
    pass

# TODO 4: Créer une classe pour collecter les métriques
# 💡 APPRENTISSAGE: Monitoring et observabilité en production
@dataclass
class RAGMetrics:
    """Métriques de performance du système RAG"""
    # Ajouter les champs de métriques ici
    pass

class MyRAGSystem:
    """
    🎯 VOTRE SYSTÈME RAG COMPLET
    
    Objectifs d'apprentissage:
    1. 🔗 Maîtriser les chaînes LangChain
    2. 📄 Implémenter un pipeline RAG robuste
    3. 🔄 Créer des workflows LangGraph avec états
    4. 📊 Intégrer monitoring et métriques
    5. 🛡️ Gérer les erreurs et la production
    """
    
    def __init__(self):
        """
        TODO 5: Initialiser votre système RAG
        💡 APPRENTISSAGE: Configuration des services LangChain
        
        À faire:
        - Configurer ChatOpenAI avec votre clé API
        - Configurer OpenAIEmbeddings
        - Initialiser les variables d'instance
        - Préparer le système de métriques
        """
        print("🚀 Initialisation de votre système RAG...")
        
        # Vérifier la clé API
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
        
        # TODO: Initialiser vos services IA ici
        # self.llm = ...
        # self.embeddings = ...
        # self.vectorstore = None
        # self.workflow = None
        # self.metrics = []
        
        print("✅ Configuration de base terminée")
    
    def create_documents_folder(self):
        """
        TODO 6: Préparer les documents d'exemple
        💡 APPRENTISSAGE: Gestion des données pour RAG
        """
        docs_dir = Path("./documents")
        docs_dir.mkdir(exist_ok=True)
        
        # Créer des documents d'exemple si le dossier est vide
        if not any(docs_dir.iterdir()):
            sample_docs = {
                "ai_guide.txt": """
# Guide Intelligence Artificielle

L'Intelligence Artificielle (IA) révolutionne notre monde. Ce guide couvre:

## 1. Fondamentaux de l'IA
- Machine Learning: apprentissage automatique à partir de données
- Deep Learning: réseaux de neurones profonds
- NLP: traitement du langage naturel

## 2. Applications Pratiques
- Chatbots et assistants virtuels
- Reconnaissance d'images
- Traduction automatique
- Véhicules autonomes

## 3. Frameworks Populaires
- LangChain: orchestration d'agents IA
- AutoGen: conversations multi-agents
- CrewAI: équipes collaboratives
- Semantic Kernel: approche Microsoft

## 4. Tendances 2024
- Agents autonomes
- Multimodalité (texte + image + audio)
- IA générative personnalisée
- Intégration enterprise
""",
                "langchain_tutorial.txt": """
# LangChain Tutorial Complet

## Qu'est-ce que LangChain?
LangChain est un framework pour développer des applications avec des LLMs.

## Concepts Clés
1. **Chains**: Séquences d'appels aux LLMs
2. **Agents**: Entités qui utilisent des outils
3. **Memory**: Maintien du contexte
4. **Retrieval**: RAG et recherche d'informations

## RAG (Retrieval-Augmented Generation)
Le RAG combine:
- Base de connaissances (documents)
- Recherche sémantique (embeddings)
- Génération de réponses (LLM)

## LangGraph
Extension pour workflows complexes:
- États partagés
- Routage conditionnel
- Workflows cycliques
- Checkpointing
""",
                "business_case.txt": """
# Business Case: IA en Entreprise

## Contexte
Les entreprises adoptent massivement l'IA pour:
- Réduire les coûts opérationnels
- Améliorer l'expérience client
- Accélérer l'innovation

## ROI de l'IA
Études montrent un ROI moyen de 300% sur 3 ans:
- 40% réduction temps traitement
- 60% amélioration satisfaction client
- 25% augmentation revenus

## Cas d'Usage Prioritaires
1. **Support Client**: Chatbots intelligents
2. **Analyse Documents**: Extraction automatique
3. **Veille Concurrentielle**: Monitoring automatisé
4. **Génération Contenu**: Marketing personnalisé

## Défis Implementation
- Formation des équipes
- Intégration systèmes existants
- Gouvernance des données
- Changement culturel
"""
            }
            
            for filename, content in sample_docs.items():
                (docs_dir / filename).write_text(content, encoding='utf-8')
            
            print(f"📄 {len(sample_docs)} documents d'exemple créés dans ./documents/")
        
        return docs_dir
    
    def ingest_documents(self, docs_path: str = "./documents"):
        """
        TODO 7: Implémenter l'ingestion de documents
        💡 APPRENTISSAGE: Pipeline de traitement de documents pour RAG
        
        Étapes à implémenter:
        1. Charger les documents (PDF, TXT)
        2. Découper en chunks intelligents
        3. Créer les embeddings
        4. Stocker dans la base vectorielle
        
        Concepts clés:
        - DocumentLoaders: PyPDFLoader, TextLoader
        - TextSplitter: RecursiveCharacterTextSplitter
        - VectorStore: Chroma
        - Embeddings: OpenAIEmbeddings
        """
        print(f"\n📚 ÉTAPE: Ingestion des documents depuis {docs_path}")
        print("=" * 60)
        
        # TODO: Implémenter votre pipeline d'ingestion
        # 1. Charger les documents
        # 2. Découper en chunks
        # 3. Créer embeddings
        # 4. Stocker dans Chroma
        
        # Exemple de structure:
        # documents = []
        # for file_path in Path(docs_path).rglob("*"):
        #     if file_path.suffix.lower() in ['.pdf', '.txt']:
        #         # Charger le document
        #         # documents.extend(loaded_docs)
        
        # text_splitter = RecursiveCharacterTextSplitter(...)
        # splits = text_splitter.split_documents(documents)
        
        # self.vectorstore = Chroma.from_documents(...)
        
        print("✅ TODO 7: Implémentez l'ingestion de documents")
        return False  # Changer en True quand implémenté
    
    def create_rag_chain(self):
        """
        TODO 8: Créer la chaîne RAG
        💡 APPRENTISSAGE: Chaînes LangChain et templates de prompts
        
        Concepts:
        - PromptTemplate avec variables
        - RetrievalQA chain
        - Retriever configuration
        - Custom prompts pour votre domaine
        """
        print("\n🔗 ÉTAPE: Création de la chaîne RAG")
        print("=" * 60)
        
        # TODO: Créer votre template de prompt personnalisé
        # template = """
        # Utilisez le contexte suivant pour répondre à la question.
        # Si l'information n'est pas dans le contexte, dites-le clairement.
        # 
        # Contexte: {context}
        # Question: {question}
        # 
        # Réponse détaillée:
        # """
        
        # TODO: Configurer le retriever
        # retriever = self.vectorstore.as_retriever(...)
        
        # TODO: Créer la chaîne RetrievalQA
        # self.qa_chain = RetrievalQA.from_chain_type(...)
        
        print("✅ TODO 8: Implémentez la chaîne RAG")
        return False
    
    def create_langgraph_workflow(self):
        """
        TODO 9: Créer le workflow LangGraph
        💡 APPRENTISSAGE: Workflows stateful et routage conditionnel
        
        Architecture du workflow:
        Input → Analyze → Route → [Simple/Complex] → Output
        
        Concepts:
        - StateGraph: graphe d'états
        - Nodes: fonctions de traitement
        - Edges: transitions entre nœuds
        - Conditional routing: routage intelligent
        """
        print("\n🔄 ÉTAPE: Création du workflow LangGraph")
        print("=" * 60)
        
        # TODO: Définir les fonctions de nœuds
        def analyze_query(state: RAGWorkflowState) -> RAGWorkflowState:
            """Analyser la complexité de la requête"""
            # Implémenter l'analyse de la requête
            pass
        
        def simple_response(state: RAGWorkflowState) -> RAGWorkflowState:
            """Réponse simple et directe"""
            # Implémenter la logique de réponse simple
            pass
        
        def complex_response(state: RAGWorkflowState) -> RAGWorkflowState:
            """Réponse complexe avec recherche approfondie"""
            # Implémenter la logique de réponse complexe
            pass
        
        def decide_route(state: RAGWorkflowState) -> str:
            """Décider du chemin à suivre"""
            # Implémenter la logique de routage
            return "simple"  # ou "complex"
        
        # TODO: Construire le graphe
        # workflow = StateGraph(RAGWorkflowState)
        # workflow.add_node("analyze", analyze_query)
        # workflow.add_node("simple", simple_response)
        # workflow.add_node("complex", complex_response)
        # workflow.set_entry_point("analyze")
        # workflow.add_conditional_edges("analyze", decide_route, {...})
        # workflow.add_edge("simple", END)
        # workflow.add_edge("complex", END)
        
        # self.workflow = workflow.compile()
        
        print("✅ TODO 9: Implémentez le workflow LangGraph")
        return False
    
    def add_monitoring(self):
        """
        TODO 10: Ajouter le monitoring
        💡 APPRENTISSAGE: Observabilité et métriques en production
        
        Métriques à tracker:
        - Temps de réponse
        - Scores de pertinence
        - Utilisation des tokens
        - Taux d'erreur
        - Coûts estimés
        """
        print("\n📊 ÉTAPE: Configuration du monitoring")
        print("=" * 60)
        
        # TODO: Implémenter la collecte de métriques
        # - Callbacks LangChain pour tracking
        # - Calcul des coûts
        # - Logs structurés
        # - Dashboard simple
        
        print("✅ TODO 10: Implémentez le monitoring")
        return False
    
    def query(self, question: str, use_workflow: bool = True) -> Dict[str, Any]:
        """
        TODO 11: Implémenter la fonction de requête principale
        💡 APPRENTISSAGE: Intégration de tous les composants
        
        Cette fonction doit:
        1. Valider l'entrée
        2. Exécuter via workflow ou chaîne simple
        3. Collecter les métriques
        4. Retourner le résultat structuré
        """
        print(f"\n❓ REQUÊTE: {question}")
        print("=" * 60)
        
        start_time = datetime.now()
        
        # TODO: Implémenter la logique de requête
        # if use_workflow and self.workflow:
        #     # Utiliser LangGraph workflow
        #     result = self.workflow.invoke({"question": question})
        # elif self.qa_chain:
        #     # Utiliser chaîne RAG simple
        #     result = self.qa_chain.invoke({"query": question})
        # else:
        #     return {"error": "Système non initialisé"}
        
        # Calculer les métriques
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # TODO: Structurer la réponse
        response = {
            "question": question,
            "answer": "TODO: Implémenter la génération de réponse",
            "sources": [],
            "execution_time": execution_time,
            "workflow_used": use_workflow,
            "timestamp": start_time.isoformat()
        }
        
        print("✅ TODO 11: Implémentez la fonction de requête")
        return response
    
    def run_demo(self):
        """
        TODO 12: Créer une démonstration complète
        💡 APPRENTISSAGE: Test end-to-end du système
        """
        print("\n🎬 DÉMONSTRATION DE VOTRE SYSTÈME RAG")
        print("=" * 60)
        
        # Questions de test
        demo_questions = [
            "Qu'est-ce que LangChain et comment ça fonctionne?",
            "Quels sont les avantages business de l'IA en entreprise?",
            "Comment implémenter un système RAG?",
            "Quelles sont les tendances IA pour 2024?",
            "Quelle est la différence entre LangChain et LangGraph?"
        ]
        
        print("🎯 Questions de démonstration:")
        for i, q in enumerate(demo_questions, 1):
            print(f"  {i}. {q}")
        
        # TODO: Exécuter les questions et afficher les résultats
        # for question in demo_questions:
        #     result = self.query(question)
        #     print(f"\n💡 {question}")
        #     print(f"📝 {result['answer']}")
        #     print(f"⏱️ Temps: {result['execution_time']:.2f}s")
        
        print("\n✅ TODO 12: Implémentez la démonstration")
    
    def save_metrics(self):
        """
        TODO 13: Sauvegarder les métriques
        💡 APPRENTISSAGE: Persistance des données de monitoring
        """
        # TODO: Sauvegarder dans metrics.json
        pass

def main():
    """
    🎯 FONCTION PRINCIPALE - VOTRE PARCOURS D'APPRENTISSAGE
    
    Suivez cette progression pour maîtriser LangChain/LangGraph:
    """
    print("🚀 BIENVENUE DANS VOTRE PROJET RAG SYSTEM !")
    print("=" * 60)
    print("📚 Vous allez apprendre en construisant un système complet")
    print("🎯 Objectif: Système RAG production-ready avec monitoring")
    print("⏱️ Temps estimé: 45 minutes")
    print("\n📋 PROGRESSION:")
    print("  1. ✅ Configuration de base")
    print("  2. 📄 Ingestion de documents")
    print("  3. 🔗 Chaîne RAG")
    print("  4. 🔄 Workflow LangGraph")
    print("  5. 📊 Monitoring")
    print("  6. 🎬 Démonstration")
    
    try:
        # Initialiser le système
        rag_system = MyRAGSystem()
        
        # Étape 1: Préparer les documents
        rag_system.create_documents_folder()
        
        # Étape 2: Message d'encouragement
        print("\n🎓 PRÊT À COMMENCER ?")
        print("👆 Suivez les TODO dans le code pour apprendre !")
        print("💡 Chaque TODO vous enseigne un concept important")
        
        # TODO: Décommenter quand vous avez implémenté les méthodes
        # rag_system.ingest_documents()
        # rag_system.create_rag_chain()
        # rag_system.create_langgraph_workflow()
        # rag_system.add_monitoring()
        # rag_system.run_demo()
        # rag_system.save_metrics()
        
        print("\n🏆 Quand vous aurez terminé tous les TODO:")
        print("   - Vous maîtriserez LangChain/LangGraph")
        print("   - Vous aurez un système RAG production-ready")
        print("   - Vous comprendrez le monitoring IA")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        print("💡 Vérifiez votre configuration (clé API, dépendances)")

if __name__ == "__main__":
    main()