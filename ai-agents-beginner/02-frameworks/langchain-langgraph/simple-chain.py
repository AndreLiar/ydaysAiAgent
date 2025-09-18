#!/usr/bin/env python3
"""
LangChain - Chaînes Simples et RAG Pipeline
Démonstration des patterns LangChain pour agents IA
"""

import os
from typing import Dict, List, Any
from dotenv import load_dotenv

# Dependencies: pip install langchain langchain-openai langchain-community chromadb
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

class LangChainDemo:
    """Démonstration des capacités LangChain essentielles"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            max_tokens=500
        )
        self.embeddings = OpenAIEmbeddings()
        
        print("🦜 LangChain Demo initialisé avec GPT-4")
    
    def demo_simple_chain(self):
        """Démonstration d'une chaîne LLM simple"""
        print("\n📋 DEMO 1: Chaîne Simple avec Prompt Template")
        print("=" * 50)
        
        # Template de prompt structuré
        template = """
        Tu es un expert en {domain} avec 10 ans d'expérience.
        
        Question: {question}
        
        Réponds de manière:
        1. Précise et technique
        2. Avec des exemples concrets
        3. En mentionnant les bonnes pratiques
        
        Réponse:
        """
        
        prompt = PromptTemplate(
            input_variables=["domain", "question"],
            template=template
        )
        
        # Créer la chaîne
        chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True  # Voir les étapes
        )
        
        # Tests avec différents domaines
        test_cases = [
            {
                "domain": "développement d'agents IA",
                "question": "Comment structurer une équipe d'agents collaboratifs?"
            },
            {
                "domain": "cybersécurité",  
                "question": "Quelles sont les vulnérabilités des agents IA?"
            }
        ]
        
        for i, test in enumerate(test_cases, 1):
            print(f"\n🧪 Test {i}: {test['domain']}")
            print(f"❓ Question: {test['question']}")
            
            response = chain.run(
                domain=test['domain'],
                question=test['question']
            )
            
            print(f"🎯 Réponse: {response[:200]}...")
            print("-" * 30)
    
    def demo_rag_pipeline(self):
        """Démonstration RAG (Retrieval-Augmented Generation)"""
        print("\n🔍 DEMO 2: Pipeline RAG Complet")
        print("=" * 50)
        
        # 1. Créer des documents de démonstration
        documents = [
            Document(
                page_content="""
                LangChain est un framework pour développer des applications alimentées par des modèles de langage.
                Il fournit des abstractions et des outils pour créer des chaînes complexes d'appels LLM,
                intégrer des sources de données externes, et gérer la mémoire conversationnelle.
                Les composants principaux incluent: Prompts, LLMs, Chains, Agents, et Memory.
                """,
                metadata={"source": "langchain_docs", "topic": "overview"}
            ),
            Document(
                page_content="""
                Les agents LangChain peuvent utiliser des outils pour interagir avec le monde extérieur.
                Ils suivent le pattern ReAct (Reasoning + Acting): observer, réfléchir, agir, répéter.
                Les agents peuvent utiliser des calculatrices, rechercher sur le web, accéder à des APIs,
                ou exécuter du code Python. L'agent décide quels outils utiliser selon le contexte.
                """,
                metadata={"source": "langchain_docs", "topic": "agents"}
            ),
            Document(
                page_content="""
                LangGraph est une extension de LangChain pour créer des workflows d'agents avec états.
                Il permet de définir des graphes de conversation où les agents peuvent passer 
                d'un état à l'autre selon les résultats. Idéal pour les workflows complexes
                nécessitant des points de décision, des boucles, ou des validations.
                """,
                metadata={"source": "langchain_docs", "topic": "langgraph"}
            ),
            Document(
                page_content="""
                CrewAI permet de créer des équipes d'agents spécialisés qui collaborent.
                Chaque agent a un rôle, des objectifs, et des outils spécifiques.
                L'orchestrateur coordonne les tâches entre agents selon leurs compétences.
                Parfait pour des projets nécessitant plusieurs expertise: recherche, analyse, écriture.
                """,
                metadata={"source": "frameworks_comparison", "topic": "crewai"}
            )
        ]
        
        # 2. Découper les documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )
        
        split_docs = text_splitter.split_documents(documents)
        print(f"📄 Documents découpés: {len(split_docs)} chunks")
        
        # 3. Créer le vector store
        vectorstore = Chroma.from_documents(
            documents=split_docs,
            embedding=self.embeddings,
            persist_directory="./langchain_demo_db"
        )
        
        print("🗂️ Base vectorielle créée")
        
        # 4. Créer le système RAG
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        
        rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )
        
        # 5. Tester le RAG
        questions = [
            "Quels sont les composants principaux de LangChain?",
            "Comment fonctionnent les agents avec des outils?", 
            "Quelle est la différence entre LangChain et CrewAI?",
            "Comment LangGraph gère-t-il les workflows complexes?"
        ]
        
        for i, question in enumerate(questions, 1):
            print(f"\n❓ Question {i}: {question}")
            
            result = rag_chain({"query": question})
            
            print(f"🎯 Réponse: {result['result'][:200]}...")
            
            # Afficher les sources
            sources = [doc.metadata.get('source', 'Unknown') for doc in result['source_documents']]
            print(f"📚 Sources: {', '.join(set(sources))}")
            print("-" * 40)
    
    def demo_memory_chain(self):
        """Démonstration des chaînes avec mémoire"""
        print("\n🧠 DEMO 3: Chaînes avec Mémoire Conversationnelle")
        print("=" * 50)
        
        # Créer une mémoire conversationnelle
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Template avec contexte de conversation
        template = """
        Tu es un assistant spécialisé en agents IA. Tu maintiens une conversation cohérente
        en gardant en mémoire ce qui a été dit précédemment.
        
        Historique de conversation:
        {chat_history}
        
        Question actuelle: {question}
        
        Réponse (cohérente avec l'historique):
        """
        
        prompt = PromptTemplate(
            input_variables=["chat_history", "question"],
            template=template
        )
        
        # Chaîne avec mémoire
        conversation_chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            memory=memory,
            verbose=True
        )
        
        # Conversation simulée
        conversation = [
            "Qu'est-ce qu'un agent IA?",
            "Peux-tu me donner des exemples concrets?",
            "Comment implémenter le pattern dont tu viens de parler?",
            "Quels sont les risques de cette approche?"
        ]
        
        for i, question in enumerate(conversation, 1):
            print(f"\n👤 Utilisateur {i}: {question}")
            
            response = conversation_chain.run(question=question)
            
            print(f"🤖 Assistant: {response[:300]}...")
            print("-" * 40)
        
        # Afficher l'historique final
        print("\n📚 Historique de la conversation:")
        print(memory.buffer)
    
    def cleanup(self):
        """Nettoyer les ressources temporaires"""
        import shutil
        try:
            shutil.rmtree("./langchain_demo_db")
            print("🗑️ Base vectorielle temporaire supprimée")
        except:
            pass


def main():
    """Démonstration complète LangChain"""
    
    print("🦜 LangChain Framework Demo")
    print("=" * 60)
    
    # Vérifier les prérequis
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY manquante!")
        print("   Ajoutez votre clé dans le fichier .env")
        return
    
    # Initialiser et lancer les demos
    demo = LangChainDemo()
    
    try:
        # Demo 1: Chaînes simples
        demo.demo_simple_chain()
        
        # Demo 2: RAG Pipeline
        demo.demo_rag_pipeline()
        
        # Demo 3: Mémoire conversationnelle
        demo.demo_memory_chain()
        
        print(f"\n🎉 Toutes les démos LangChain terminées!")
        print(f"\n💡 Points clés à retenir:")
        print(f"   ✅ Templates de prompts pour la cohérence")
        print(f"   ✅ RAG pour intégrer vos données privées")
        print(f"   ✅ Mémoire conversationnelle pour le contexte")
        print(f"   ✅ Chaînes composables pour la complexité")
        
    except Exception as e:
        print(f"❌ Erreur pendant la démo: {e}")
    
    finally:
        demo.cleanup()


if __name__ == "__main__":
    main()