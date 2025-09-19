# 🎯 Guide Étape par Étape - Agent Intelligent avec Semantic Kernel

## 📚 Vue d'Ensemble du Projet

Ce guide vous accompagne dans la construction d'un **agent intelligent avec mémoire** en utilisant Semantic Kernel. Vous apprendrez en faisant - chaque étape vous enseigne des concepts clés tout en construisant un assistant personnel avec planification automatique.

### 🎯 Objectifs d'Apprentissage
- Maîtriser les concepts Semantic Kernel
- Créer et intégrer des plugins personnalisés
- Implémenter une mémoire persistante
- Utiliser la planification automatique
- Construire un assistant adaptatif

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
pip install semantic-kernel openai python-dotenv

# 2. Configurer votre clé API
cp .env.example .env
# Ajouter votre OPENAI_API_KEY dans le fichier .env

# 3. Lancer le projet starter
python my_intelligent_agent_starter.py
```

## 📋 Progression Étape par Étape

### ✅ TODO 1: Installation des Dépendances (2 min)

**Concepts appris**: Écosystème Semantic Kernel et architecture Microsoft

```bash
pip install semantic-kernel openai python-dotenv
```

**Pourquoi ces packages ?**
- `semantic-kernel`: Framework principal Microsoft pour agents IA
- `openai`: Intégration OpenAI (GPT-4) pour les fonctions sémantiques
- `python-dotenv`: Gestion sécurisée des configurations

### ✅ TODO 2: Imports et Architecture (3 min)

**Concepts appris**: Structure modulaire de Semantic Kernel

Décommentez et complétez les imports dans `my_intelligent_agent_starter.py`:

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.planning import BasicPlanner
from semantic_kernel.memory import SemanticTextMemory
from semantic_kernel.connectors.ai.open_ai import OpenAITextEmbedding
```

**Architecture Semantic Kernel**:
- **Kernel**: Orchestrateur central du système
- **Functions**: Fonctions natives et sémantiques
- **Plugins**: Collections de fonctions réutilisables
- **Planner**: Orchestration automatique multi-étapes
- **Memory**: Stockage sémantique persistant

### ✅ TODO 3: État de l'Agent (5 min)

**Concepts appris**: Mémoire et préférences utilisateur

Définissez la classe `AgentState`:

```python
@dataclass
class AgentState:
    """État persistant de l'agent intelligent"""
    created_at: str
    last_interaction: Optional[str]
    user_name: Optional[str]
    communication_style: str = "professional"  # professional/casual/formal
    notification_time: str = "09:00"           # Heure préférée
    task_priority: str = "high"                # high/medium/low
    language: str = "fr"                       # Langue préférée
    timezone: str = "Europe/Paris"             # Fuseau horaire
    interests: List[str] = None                # Centres d'intérêt
    work_context: Optional[str] = None         # Contexte professionnel
    learning_preferences: List[str] = None     # Style d'apprentissage
    conversation_count: int = 0                # Nombre de conversations
    
    def __post_init__(self):
        if self.interests is None:
            self.interests = []
        if self.learning_preferences is None:
            self.learning_preferences = ["visual", "practical"]
```

**Pourquoi cet État ?**
- **Personnalisation**: Adaptation aux préférences utilisateur
- **Persistance**: Mémoire entre sessions
- **Contextualisation**: Réponses adaptées au profil
- **Évolution**: Apprentissage continu des habitudes

### ✅ TODO 4: Système de Plugins (8 min)

**Concepts appris**: Extensibilité avec plugins Semantic Kernel

Complétez la classe `PluginRegistry`:

```python
class PluginRegistry:
    """Registre de plugins personnalisés"""
    
    def __init__(self):
        self.plugins = {}
    
    def create_time_plugin(self):
        """Plugin pour gestion du temps"""
        
        @sk_function(
            description="Get the current date and time",
            name="get_current_time"
        )
        def get_current_time() -> str:
            """Obtenir la date et heure actuelles"""
            from datetime import datetime
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        @sk_function(
            description="Calculate time difference between two dates",
            name="calculate_time_diff"
        )
        def calculate_time_diff(date1: str, date2: str) -> str:
            """Calculer la différence entre deux dates"""
            try:
                from datetime import datetime
                d1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
                d2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
                diff = abs((d2 - d1).total_seconds())
                
                hours = int(diff // 3600)
                minutes = int((diff % 3600) // 60)
                return f"{hours}h {minutes}m"
            except Exception as e:
                return f"Erreur de calcul: {e}"
        
        @sk_function(
            description="Schedule a reminder for a specific time",
            name="schedule_reminder"
        )
        def schedule_reminder(message: str, time: str) -> str:
            """Programmer un rappel"""
            # En production: intégration avec système de notifications
            return f"Rappel programmé: '{message}' à {time}"
        
        return {
            "get_current_time": get_current_time,
            "calculate_time_diff": calculate_time_diff,
            "schedule_reminder": schedule_reminder
        }
    
    def create_preference_plugin(self):
        """Plugin pour gestion des préférences"""
        
        @sk_function(
            description="Update user preference for a specific setting",
            name="update_preference"
        )
        def update_preference(preference_type: str, value: str) -> str:
            """Mettre à jour une préférence utilisateur"""
            valid_prefs = [
                "communication_style", "notification_time", 
                "task_priority", "language", "timezone"
            ]
            
            if preference_type in valid_prefs:
                # En production: sauvegarder dans la mémoire persistante
                return f"Préférence '{preference_type}' mise à jour: {value}"
            else:
                return f"Type de préférence invalide. Valides: {', '.join(valid_prefs)}"
        
        @sk_function(
            description="Get current user preferences",
            name="get_preferences"
        )
        def get_preferences() -> str:
            """Obtenir les préférences actuelles"""
            # En production: charger depuis la mémoire
            return "Préférences: Style professionnel, notifications 9h, priorité haute"
        
        @sk_function(
            description="Add user interest or expertise area",
            name="add_interest"
        )
        def add_interest(interest: str) -> str:
            """Ajouter un centre d'intérêt"""
            return f"Centre d'intérêt ajouté: {interest}"
        
        return {
            "update_preference": update_preference,
            "get_preferences": get_preferences,
            "add_interest": add_interest
        }
    
    def create_task_plugin(self):
        """Plugin pour gestion des tâches"""
        
        @sk_function(
            description="Create a new task with priority and deadline",
            name="create_task"
        )
        def create_task(title: str, priority: str = "medium", deadline: str = "") -> str:
            """Créer une nouvelle tâche"""
            task_id = hash(title + str(datetime.now())) % 10000
            return f"Tâche créée: {title} (ID: {task_id}, Priorité: {priority})"
        
        @sk_function(
            description="List all pending tasks",
            name="list_tasks"
        )
        def list_tasks() -> str:
            """Lister les tâches en cours"""
            # En production: récupérer depuis la mémoire
            return "Tâches en cours: 1. Projet IA (haute), 2. Rapport (moyenne)"
        
        @sk_function(
            description="Mark a task as completed",
            name="complete_task"
        )
        def complete_task(task_id: str) -> str:
            """Marquer une tâche comme terminée"""
            return f"Tâche {task_id} marquée comme terminée"
        
        return {
            "create_task": create_task,
            "list_tasks": list_tasks,
            "complete_task": complete_task
        }
```

**Concepts Clés Plugins**:
- **@sk_function**: Décorateur pour fonctions natives
- **description**: Description pour le planner automatique
- **name**: Nom unique de la fonction
- **Type hints**: Important pour l'inférence automatique

### ✅ TODO 5: Initialisation du Système (10 min)

**Concepts appris**: Configuration Semantic Kernel

Implémentez l'initialisation dans `__init__`:

```python
def __init__(self):
    print("🚀 Initialisation de votre agent intelligent...")
    
    # Vérifier la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
    
    # Créer le kernel Semantic Kernel
    self.kernel = sk.Kernel()
    
    # Configurer le service AI pour chat completion
    self.kernel.add_text_completion_service(
        "gpt-4-completion",
        OpenAIChatCompletion("gpt-4", api_key, org_id=None)
    )
    
    # Configurer les embeddings pour la mémoire
    self.kernel.add_text_embedding_generation_service(
        "text-embedding-ada-002",
        OpenAITextEmbedding("text-embedding-ada-002", api_key)
    )
    
    # Initialiser la mémoire sémantique
    self.kernel.register_memory_store(SemanticTextMemory(
        storage=sk.memory.VolatileMemoryStore(),  # En production: persistant
        embeddings_generator=self.kernel.get_service("text-embedding-ada-002")
    ))
    
    # Initialiser vos variables d'instance
    self.plugins = PluginRegistry()
    self.planner = None
    self.agent_state = AgentState(
        created_at=datetime.now().isoformat(),
        conversation_count=0
    )
    self.conversation_history = []
    
    print("✅ Configuration de base terminée")
    print("🧠 Kernel initialisé avec services AI")
    print("💾 Mémoire sémantique configurée")
```

**Bonnes Pratiques Semantic Kernel**:
- **Services séparés**: Completion et embeddings distincts
- **Memory store**: Stockage vectoriel pour recherche sémantique
- **Service registration**: Enregistrement propre des services
- **Error handling**: Validation des prérequis

### ✅ TODO 6: Plugins Personnalisés (15 min)

**Concepts appris**: Système de plugins Semantic Kernel

Implémentez `create_custom_plugins()`:

```python
def create_custom_plugins(self):
    print("\n🔌 ÉTAPE: Création de plugins personnalisés")
    print("=" * 60)
    
    # Créer le plugin Time
    time_functions = self.plugins.create_time_plugin()
    time_plugin = self.kernel.import_plugin_from_object(
        time_functions, 
        plugin_name="TimePlugin"
    )
    
    # Créer le plugin Preference
    pref_functions = self.plugins.create_preference_plugin()
    pref_plugin = self.kernel.import_plugin_from_object(
        pref_functions,
        plugin_name="PreferencePlugin"
    )
    
    # Créer le plugin Task
    task_functions = self.plugins.create_task_plugin()
    task_plugin = self.kernel.import_plugin_from_object(
        task_functions,
        plugin_name="TaskPlugin"
    )
    
    # Créer un plugin Weather simple (exemple)
    @sk_function(
        description="Get weather information for a location",
        name="get_weather"
    )
    def get_weather(location: str) -> str:
        """Obtenir la météo d'un lieu"""
        # Simulation - en production: appel API météo réelle
        return f"Météo à {location}: Ensoleillé, 22°C"
    
    weather_plugin = self.kernel.import_plugin_from_object(
        {"get_weather": get_weather},
        plugin_name="WeatherPlugin"
    )
    
    # Créer un plugin de calcul
    @sk_function(
        description="Perform basic mathematical calculations",
        name="calculate"
    )
    def calculate(expression: str) -> str:
        """Effectuer des calculs mathématiques"""
        try:
            # Sécurisé: seulement opérations de base
            allowed_chars = set("0123456789+-*/.() ")
            if all(c in allowed_chars for c in expression):
                result = eval(expression)
                return f"Résultat: {result}"
            else:
                return "Expression non autorisée"
        except Exception as e:
            return f"Erreur de calcul: {e}"
    
    calc_plugin = self.kernel.import_plugin_from_object(
        {"calculate": calculate},
        plugin_name="CalculatorPlugin"
    )
    
    print("✅ Plugins créés avec succès:")
    print("   🕒 TimePlugin - Gestion du temps et rappels")
    print("   ⚙️ PreferencePlugin - Préférences utilisateur")
    print("   📋 TaskPlugin - Gestion des tâches")
    print("   🌤️ WeatherPlugin - Informations météo")
    print("   🔢 CalculatorPlugin - Calculs mathématiques")
    
    return True
```

**Patterns d'Plugins**:
- **Plugin grouping**: Fonctions liées regroupées
- **Naming convention**: Noms descriptifs et cohérents
- **Error handling**: Gestion robuste des erreurs
- **Security**: Validation des entrées utilisateur

### ✅ TODO 7: Mémoire Sémantique (12 min)

**Concepts appris**: Mémoire persistante et recherche sémantique

Implémentez `setup_semantic_memory()`:

```python
async def setup_semantic_memory(self):
    print("\n🧠 ÉTAPE: Configuration de la mémoire sémantique")
    print("=" * 60)
    
    # Créer les collections de mémoire
    memory_collections = [
        "conversations",    # Historique des conversations
        "preferences",      # Préférences utilisateur
        "knowledge",        # Base de connaissances personnelle
        "tasks",           # Historique des tâches
        "context"          # Contexte de travail
    ]
    
    # Initialiser les collections
    for collection in memory_collections:
        try:
            await self.kernel.memory.create_collection_async(collection)
            print(f"   ✅ Collection '{collection}' créée")
        except Exception as e:
            print(f"   ℹ️ Collection '{collection}' existe déjà")
    
    # Charger la mémoire existante depuis le fichier
    await self._load_persistent_memory()
    
    # Ajouter des connaissances de base
    await self._seed_initial_knowledge()
    
    print("🧠 Mémoire sémantique configurée avec succès")
    return True

async def _load_persistent_memory(self):
    """Charger la mémoire persistante depuis le fichier"""
    memory_file = Path("memory_state.json")
    
    if memory_file.exists():
        try:
            with open(memory_file, "r", encoding="utf-8") as f:
                memory_data = json.load(f)
            
            # Restaurer les préférences
            agent_info = memory_data.get("agent_info", {})
            self.agent_state.last_interaction = agent_info.get("last_interaction")
            self.agent_state.conversation_count = agent_info.get("total_conversations", 0)
            
            print("   📂 Mémoire persistante chargée")
            
        except Exception as e:
            print(f"   ⚠️ Erreur lors du chargement de la mémoire: {e}")
    else:
        print("   🆕 Première utilisation - nouvelle mémoire créée")

async def _seed_initial_knowledge(self):
    """Ajouter des connaissances de base"""
    initial_knowledge = [
        {
            "collection": "knowledge",
            "text": "Semantic Kernel est un framework Microsoft pour créer des agents IA avec planification automatique et mémoire.",
            "id": "sk_intro"
        },
        {
            "collection": "knowledge", 
            "text": "Les plugins Semantic Kernel permettent d'étendre les capacités de l'agent avec des fonctions personnalisées.",
            "id": "sk_plugins"
        },
        {
            "collection": "knowledge",
            "text": "La planification automatique permet de décomposer des tâches complexes en étapes simples.",
            "id": "sk_planning"
        }
    ]
    
    for item in initial_knowledge:
        try:
            await self.kernel.memory.save_information_async(
                collection=item["collection"],
                text=item["text"],
                id=item["id"]
            )
        except Exception:
            pass  # Déjà existant
    
    print("   📚 Connaissances de base ajoutées")
```

**Concepts Mémoire Sémantique**:
- **Collections**: Organisation thématique des souvenirs
- **Embeddings**: Vectorisation pour recherche sémantique
- **Persistence**: Sauvegarde entre sessions
- **Seeding**: Connaissances de base initiales

### ✅ TODO 8: Planificateur Automatique (10 min)

**Concepts appris**: Planification et orchestration automatique

Implémentez `create_automatic_planner()`:

```python
def create_automatic_planner(self):
    print("\n📋 ÉTAPE: Création du planificateur automatique")
    print("=" * 60)
    
    # Créer le planner avec configuration optimisée
    self.planner = BasicPlanner()
    
    # Configuration des capacités de planification
    self.planning_config = {
        "max_tokens": 1000,
        "temperature": 0.3,  # Plus déterministe pour planification
        "max_iterations": 5,
        "allow_missing_functions": False,
        "excluded_plugins": [],  # Plugins à exclure si nécessaire
        "included_functions": []  # Fonctions spécifiques à inclure
    }
    
    # Créer des exemples de plans pour différents scénarios
    self.example_plans = {
        "productivity": {
            "description": "Plan a productive day based on user preferences",
            "expected_functions": ["TimePlugin.get_current_time", "TaskPlugin.list_tasks", "PreferencePlugin.get_preferences"]
        },
        "learning": {
            "description": "Help me learn about AI agents step by step",
            "expected_functions": ["memory search", "structured explanation", "progress tracking"]
        },
        "organization": {
            "description": "Organize my project timeline with reminders",
            "expected_functions": ["TaskPlugin.create_task", "TimePlugin.schedule_reminder", "task prioritization"]
        },
        "analysis": {
            "description": "Analyze data and provide insights with recommendations",
            "expected_functions": ["data processing", "pattern recognition", "recommendation generation"]
        }
    }
    
    print("✅ Planificateur automatique configuré")
    print("🎯 Capacités de planification:")
    print("   • Décomposition automatique de tâches complexes")
    print("   • Sélection intelligente de plugins")
    print("   • Orchestration multi-étapes")
    print("   • Adaptation en cas d'erreur")
    
    return True

async def _demonstrate_planning_capability(self, goal: str):
    """Démontrer les capacités de planification"""
    try:
        print(f"\n🎯 Démonstration de planification pour: {goal}")
        
        # Créer un plan pour l'objectif donné
        plan = await self.planner.create_plan_async(goal, self.kernel)
        
        print("📋 Plan généré:")
        for i, step in enumerate(plan.steps, 1):
            print(f"   {i}. {step.description}")
            print(f"      Plugin: {step.plugin_name}")
            print(f"      Fonction: {step.function_name}")
        
        return plan
        
    except Exception as e:
        print(f"❌ Erreur lors de la planification: {e}")
        return None
```

**Capacités du Planner**:
- **Auto-decomposition**: Division automatique des tâches
- **Function selection**: Choix optimal des plugins
- **Error recovery**: Adaptation en cas de problème
- **Goal orientation**: Focus sur l'objectif final

### ✅ TODO 9: Conversation avec Mémoire (20 min)

**Concepts appris**: Intégration mémoire et conversation

Implémentez `implement_conversation_with_memory()`:

```python
async def implement_conversation_with_memory(self, user_input: str):
    print(f"\n💬 ÉTAPE: Conversation avec mémoire - '{user_input}'")
    print("=" * 60)
    
    start_time = datetime.now()
    
    try:
        # 1. Rechercher le contexte dans la mémoire sémantique
        relevant_memories = await self._search_relevant_context(user_input)
        
        # 2. Analyser la complexité et décider du traitement
        complexity_analysis = self._analyze_query_complexity(user_input)
        needs_planning = complexity_analysis["requires_planning"]
        
        print(f"🔍 Contexte trouvé: {len(relevant_memories)} éléments")
        print(f"📊 Complexité: {complexity_analysis['score']:.2f} - Planning: {'Oui' if needs_planning else 'Non'}")
        
        # 3. Construire le prompt avec contexte et personnalisation
        context_prompt = await self._build_context_prompt(user_input, relevant_memories)
        
        # 4. Traitement selon la complexité
        if needs_planning:
            print("🎯 Utilisation du planificateur pour tâche complexe")
            response = await self._handle_complex_query_with_planning(user_input, context_prompt)
        else:
            print("💬 Réponse directe avec contexte")
            response = await self._handle_simple_query(user_input, context_prompt)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # 5. Mémoriser la conversation
        await self._memorize_conversation(user_input, response, execution_time)
        
        # 6. Mettre à jour l'état de l'agent
        self._update_agent_state(user_input, response)
        
        print(f"✅ Conversation traitée en {execution_time:.2f}s")
        
        return {
            "user_input": user_input,
            "response": response,
            "execution_time": execution_time,
            "used_memory": len(relevant_memories) > 0,
            "used_planning": needs_planning,
            "context_elements": len(relevant_memories),
            "complexity_score": complexity_analysis["score"],
            "timestamp": start_time.isoformat()
        }
        
    except Exception as e:
        print(f"❌ Erreur durant la conversation: {e}")
        return {
            "user_input": user_input,
            "response": f"Désolé, j'ai rencontré une erreur: {e}",
            "error": str(e),
            "execution_time": (datetime.now() - start_time).total_seconds(),
            "timestamp": start_time.isoformat()
        }

async def _search_relevant_context(self, query: str, limit: int = 3):
    """Rechercher le contexte pertinent dans la mémoire"""
    try:
        # Recherche dans toutes les collections
        all_memories = []
        
        for collection in ["conversations", "knowledge", "preferences"]:
            memories = await self.kernel.memory.search_async(
                collection=collection,
                query=query,
                limit=limit
            )
            all_memories.extend(memories)
        
        # Trier par pertinence et retourner les meilleurs
        sorted_memories = sorted(all_memories, key=lambda x: x.relevance, reverse=True)
        return sorted_memories[:limit]
        
    except Exception as e:
        print(f"⚠️ Erreur recherche mémoire: {e}")
        return []

def _analyze_query_complexity(self, query: str) -> Dict[str, Any]:
    """Analyser la complexité d'une requête"""
    complexity_indicators = {
        "multi_step_keywords": ["plan", "organize", "schedule", "analyze", "compare", "strategy"],
        "question_complexity": ["how to", "what if", "explain", "breakdown", "step by step"],
        "time_planning": ["tomorrow", "next week", "schedule", "remind", "deadline"],
        "multi_domain": ["and", "also", "plus", "additionally"],
        "conditional": ["if", "when", "unless", "depending"]
    }
    
    score = 0
    detected_indicators = []
    
    query_lower = query.lower()
    
    for category, keywords in complexity_indicators.items():
        for keyword in keywords:
            if keyword in query_lower:
                score += 1
                detected_indicators.append(f"{category}:{keyword}")
    
    # Normaliser le score
    max_possible = sum(len(keywords) for keywords in complexity_indicators.values())
    normalized_score = score / max_possible if max_possible > 0 else 0
    
    return {
        "score": normalized_score,
        "requires_planning": normalized_score > 0.3,  # Seuil de complexité
        "indicators": detected_indicators,
        "category": "complex" if normalized_score > 0.3 else "simple"
    }

async def _build_context_prompt(self, user_input: str, memories: List) -> str:
    """Construire un prompt avec contexte personnalisé"""
    context_parts = []
    
    # Ajouter les souvenirs pertinents
    if memories:
        context_parts.append("Contexte mémorisé:")
        for memory in memories:
            context_parts.append(f"- {memory.text}")
    
    # Ajouter les préférences utilisateur
    prefs = f"""Préférences utilisateur:
- Style de communication: {self.agent_state.communication_style}
- Langue: {self.agent_state.language}
- Contexte: {self.agent_state.work_context or 'Non spécifié'}
- Intérêts: {', '.join(self.agent_state.interests) if self.agent_state.interests else 'Non spécifiés'}"""
    
    context_parts.append(prefs)
    
    # Construire le prompt final
    context_section = "\n".join(context_parts)
    
    prompt = f"""Tu es un assistant intelligent personnel avec accès à la mémoire et aux préférences de l'utilisateur.

{context_section}

Instructions:
- Utilise le contexte mémorisé pour personnaliser ta réponse
- Respecte le style de communication préféré
- Sois proactif en suggérant des actions pertinentes
- Si des informations sont manquantes, demande des clarifications

Requête utilisateur: {user_input}

Réponse personnalisée:"""
    
    return prompt

async def _handle_simple_query(self, user_input: str, context_prompt: str) -> str:
    """Traiter une requête simple avec contexte"""
    try:
        # Créer une fonction sémantique pour la réponse
        response_function = self.kernel.create_semantic_function(
            prompt_template=context_prompt,
            max_tokens=500,
            temperature=0.7
        )
        
        # Exécuter la fonction
        result = await response_function.invoke_async()
        return result.result.strip()
        
    except Exception as e:
        return f"Erreur lors du traitement: {e}"

async def _handle_complex_query_with_planning(self, user_input: str, context_prompt: str) -> str:
    """Traiter une requête complexe avec planification"""
    try:
        # Créer un plan pour la requête complexe
        plan = await self.planner.create_plan_async(user_input, self.kernel)
        
        # Exécuter le plan
        plan_result = await plan.invoke_async()
        
        # Enrichir avec le contexte
        enriched_prompt = f"""{context_prompt}

Plan exécuté: {plan_result.result}

Synthèse finale personnalisée:"""
        
        # Générer la réponse finale
        synthesis_function = self.kernel.create_semantic_function(
            prompt_template=enriched_prompt,
            max_tokens=600,
            temperature=0.6
        )
        
        final_result = await synthesis_function.invoke_async()
        return final_result.result.strip()
        
    except Exception as e:
        return f"Erreur lors de la planification: {e}"

async def _memorize_conversation(self, user_input: str, response: str, execution_time: float):
    """Mémoriser la conversation dans la mémoire sémantique"""
    try:
        conversation_text = f"Utilisateur: {user_input}\nAssistant: {response}"
        conversation_id = f"conv_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        await self.kernel.memory.save_information_async(
            collection="conversations",
            text=conversation_text,
            id=conversation_id,
            description=f"Conversation du {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
        
        print(f"💾 Conversation mémorisée (ID: {conversation_id})")
        
    except Exception as e:
        print(f"⚠️ Erreur mémorisation: {e}")

def _update_agent_state(self, user_input: str, response: str):
    """Mettre à jour l'état de l'agent"""
    self.agent_state.last_interaction = datetime.now().isoformat()
    self.agent_state.conversation_count += 1
    
    # Ajouter à l'historique local
    self.conversation_history.append({
        "user": user_input,
        "assistant": response,
        "timestamp": datetime.now().isoformat(),
        "turn": self.agent_state.conversation_count
    })
    
    # Analyser pour détecter de nouveaux intérêts
    self._detect_user_interests(user_input)

def _detect_user_interests(self, user_input: str):
    """Détecter de nouveaux centres d'intérêt"""
    tech_keywords = ["IA", "machine learning", "python", "data", "cloud", "blockchain"]
    business_keywords = ["stratégie", "marketing", "finance", "management", "startup"]
    
    user_lower = user_input.lower()
    
    for keyword in tech_keywords:
        if keyword.lower() in user_lower and "technologie" not in self.agent_state.interests:
            self.agent_state.interests.append("technologie")
            print(f"🎯 Nouvel intérêt détecté: technologie")
            break
    
    for keyword in business_keywords:
        if keyword.lower() in user_lower and "business" not in self.agent_state.interests:
            self.agent_state.interests.append("business")
            print(f"🎯 Nouvel intérêt détecté: business")
            break
```

### ✅ TODO 10: Gestion des Préférences (8 min)

**Concepts appris**: Personnalisation et adaptation

Implémentez `manage_user_preferences()`:

```python
async def manage_user_preferences(self, preference_type: str, value: Any):
    print(f"\n⚙️ ÉTAPE: Gestion des préférences - {preference_type}")
    print("=" * 60)
    
    # Valider le type de préférence
    valid_preferences = {
        "communication_style": ["professional", "casual", "formal"],
        "notification_time": "time_format",  # HH:MM
        "task_priority": ["high", "medium", "low"],
        "language": ["fr", "en", "es", "de"],
        "timezone": "timezone_format",
        "work_context": "free_text"
    }
    
    if preference_type not in valid_preferences:
        print(f"❌ Type de préférence invalide: {preference_type}")
        print(f"   Types valides: {', '.join(valid_preferences.keys())}")
        return False
    
    # Valider la valeur selon le type
    validation_result = self._validate_preference_value(preference_type, value, valid_preferences)
    
    if not validation_result["valid"]:
        print(f"❌ Valeur invalide: {validation_result['reason']}")
        return False
    
    # Mettre à jour l'état local
    old_value = getattr(self.agent_state, preference_type, "Non défini")
    setattr(self.agent_state, preference_type, value)
    
    # Sauvegarder dans la mémoire sémantique
    await self._save_preference_to_memory(preference_type, value, old_value)
    
    print(f"✅ Préférence mise à jour:")
    print(f"   {preference_type}: {old_value} → {value}")
    
    return True

def _validate_preference_value(self, pref_type: str, value: Any, valid_prefs: Dict) -> Dict:
    """Valider une valeur de préférence"""
    constraints = valid_prefs[pref_type]
    
    if isinstance(constraints, list):
        # Valeurs prédéfinies
        if value in constraints:
            return {"valid": True}
        else:
            return {"valid": False, "reason": f"Valeurs acceptées: {', '.join(constraints)}"}
    
    elif constraints == "time_format":
        # Format HH:MM
        try:
            datetime.strptime(value, "%H:%M")
            return {"valid": True}
        except ValueError:
            return {"valid": False, "reason": "Format attendu: HH:MM (ex: 09:30)"}
    
    elif constraints == "timezone_format":
        # Validation basique de timezone
        valid_timezones = ["Europe/Paris", "America/New_York", "Asia/Tokyo", "UTC"]
        if value in valid_timezones:
            return {"valid": True}
        else:
            return {"valid": False, "reason": f"Timezones supportées: {', '.join(valid_timezones)}"}
    
    elif constraints == "free_text":
        # Texte libre avec contraintes basiques
        if isinstance(value, str) and 3 <= len(value) <= 200:
            return {"valid": True}
        else:
            return {"valid": False, "reason": "Texte entre 3 et 200 caractères"}
    
    return {"valid": False, "reason": "Type de contrainte non reconnu"}

async def _save_preference_to_memory(self, pref_type: str, value: Any, old_value: Any):
    """Sauvegarder une préférence dans la mémoire"""
    try:
        pref_text = f"Préférence {pref_type}: {value} (ancienne valeur: {old_value})"
        pref_id = f"pref_{pref_type}_{datetime.now().strftime('%Y%m%d')}"
        
        await self.kernel.memory.save_information_async(
            collection="preferences",
            text=pref_text,
            id=pref_id,
            description=f"Mise à jour préférence {pref_type}"
        )
        
        print(f"💾 Préférence sauvegardée en mémoire")
        
    except Exception as e:
        print(f"⚠️ Erreur sauvegarde préférence: {e}")
```

### ✅ TODO 11: Démonstration Planification (10 min)

**Concepts appris**: Planification complexe et adaptation

Implémentez `demonstrate_planning_capabilities()`:

```python
async def demonstrate_planning_capabilities(self):
    print("\n🎯 ÉTAPE: Démonstration des capacités de planification")
    print("=" * 60)
    
    demo_scenarios = [
        "Plan me a productive day based on my preferences",
        "Help me organize a project to learn machine learning in 3 months",
        "Create a strategy to improve my work-life balance with specific actions",
        "Plan a comprehensive research approach for AI agent frameworks"
    ]
    
    print("📋 Scénarios de planification:")
    for i, scenario in enumerate(demo_scenarios, 1):
        print(f"  {i}. {scenario}")
    
    # Exécuter les scénarios de planification
    for i, scenario in enumerate(demo_scenarios, 1):
        print(f"\n🎯 Scénario {i}: {scenario}")
        print("-" * 50)
        
        try:
            # Créer et exécuter le plan
            plan = await self.planner.create_plan_async(scenario, self.kernel)
            
            print(f"📝 Plan généré ({len(plan.steps)} étapes):")
            for j, step in enumerate(plan.steps, 1):
                print(f"   {j}. {step.description}")
                if hasattr(step, 'plugin_name') and step.plugin_name:
                    print(f"      → Plugin: {step.plugin_name}.{step.function_name}")
            
            # Simuler l'exécution (en production: vraie exécution)
            print(f"⚡ Simulation d'exécution...")
            execution_time = len(plan.steps) * 0.5  # Simulation
            
            print(f"✅ Plan exécuté en {execution_time:.1f}s (simulé)")
            
            # Démontrer l'adaptation d'erreur
            if i == 2:  # Pour le scénario work-life balance
                print("🔄 Démonstration d'adaptation d'erreur:")
                print("   • Erreur simulée: Plugin indisponible")
                print("   • Adaptation: Utilisation d'alternative")
                print("   • Récupération: Plan modifié automatiquement")
            
        except Exception as e:
            print(f"❌ Erreur planification: {e}")
            print("🔄 En production: retry avec plan simplifié")
        
        if i < len(demo_scenarios):
            print()
    
    print(f"\n🏆 Démonstration de planification terminée")
    print("💡 Capacités démontrées:")
    print("   • Décomposition automatique de tâches complexes")
    print("   • Sélection intelligente de plugins")
    print("   • Adaptation en cas de problème")
    print("   • Personnalisation selon le contexte utilisateur")
```

### ✅ TODO 12: Sauvegarde d'État (5 min)

**Concepts appris**: Persistance et continuité

Implémentez `save_agent_state()`:

```python
def save_agent_state(self):
    print("\n💾 ÉTAPE: Sauvegarde de l'état de l'agent")
    print("=" * 60)
    
    # Préparer les données d'état
    state_data = {
        "agent_info": {
            "created_at": self.agent_state.created_at,
            "last_interaction": self.agent_state.last_interaction,
            "total_conversations": self.agent_state.conversation_count,
            "version": "1.0.0",
            "last_saved": datetime.now().isoformat()
        },
        "user_preferences": {
            "communication_style": self.agent_state.communication_style,
            "notification_time": self.agent_state.notification_time,
            "task_priority": self.agent_state.task_priority,
            "language": self.agent_state.language,
            "timezone": self.agent_state.timezone,
            "work_context": self.agent_state.work_context
        },
        "user_profile": {
            "interests": self.agent_state.interests,
            "learning_preferences": self.agent_state.learning_preferences,
            "conversation_count": self.agent_state.conversation_count
        },
        "conversation_summary": {
            "recent_topics": self._extract_recent_topics(),
            "user_interaction_patterns": self._analyze_interaction_patterns(),
            "recurring_requests": self._identify_recurring_requests()
        },
        "performance_metrics": {
            "avg_response_time": self._calculate_avg_response_time(),
            "successful_plans": self._count_successful_plans(),
            "memory_utilization": self._estimate_memory_usage(),
            "plugin_usage_stats": self._get_plugin_usage_stats()
        },
        "system_health": {
            "memory_collections_count": 5,  # conversations, preferences, knowledge, tasks, context
            "plugins_active": 5,  # Time, Preference, Task, Weather, Calculator
            "last_error": None,
            "uptime_sessions": self.agent_state.conversation_count
        }
    }
    
    # Sauvegarder dans memory_state.json
    try:
        with open("memory_state.json", "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2, ensure_ascii=False)
        
        print("✅ État de l'agent sauvegardé dans memory_state.json")
        print(f"📊 Résumé de session:")
        print(f"   • Conversations: {state_data['agent_info']['total_conversations']}")
        print(f"   • Intérêts détectés: {len(self.agent_state.interests)}")
        print(f"   • Plugins actifs: {state_data['system_health']['plugins_active']}")
        
    except Exception as e:
        print(f"❌ Erreur sauvegarde: {e}")

def _extract_recent_topics(self) -> List[str]:
    """Extraire les sujets récents des conversations"""
    topics = []
    for conv in self.conversation_history[-5:]:  # 5 dernières conversations
        user_msg = conv["user"].lower()
        if "plan" in user_msg or "organiz" in user_msg:
            topics.append("planification")
        elif "learn" in user_msg or "explain" in user_msg:
            topics.append("apprentissage")
        elif "prefer" in user_msg or "setting" in user_msg:
            topics.append("configuration")
    return list(set(topics))

def _analyze_interaction_patterns(self) -> Dict[str, Any]:
    """Analyser les patterns d'interaction"""
    if not self.conversation_history:
        return {"pattern": "insufficient_data"}
    
    # Analyser la longueur des questions
    avg_question_length = sum(len(conv["user"].split()) for conv in self.conversation_history) / len(self.conversation_history)
    
    # Analyser la fréquence
    time_intervals = []
    for i in range(1, len(self.conversation_history)):
        prev_time = datetime.fromisoformat(self.conversation_history[i-1]["timestamp"])
        curr_time = datetime.fromisoformat(self.conversation_history[i]["timestamp"])
        interval = (curr_time - prev_time).total_seconds()
        time_intervals.append(interval)
    
    avg_interval = sum(time_intervals) / len(time_intervals) if time_intervals else 0
    
    return {
        "avg_question_length": avg_question_length,
        "avg_time_between_queries": f"{avg_interval:.1f}s",
        "interaction_style": "detailed" if avg_question_length > 10 else "concise"
    }

def _identify_recurring_requests(self) -> List[str]:
    """Identifier les demandes récurrentes"""
    # Analyser les mots-clés fréquents
    all_words = []
    for conv in self.conversation_history:
        words = conv["user"].lower().split()
        all_words.extend(word for word in words if len(word) > 3)
    
    from collections import Counter
    word_counts = Counter(all_words)
    recurring = [word for word, count in word_counts.items() if count >= 2]
    
    return recurring[:5]  # Top 5

def _calculate_avg_response_time(self) -> float:
    """Calculer le temps de réponse moyen"""
    # Simulation - en production: vraies métriques
    return 2.3  # secondes

def _count_successful_plans(self) -> int:
    """Compter les plans réussis"""
    # Simulation - en production: tracking réel
    return max(0, self.agent_state.conversation_count - 2)

def _estimate_memory_usage(self) -> str:
    """Estimer l'utilisation mémoire"""
    conversations = len(self.conversation_history)
    estimated_mb = conversations * 0.1  # Estimation: 0.1MB par conversation
    return f"{estimated_mb:.1f}MB"

def _get_plugin_usage_stats(self) -> Dict[str, int]:
    """Obtenir les statistiques d'utilisation des plugins"""
    # Simulation - en production: tracking réel
    return {
        "TimePlugin": 3,
        "PreferencePlugin": 2,
        "TaskPlugin": 1,
        "WeatherPlugin": 1,
        "CalculatorPlugin": 0
    }
```

### ✅ TODO 13: Démonstration Complète (5 min)

**Concepts appris**: Test end-to-end du système

Implémentez `run_demo()`:

```python
async def run_demo(self):
    print("\n🎬 DÉMONSTRATION DE VOTRE AGENT INTELLIGENT")
    print("=" * 60)
    
    # Interactions de démonstration progressives
    demo_interactions = [
        "Hello! I'm new here. Can you introduce yourself?",
        "I prefer a casual communication style",
        "What's the weather like in Paris today?",
        "Help me plan a productive morning routine with reminders",
        "Remember that I'm interested in AI and machine learning",
        "Calculate 15 * 8 + 42",
        "Plan a strategy to learn Python programming in 2 months"
    ]
    
    print("💬 Interactions de démonstration:")
    for i, interaction in enumerate(demo_interactions, 1):
        print(f"  {i}. {interaction}")
    
    print("\n📋 Processus de démonstration:")
    print("  1. 🔌 Création des plugins personnalisés")
    print("  2. 🧠 Configuration de la mémoire sémantique")
    print("  3. 📋 Création du planificateur automatique")
    print("  4. 💬 Conversations avec mémoire et adaptation")
    print("  5. ⚙️ Gestion des préférences utilisateur")
    print("  6. 🎯 Démonstration de planification avancée")
    print("  7. 💾 Sauvegarde de l'état complet")
    
    # Exécuter la démonstration complète
    print("\n⚡ Lancement de la démonstration...")
    
    try:
        # Étape 1: Plugins
        if self.create_custom_plugins():
            print("✅ Plugins créés avec succès")
            
            # Étape 2: Mémoire
            if await self.setup_semantic_memory():
                print("✅ Mémoire sémantique configurée")
                
                # Étape 3: Planner
                if self.create_automatic_planner():
                    print("✅ Planificateur automatique créé")
                    
                    # Étape 4: Conversations interactives
                    print(f"\n💬 Exécution de {len(demo_interactions)} interactions...")
                    
                    for i, interaction in enumerate(demo_interactions, 1):
                        print(f"\n--- Interaction {i}/{len(demo_interactions)} ---")
                        print(f"👤 Utilisateur: {interaction}")
                        
                        # Traiter avec gestion spéciale pour les préférences
                        if "prefer" in interaction.lower() and "casual" in interaction.lower():
                            await self.manage_user_preferences("communication_style", "casual")
                            response_data = {"response": "Parfait ! J'ai mis à jour votre style de communication en mode décontracté. 😊"}
                        else:
                            response_data = await self.implement_conversation_with_memory(interaction)
                        
                        print(f"🤖 Assistant: {response_data['response']}")
                        
                        if response_data.get("used_planning"):
                            print("   🎯 Planification automatique utilisée")
                        if response_data.get("used_memory"):
                            print(f"   🧠 Contexte mémoire: {response_data.get('context_elements', 0)} éléments")
                        
                        # Petite pause pour la démo
                        await asyncio.sleep(0.5)
                    
                    # Étape 5: Démonstration planification
                    print(f"\n🎯 Démonstration des capacités de planification...")
                    await self.demonstrate_planning_capabilities()
                    
                    # Étape 6: Sauvegarde
                    self.save_agent_state()
                    
                    print("\n🏆 DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
                    print("\n📁 Fichiers générés:")
                    print("  💾 memory_state.json - État complet de l'agent")
                    print("  🧠 Mémoire sémantique - Collections en mémoire")
                    print("  📊 Métriques de performance - Intégrées dans l'état")
                    
                    # Afficher les statistiques finales
                    print(f"\n📊 Statistiques de la session:")
                    print(f"   💬 Conversations: {self.agent_state.conversation_count}")
                    print(f"   🎯 Intérêts détectés: {len(self.agent_state.interests)}")
                    print(f"   🔌 Plugins actifs: 5 (Time, Preference, Task, Weather, Calculator)")
                    print(f"   🧠 Collections mémoire: 5 (conversations, preferences, knowledge, tasks, context)")
                    print(f"   ⚙️ Préférences configurées: Style {self.agent_state.communication_style}")
                    
                    return True
                else:
                    print("❌ Échec de la création du planificateur")
            else:
                print("❌ Échec de la configuration mémoire")
        else:
            print("❌ Échec de la création des plugins")
            
    except Exception as e:
        print(f"❌ Erreur durant la démonstration: {e}")
        
    return False
```

## 🎯 Résultat Final

Après avoir complété tous les TODOs, vous aurez créé :

### 📁 Fichiers Générés
- ✅ `memory_state.json` - État complet de l'agent avec préférences et métriques
- ✅ Collections mémoire - Stockage sémantique des conversations et connaissances
- ✅ Plugins personnalisés - 5 plugins fonctionnels (Time, Preference, Task, Weather, Calculator)

### 🎓 Compétences Acquises
- **Semantic Kernel**: Kernel, plugins, fonctions sémantiques
- **Planification**: Décomposition automatique et orchestration
- **Mémoire**: Stockage sémantique et recherche contextuelle
- **Personnalisation**: Préférences utilisateur et adaptation
- **Production**: État persistant et métriques de performance

### 🚀 Applications Possibles
- Assistant personnel intelligent
- Agent de productivité avec mémoire
- Système de recommandations adaptatif
- Chatbot d'entreprise avec contexte

## 🎬 Démonstration

Lancez votre agent terminé :

```bash
python my_intelligent_agent_starter.py
```

Le système exécutera automatiquement :
1. ✅ Création de 5 plugins personnalisés
2. ✅ Configuration mémoire sémantique avec 5 collections
3. ✅ Planificateur automatique avec décomposition de tâches
4. ✅ 7 conversations interactives avec adaptation
5. ✅ Démonstration de planification complexe
6. ✅ Sauvegarde d'état complet avec métriques

## 🔧 Personnalisation

### Adapter à Votre Domaine
1. **Plugins**: Créez des fonctions spécifiques à votre métier
2. **Mémoire**: Ajoutez des collections pour vos données
3. **Préférences**: Étendez les types selon vos besoins
4. **Planification**: Adaptez les patterns de décomposition

### Optimisations Production
1. **Performance**: Mémoire vectorielle distribuée, caching intelligent
2. **Scalabilité**: Multi-utilisateurs, isolation des données
3. **Intégrations**: APIs externes, webhooks, notifications
4. **Sécurité**: Chiffrement, audit logs, permissions

## 🏆 Validation des Acquis

Vous maîtrisez le projet si vous pouvez :
- [ ] Expliquer l'architecture Semantic Kernel (Kernel, Plugins, Planner, Memory)
- [ ] Créer des plugins personnalisés avec @sk_function
- [ ] Configurer la mémoire sémantique et recherche contextuelle
- [ ] Utiliser la planification automatique pour tâches complexes
- [ ] Implémenter la persistance d'état et personnalisation

## 🔗 Ressources pour Aller Plus Loin

- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Plugin Development Guide](https://learn.microsoft.com/en-us/semantic-kernel/agents/plugins/)
- [Planning and Orchestration](https://learn.microsoft.com/en-us/semantic-kernel/agents/planning/)
- [Memory and Embeddings](https://learn.microsoft.com/en-us/semantic-kernel/memories/)

---

🎯 **Félicitations !** Vous avez construit un agent intelligent adaptatif et maîtrisé Semantic Kernel !