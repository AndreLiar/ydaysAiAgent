# 🎯 Guide Étape par Étape - Système RAG avec LangChain/LangGraph

## 📚 Vue d'Ensemble du Projet

Ce guide vous accompagne dans la construction d'un **système RAG (Retrieval-Augmented Generation) complet** en utilisant LangChain et LangGraph. Vous apprendrez en faisant - chaque étape vous enseigne des concepts clés tout en construisant une application production-ready.

### 🎯 Objectifs d'Apprentissage
- Maîtriser les chaînes LangChain et l'écosystème
- Comprendre les workflows stateful avec LangGraph  
- Implémenter un pipeline RAG robuste
- Intégrer monitoring et observabilité
- Créer une application prête pour la production

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
pip install langchain langchain-openai langchain-community chromadb langgraph pypdf python-dotenv

# 2. Configurer votre clé API
cp .env.example .env
# Ajouter votre OPENAI_API_KEY dans le fichier .env

# 3. Lancer le projet starter
python my_rag_system_starter.py
```

## 📋 Progression Étape par Étape

### ✅ TODO 1: Installation des Dépendances (2 min)

**Concepts appris**: Écosystème LangChain et dépendances

```bash
pip install langchain langchain-openai langchain-community chromadb langgraph pypdf
```

**Pourquoi ces packages ?**
- `langchain`: Framework principal pour orchestrer les LLMs
- `langchain-openai`: Intégration OpenAI (GPT-4, embeddings)
- `langchain-community`: Loaders et outils communautaires
- `chromadb`: Base de données vectorielle pour les embeddings
- `langgraph`: Extension pour workflows complexes avec états
- `pypdf`: Lecture de documents PDF

### ✅ TODO 2: Imports et Architecture (3 min)

**Concepts appris**: Structure modulaire de LangChain

Décommentez et complétez les imports dans `my_rag_system_starter.py`:

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
```

**Architecture LangChain**:
- **Loaders**: Ingestion de documents (PDF, TXT, Web, etc.)
- **Text Splitters**: Découpage intelligent en chunks
- **Embeddings**: Vectorisation sémantique
- **Vector Stores**: Stockage et recherche vectorielle
- **Chains**: Orchestration de prompts et LLMs
- **Agents**: Entités autonomes avec outils

### ✅ TODO 3: État du Workflow LangGraph (5 min)

**Concepts appris**: Workflows stateful et gestion d'état

Définissez la classe `RAGWorkflowState`:

```python
class RAGWorkflowState(TypedDict):
    """État partagé du workflow RAG"""
    question: str              # Question de l'utilisateur
    documents: List[str]       # Documents récupérés
    context: str               # Contexte assemblé
    answer: str                # Réponse générée
    sources: List[str]         # Sources citées
    complexity_score: float    # Score de complexité (0-1)
    routing_decision: str      # Décision de routage (simple/complex)
    retrieval_count: int       # Nombre de documents récupérés
    processing_time: float     # Temps de traitement
```

**Pourquoi les États ?**
- **Persistence**: Maintenir le contexte entre les nœuds
- **Coordination**: Partager des données entre agents
- **Debugging**: Tracer l'évolution du workflow
- **Optimisation**: Éviter les recalculs inutiles

### ✅ TODO 4: Métriques et Monitoring (5 min)

**Concepts appris**: Observabilité en production

Complétez la classe `RAGMetrics`:

```python
@dataclass
class RAGMetrics:
    """Métriques de performance du système RAG"""
    timestamp: str
    query_id: str
    execution_time: float
    retrieval_time: float
    generation_time: float
    documents_retrieved: int
    context_length: int
    answer_length: int
    estimated_cost: float      # Coût estimé en tokens
    relevance_score: float     # Score de pertinence (0-1)
    user_satisfaction: Optional[float]  # Feedback utilisateur
    error_message: Optional[str]
    workflow_path: str         # Chemin pris dans le workflow
```

**Métriques Clés pour RAG**:
- **Performance**: Temps de réponse, latence
- **Qualité**: Pertinence, précision des sources
- **Coûts**: Utilisation tokens, appels API
- **Fiabilité**: Taux d'erreur, disponibilité

### ✅ TODO 5: Initialisation du Système (10 min)

**Concepts appris**: Configuration et initialisation des services

Implémentez l'initialisation dans `__init__`:

```python
def __init__(self):
    print("🚀 Initialisation de votre système RAG...")
    
    # Vérifier la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
    
    # Initialiser les services IA
    self.llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3,  # Responses plus déterministes
        max_tokens=1000
    )
    
    self.embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002"
    )
    
    # Variables d'instance
    self.vectorstore = None
    self.qa_chain = None
    self.workflow = None
    self.metrics = []
    
    print("✅ Configuration de base terminée")
```

**Bonnes Pratiques**:
- **Configuration centralisée**: Variables d'environnement
- **Validation précoce**: Vérifier les dépendances au démarrage
- **Logging structuré**: Messages informatifs pour debugging
- **Paramètres optimaux**: Temperature basse pour consistance

### ✅ TODO 6: Documents d'Exemple (Déjà fait ✅)

Le code crée automatiquement des documents d'exemple dans `./documents/` :
- `ai_guide.txt`: Guide Intelligence Artificielle
- `langchain_tutorial.txt`: Tutorial LangChain complet
- `business_case.txt`: Business case IA en entreprise

### ✅ TODO 7: Pipeline d'Ingestion (15 min)

**Concepts appris**: Pipeline RAG et traitement de documents

Implémentez `ingest_documents()`:

```python
def ingest_documents(self, docs_path: str = "./documents"):
    print(f"\n📚 ÉTAPE: Ingestion des documents depuis {docs_path}")
    print("=" * 60)
    
    # 1. Charger les documents
    documents = []
    docs_dir = Path(docs_path)
    
    for file_path in docs_dir.rglob("*"):
        if file_path.suffix.lower() == '.pdf':
            loader = PyPDFLoader(str(file_path))
            documents.extend(loader.load())
        elif file_path.suffix.lower() == '.txt':
            loader = TextLoader(str(file_path), encoding='utf-8')
            documents.extend(loader.load())
    
    if not documents:
        print("❌ Aucun document trouvé")
        return False
    
    print(f"📄 {len(documents)} documents chargés")
    
    # 2. Découper en chunks intelligents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,        # Taille optimale pour contexte
        chunk_overlap=200,      # Overlap pour continuité
        length_function=len,
        separators=["\n\n", "\n", " ", ""]  # Séparateurs logiques
    )
    
    splits = text_splitter.split_documents(documents)
    print(f"🔪 {len(splits)} chunks créés")
    
    # 3. Créer la base vectorielle
    self.vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=self.embeddings,
        persist_directory="./chroma_db"  # Persistence locale
    )
    
    print(f"🗄️ Base vectorielle créée avec {len(splits)} embeddings")
    print("✅ Ingestion terminée avec succès")
    return True
```

**Pipeline RAG Expliqué**:
1. **Loaders**: Extraction texte depuis différents formats
2. **Text Splitting**: Découpage en chunks cohérents
3. **Embeddings**: Vectorisation sémantique
4. **Vector Store**: Indexation pour recherche rapide

**Optimisations Importantes**:
- **Chunk size**: Balance entre contexte et précision
- **Overlap**: Éviter la perte d'information aux frontières
- **Séparateurs**: Respecter la structure logique du texte

### ✅ TODO 8: Chaîne RAG (10 min)

**Concepts appris**: Chaînes LangChain et prompts

Implémentez `create_rag_chain()`:

```python
def create_rag_chain(self):
    print("\n🔗 ÉTAPE: Création de la chaîne RAG")
    print("=" * 60)
    
    if not self.vectorstore:
        print("❌ Base vectorielle non initialisée")
        return False
    
    # Template de prompt personnalisé
    template = """Utilisez le contexte suivant pour répondre à la question.
Si l'information n'est pas dans le contexte, dites-le clairement.
Citez toujours vos sources avec des références spécifiques.

Contexte: {context}

Question: {question}

Instructions:
- Réponse détaillée et structurée
- Citations avec sources spécifiques
- Si information manquante, le mentionner
- Format professionnel

Réponse:"""
    
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )
    
    # Configurer le retriever
    retriever = self.vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}  # Top 4 documents les plus pertinents
    )
    
    # Créer la chaîne RetrievalQA
    self.qa_chain = RetrievalQA.from_chain_type(
        llm=self.llm,
        chain_type="stuff",  # Stratégie d'assemblage du contexte
        retriever=retriever,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True  # Retourner les sources
    )
    
    print("✅ Chaîne RAG créée avec succès")
    return True
```

**Types de Chaînes**:
- **stuff**: Concatène tous les documents (simple, limité par context window)
- **map_reduce**: Traite en parallèle puis synthétise (scalable)
- **refine**: Améliore itérativement la réponse (précis mais lent)

### ✅ TODO 9: Workflow LangGraph (20 min)

**Concepts appris**: Workflows complexes et routage conditionnel

Implémentez `create_langgraph_workflow()`:

```python
def create_langgraph_workflow(self):
    print("\n🔄 ÉTAPE: Création du workflow LangGraph")
    print("=" * 60)
    
    def analyze_query(state: RAGWorkflowState) -> RAGWorkflowState:
        """Analyser la complexité de la requête"""
        question = state["question"]
        
        # Analyse de complexité (vous pouvez améliorer cette logique)
        complexity_indicators = [
            len(question.split()) > 15,  # Question longue
            "compare" in question.lower(),
            "analyze" in question.lower(),
            "relationship" in question.lower(),
            "?" in question and question.count("?") > 1  # Questions multiples
        ]
        
        complexity_score = sum(complexity_indicators) / len(complexity_indicators)
        
        state["complexity_score"] = complexity_score
        state["routing_decision"] = "complex" if complexity_score > 0.4 else "simple"
        
        print(f"📊 Complexité analysée: {complexity_score:.2f} → {state['routing_decision']}")
        return state
    
    def simple_response(state: RAGWorkflowState) -> RAGWorkflowState:
        """Réponse simple et directe"""
        if not self.qa_chain:
            state["answer"] = "❌ Système RAG non initialisé"
            return state
        
        start_time = time.time()
        result = self.qa_chain.invoke({"query": state["question"]})
        
        state["answer"] = result["result"]
        state["sources"] = [doc.page_content[:100] + "..." for doc in result["source_documents"]]
        state["processing_time"] = time.time() - start_time
        
        print("✅ Réponse simple générée")
        return state
    
    def complex_response(state: RAGWorkflowState) -> RAGWorkflowState:
        """Réponse complexe avec recherche approfondie"""
        if not self.qa_chain:
            state["answer"] = "❌ Système RAG non initialisé"
            return state
        
        start_time = time.time()
        
        # Recherche plus approfondie pour questions complexes
        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 8}  # Plus de documents pour complexité
        )
        
        # Template spécialisé pour l'analyse complexe
        complex_template = """Analysez le contexte suivant pour fournir une réponse approfondie et nuancée.
        
Contexte: {context}
Question: {question}

Instructions pour analyse complexe:
- Examinez tous les aspects de la question
- Identifiez les relations et connexions
- Fournissez des exemples concrets
- Structurez votre réponse en sections claires
- Citez précisément vos sources

Analyse détaillée:"""
        
        # [Logique de traitement complexe ici]
        result = self.qa_chain.invoke({"query": state["question"]})
        
        state["answer"] = "🔍 ANALYSE APPROFONDIE:\n\n" + result["result"]
        state["sources"] = [doc.page_content[:150] + "..." for doc in result["source_documents"]]
        state["processing_time"] = time.time() - start_time
        
        print("✅ Analyse complexe générée")
        return state
    
    def decide_route(state: RAGWorkflowState) -> str:
        """Décider du chemin à suivre"""
        return state["routing_decision"]
    
    # Construire le graphe
    workflow = StateGraph(RAGWorkflowState)
    
    # Ajouter les nœuds
    workflow.add_node("analyze", analyze_query)
    workflow.add_node("simple", simple_response)
    workflow.add_node("complex", complex_response)
    
    # Définir les transitions
    workflow.set_entry_point("analyze")
    workflow.add_conditional_edges(
        "analyze",
        decide_route,
        {
            "simple": "simple",
            "complex": "complex"
        }
    )
    workflow.add_edge("simple", END)
    workflow.add_edge("complex", END)
    
    # Compiler le workflow
    self.workflow = workflow.compile()
    
    print("✅ Workflow LangGraph créé avec routage intelligent")
    return True
```

**Architecture LangGraph**:
```
Input → analyze → [simple/complex] → Output
         ↓
   Routage conditionnel
```

### ✅ TODO 10: Monitoring (15 min)

**Concepts appris**: Observabilité et métriques production

Implémentez `add_monitoring()`:

```python
def add_monitoring(self):
    print("\n📊 ÉTAPE: Configuration du monitoring")
    print("=" * 60)
    
    # Classe pour collecter les métriques
    class MetricsCollector:
        def __init__(self):
            self.metrics = []
        
        def collect_metrics(self, query_data):
            """Collecter les métriques d'une requête"""
            metrics = RAGMetrics(
                timestamp=datetime.now().isoformat(),
                query_id=str(hash(query_data.get("question", ""))),
                execution_time=query_data.get("processing_time", 0),
                retrieval_time=0,  # À implémenter
                generation_time=0,  # À implémenter
                documents_retrieved=len(query_data.get("sources", [])),
                context_length=len(query_data.get("context", "")),
                answer_length=len(query_data.get("answer", "")),
                estimated_cost=self.estimate_cost(query_data),
                relevance_score=0.95,  # Score mockup - à implémenter avec vraie évaluation
                user_satisfaction=None,
                error_message=None,
                workflow_path=query_data.get("routing_decision", "unknown")
            )
            
            self.metrics.append(metrics)
            return metrics
        
        def estimate_cost(self, query_data):
            """Estimer le coût en tokens"""
            # Estimation approximative (à améliorer)
            prompt_tokens = len(query_data.get("question", "").split()) * 1.3
            completion_tokens = len(query_data.get("answer", "").split()) * 1.3
            
            # Prix approximatifs GPT-4 (à jour au moment du développement)
            prompt_cost = prompt_tokens * 0.00003  # $0.03/1K tokens
            completion_cost = completion_tokens * 0.00006  # $0.06/1K tokens
            
            return prompt_cost + completion_cost
        
        def get_dashboard_data(self):
            """Générer des données pour dashboard"""
            if not self.metrics:
                return {"message": "Aucune métrique collectée"}
            
            total_queries = len(self.metrics)
            avg_time = sum(m.execution_time for m in self.metrics) / total_queries
            total_cost = sum(m.estimated_cost for m in self.metrics)
            
            return {
                "total_queries": total_queries,
                "average_response_time": f"{avg_time:.2f}s",
                "total_estimated_cost": f"${total_cost:.4f}",
                "success_rate": "100%",  # À calculer réellement
                "most_common_workflow": "simple"  # Analyser les routing_decisions
            }
    
    self.metrics_collector = MetricsCollector()
    
    print("✅ Système de monitoring configuré")
    print("📈 Métriques collectées: temps, coûts, performance, qualité")
    return True
```

### ✅ TODO 11: Fonction de Requête (10 min)

**Concepts appris**: Intégration de tous les composants

Implémentez `query()`:

```python
def query(self, question: str, use_workflow: bool = True) -> Dict[str, Any]:
    print(f"\n❓ REQUÊTE: {question}")
    print("=" * 60)
    
    start_time = datetime.now()
    
    try:
        if use_workflow and self.workflow:
            # Utiliser LangGraph workflow
            initial_state = {
                "question": question,
                "documents": [],
                "context": "",
                "answer": "",
                "sources": [],
                "complexity_score": 0.0,
                "routing_decision": "",
                "retrieval_count": 0,
                "processing_time": 0.0
            }
            
            result = self.workflow.invoke(initial_state)
            
            response = {
                "question": question,
                "answer": result["answer"],
                "sources": result["sources"],
                "execution_time": result.get("processing_time", 0),
                "workflow_used": True,
                "routing_decision": result.get("routing_decision", "unknown"),
                "complexity_score": result.get("complexity_score", 0),
                "timestamp": start_time.isoformat()
            }
            
        elif self.qa_chain:
            # Utiliser chaîne RAG simple
            chain_result = self.qa_chain.invoke({"query": question})
            execution_time = (datetime.now() - start_time).total_seconds()
            
            response = {
                "question": question,
                "answer": chain_result["result"],
                "sources": [doc.page_content[:100] + "..." for doc in chain_result["source_documents"]],
                "execution_time": execution_time,
                "workflow_used": False,
                "routing_decision": "simple_chain",
                "complexity_score": 0.5,
                "timestamp": start_time.isoformat()
            }
        else:
            response = {
                "question": question,
                "answer": "❌ Système non initialisé. Exécutez d'abord ingest_documents() et create_rag_chain()",
                "sources": [],
                "execution_time": 0,
                "workflow_used": False,
                "error": "System not initialized",
                "timestamp": start_time.isoformat()
            }
        
        # Collecter les métriques si le monitoring est configuré
        if hasattr(self, 'metrics_collector'):
            metrics = self.metrics_collector.collect_metrics(response)
            response["metrics"] = metrics
        
        print(f"✅ Réponse générée en {response['execution_time']:.2f}s")
        return response
        
    except Exception as e:
        error_response = {
            "question": question,
            "answer": f"❌ Erreur lors du traitement: {str(e)}",
            "sources": [],
            "execution_time": (datetime.now() - start_time).total_seconds(),
            "workflow_used": use_workflow,
            "error": str(e),
            "timestamp": start_time.isoformat()
        }
        
        print(f"❌ Erreur: {e}")
        return error_response
```

### ✅ TODO 12: Démonstration (5 min)

**Concepts appris**: Tests end-to-end

Implémentez `run_demo()`:

```python
def run_demo(self):
    print("\n🎬 DÉMONSTRATION DE VOTRE SYSTÈME RAG")
    print("=" * 60)
    
    # Questions de test progressives
    demo_questions = [
        "Qu'est-ce que LangChain et comment ça fonctionne?",
        "Quels sont les avantages business de l'IA en entreprise?", 
        "Comment implémenter un système RAG avec monitoring?",
        "Quelles sont les tendances IA pour 2024 et leur impact sur les entreprises?",
        "Compare LangChain et LangGraph pour des applications complexes avec exemples concrets"
    ]
    
    print("🎯 Questions de démonstration:")
    for i, q in enumerate(demo_questions, 1):
        print(f"  {i}. {q}")
    
    print("\n" + "="*60)
    
    # Exécuter les questions et afficher les résultats
    for i, question in enumerate(demo_questions, 1):
        print(f"\n💡 QUESTION {i}: {question}")
        print("-" * 50)
        
        result = self.query(question)
        
        print(f"📝 RÉPONSE:")
        print(result['answer'])
        print(f"\n📚 SOURCES: {len(result['sources'])} documents utilisés")
        print(f"⏱️ TEMPS: {result['execution_time']:.2f}s")
        print(f"🔄 WORKFLOW: {result.get('routing_decision', 'N/A')}")
        
        if i < len(demo_questions):
            print("\n" + "-"*30 + " SUIVANT " + "-"*30)
    
    # Afficher les métriques globales
    if hasattr(self, 'metrics_collector'):
        dashboard = self.metrics_collector.get_dashboard_data()
        print(f"\n📊 MÉTRIQUES GLOBALES:")
        print(f"   Total requêtes: {dashboard['total_queries']}")
        print(f"   Temps moyen: {dashboard['average_response_time']}")
        print(f"   Coût estimé: {dashboard['total_estimated_cost']}")
    
    print("\n✅ Démonstration terminée avec succès!")
```

### ✅ TODO 13: Sauvegarde des Métriques (5 min)

**Concepts appris**: Persistance des données

Implémentez `save_metrics()`:

```python
def save_metrics(self):
    if not hasattr(self, 'metrics_collector') or not self.metrics_collector.metrics:
        print("📊 Aucune métrique à sauvegarder")
        return
    
    # Préparer les données pour JSON
    metrics_data = {
        "session_info": {
            "timestamp": datetime.now().isoformat(),
            "total_queries": len(self.metrics_collector.metrics),
            "system_version": "1.0.0"
        },
        "metrics": [
            {
                "timestamp": m.timestamp,
                "query_id": m.query_id,
                "execution_time": m.execution_time,
                "documents_retrieved": m.documents_retrieved,
                "estimated_cost": m.estimated_cost,
                "workflow_path": m.workflow_path,
                "answer_length": m.answer_length
            }
            for m in self.metrics_collector.metrics
        ],
        "summary": self.metrics_collector.get_dashboard_data()
    }
    
    # Sauvegarder dans metrics.json
    with open("metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics_data, f, indent=2, ensure_ascii=False)
    
    print("✅ Métriques sauvegardées dans metrics.json")
```

## 🎯 Résultat Final

Après avoir complété tous les TODOs, vous aurez créé :

### 📁 Fichiers Générés
- ✅ `./documents/` - Documents d'exemple
- ✅ `./chroma_db/` - Base vectorielle persistante  
- ✅ `metrics.json` - Métriques de performance

### 🎓 Compétences Acquises
- **LangChain**: Chaînes, prompts, loaders, embeddings
- **LangGraph**: Workflows stateful, routage conditionnel
- **RAG**: Pipeline complet d'ingestion à génération
- **Monitoring**: Métriques, observabilité, coûts
- **Production**: Gestion d'erreurs, persistence, configuration

### 🚀 Applications Possibles
- Chatbot d'entreprise avec base de connaissances
- Assistant de recherche documentaire
- Système de Q&A pour support client
- Outil d'analyse de documents réglementaires

## 🎬 Démonstration

Lancez votre système terminé :

```bash
python my_rag_system_starter.py
```

Le système exécutera automatiquement :
1. ✅ Création des documents d'exemple
2. ✅ Ingestion dans la base vectorielle
3. ✅ Configuration des chaînes et workflows
4. ✅ Démonstration avec 5 questions test
5. ✅ Affichage des métriques de performance

## 🔧 Personnalisation

### Adapter à Votre Domaine
1. **Documents**: Remplacez le contenu de `./documents/`
2. **Prompts**: Modifiez les templates pour votre use case
3. **Métriques**: Ajoutez des KPIs spécifiques à votre métier
4. **Workflow**: Adaptez la logique de routage

### Optimisations Avancées
1. **Performance**: Caching, embeddings optimisés
2. **Qualité**: Évaluation automatique, feedback loops
3. **Coûts**: Optimisation des prompts, modèles locaux
4. **Scalabilité**: Base vectorielle distribuée, load balancing

## 🏆 Validation des Acquis

Vous maîtrisez le projet si vous pouvez :
- [ ] Expliquer le pipeline RAG end-to-end
- [ ] Modifier les prompts pour votre domaine
- [ ] Ajouter de nouveaux types de documents
- [ ] Comprendre les métriques de performance
- [ ] Adapter le routage LangGraph

## 🔗 Ressources pour Aller Plus Loin

- [LangChain Documentation](https://docs.langchain.com/)
- [LangGraph Tutorials](https://langchain-ai.github.io/langgraph/)
- [RAG Best Practices](https://docs.langchain.com/docs/use-cases/question-answering)
- [Production Deployment](https://docs.langchain.com/docs/guides/deployments)

---

🎯 **Félicitations !** Vous avez construit un système RAG production-ready et maîtrisé LangChain/LangGraph !