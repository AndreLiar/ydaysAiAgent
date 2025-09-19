# 🔷 Semantic Kernel - L'Approche Microsoft

## 📚 Vue d'ensemble

Semantic Kernel est le framework d'agents IA de Microsoft qui combine programmation traditionnelle et intelligence artificielle. Il utilise une approche unique basée sur les "skills" (compétences) et la planification automatique pour orchestrer des tâches complexes.

### 🎯 Cas d'usage principaux
- **Intégration Microsoft 365** : Automatisation Office et Teams
- **Planification automatique** : Orchestration intelligente de tâches
- **Système de plugins** : Extensions modulaires et réutilisables
- **Mémoire avancée** : Contexte persistant et personnalisation

## 📂 Structure des fichiers

```
semantic-kernel/
├── kernel-basics.py        # 🧠 Concepts fondamentaux et bases
├── plugins-demo.py         # 🔌 Système de plugins et compétences
├── planners.py            # 🧭 Planification automatique avancée
└── memory-integration.py   # 🧠 Intégration mémoire complète
```

## 🚀 Installation

```bash
# Dépendance principale
pip install semantic-kernel

# Pour les LLMs OpenAI
pip install openai

# Dépendances supplémentaires
pip install numpy python-dotenv requests
```

## ⚙️ Configuration

Créez un fichier `.env` :

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Configuration de base Semantic Kernel :
```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()
kernel.add_chat_service(
    "openai-gpt4",
    OpenAIChatCompletion("gpt-4", api_key)
)
```

## 📖 Guide d'utilisation

### 1. 🧠 Kernel Basics (`kernel-basics.py`)

**Ce que vous apprendrez :**
- Architecture du Semantic Kernel
- Fonctions sémantiques vs natives
- Templating avancé avec variables
- Chaînage et orchestration de base

**Concepts fondamentaux :**

#### 🎯 Semantic Functions
```python
# Fonction basée sur prompts IA
semantic_function = kernel.create_semantic_function(
    prompt_template,
    function_name="Assistant",
    skill_name="Communication"
)
```

#### ⚙️ Native Functions
```python
# Fonction Python traditionnelle
class MathSkills:
    @sk_function(description="Additionne deux nombres")
    def add(self, context: SKContext) -> str:
        return str(float(context["number1"]) + float(context["number2"]))
```

#### 🔗 Function Chaining
```
Input → Semantic Function → Native Function → Output
```

**Démonstrations disponibles :**
1. **Prompts simples** : Bases du templating
2. **Templating avancé** : Variables multiples
3. **Chaînage de fonctions** : Workflows séquentiels
4. **Fonctions natives** : Intégration code Python
5. **Combinaison sémantique + native** : Puissance hybride
6. **Mémoire et contexte** : Conversations persistantes

## 🎬 Votre Agent Semantic Kernel en Action

### 🤖 **Ce que Votre Agent Intelligent Fera Concrètement**

**Démonstration assistant personnel avec mémoire** :

```
🎯 USER: "Aide-moi à planifier ma stratégie marketing Q1 2025"

🧠 SEMANTIC KERNEL AGENT:

🔍 Kernel Planning: "Analyse de votre demande → Planification automatique"

📋 PLAN GÉNÉRÉ:
   1. [Memory] Récupérer contexte business utilisateur
   2. [Research] Analyser tendances marketing Q1
   3. [Strategy] Générer framework stratégique  
   4. [Budget] Calculer allocations optimales
   5. [Timeline] Créer planning détaillé
   6. [Memory] Sauvegarder préférences pour futures sessions

⚙️ EXÉCUTION AUTOMATIQUE:

🧠 Memory Plugin: "Contexte utilisateur récupéré:
   - Secteur: SaaS B2B (CRM)
   - Budget annuel: €50k marketing
   - Objectif: +40% leads qualifiés
   - Préférence: digital-first, mesurable"

🔍 Research Plugin: "Tendances Q1 2025 identifiées:
   ✅ Video content: +67% engagement  
   ✅ AI-powered personalization mainstream
   ✅ LinkedIn ads 23% plus efficaces que Google
   ✅ Webinars ROI stable: 4.2x investment"

📊 Strategy Plugin: "Framework adapté à votre contexte:
   
   🎯 STRATÉGIE RECOMMANDÉE:
   1. Video content LinkedIn (40% budget)
   2. Webinars techniques mensuels (25% budget)  
   3. AI-personalized email sequences (20% budget)
   4. Retargeting campaigns (15% budget)
   
   📈 PRÉDICTIONS ROI:
   - Leads: +47% (vs objectif 40%) ✅
   - Cost per lead: -23%
   - Pipeline value: +€180k estimé"

💰 Budget Plugin: "Allocation optimisée €50k:
   - LinkedIn Video Ads: €20k
   - Webinar Production: €12.5k  
   - Email Marketing Platform: €10k
   - Retargeting Tools: €7.5k"

📅 Timeline Plugin: "Planning Q1 généré:
   'Marketing_Strategy_Q1_2025.pdf' - 30 pages détaillées
   'Budget_Allocation_Optimized.xlsx' - breakdown mensuel"

🧠 Memory Update: "Préférences sauvegardées pour prochaines sessions"

⏱️ Temps total: 6 minutes | 🔌 5 plugins | 🧠 Mémoire persistante
```

### 🏆 **Résultat Final Concret**

À la fin, vous aurez un **agent intelligent avec mémoire** qui :
- **Planification automatique** : Décomposition intelligente → plugins → orchestration
- **Plugins modulaires** : Research, Analysis, Memory, Budget, Timeline → extensible
- **Mémoire persistante** : Contexte utilisateur → préférences → amélioration continue  
- **Orchestration Microsoft** : Intégration Office 365, Teams, SharePoint
- **Intelligence adaptative** : Apprentissage usage → optimisation workflows

**Utilisation :**
```bash
python kernel-basics.py
# Choisir la démo (1-7)
```

### 2. 🔌 Plugins Demo (`plugins-demo.py`)

**Ce que vous apprendrez :**
- Système de plugins modulaires
- Création de compétences spécialisées
- Orchestration multi-plugins
- Réutilisabilité et extensibilité

**Plugins disponibles :**

#### ⏰ Time Plugin
```python
@sk_function(description="Obtient la date actuelle")
def get_current_time(self, context: SKContext) -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

#### 🌐 Web Plugin
```python
@sk_function(description="Obtient la météo d'une ville")
def get_weather(self, context: SKContext) -> str:
    city = context["city"]
    return get_weather_data(city)
```

#### 📁 File Plugin
```python
@sk_function(description="Lit un fichier")
def read_file(self, context: SKContext) -> str:
    with open(context["filename"]) as f:
        return f.read()
```

#### 📊 Data Plugin
```python
@sk_function(description="Calcule des statistiques")
def calculate_stats(self, context: SKContext) -> str:
    numbers = [float(x) for x in context["numbers"].split(",")]
    return f"Moyenne: {sum(numbers)/len(numbers):.2f}"
```

**Architecture plugins :**
```
Kernel
├── TimePlugin (get_time, add_days, format_date)
├── WebPlugin (weather, search, validate_url)
├── FilePlugin (read, write, list)
└── DataPlugin (stats, json_parse, transform)
```

**Orchestration multi-plugins :**
```python
# Utilisation coordonnée de plusieurs plugins
result = await time_plugin["get_current_time"].invoke_async()
weather = await web_plugin["get_weather"].invoke_async(context)
await file_plugin["write_file"].invoke_async(report_context)
```

**Utilisation :**
```bash
python plugins-demo.py
# Tester les différents plugins (1-6)
```

### 3. 🧭 Planners (`planners.py`)

**Ce que vous apprendrez :**
- Planification automatique de tâches
- Orchestration intelligente multi-étapes
- Adaptation et récupération d'erreurs
- Mémoire de planification

**Types de planners :**

#### 🎯 Basic Planner
```python
plan = await basic_planner.create_plan_async(
    "Calcule 15 + 27 puis multiplie par 3", 
    kernel
)
```
- Tâches simples et directes
- Séquence linéaire d'actions
- Idéal pour workflows basiques

#### 🔄 Sequential Planner
```python
plan = await sequential_planner.create_plan_async(
    goal="Analyse des ventes Q1 avec rapport"
)
```
- Tâches complexes multi-étapes
- Dépendances entre actions
- Orchestration intelligente

#### 🧠 Custom Planning
```python
planning_function = kernel.create_semantic_function(
    planning_template,
    function_name="CustomPlanner"
)
```
- Logique de planification personnalisée
- Adaptation au domaine spécifique
- Intelligence contextuelle

#### 🔄 Adaptive Planning
```python
# Récupération d'erreurs et adaptation
if execution_failed:
    new_plan = await adaptive_planner.create_plan_async(
        original_task, failed_context
    )
```

#### 🧠 Memory-based Planning
```python
# Planification basée sur l'historique
plan = await memory_planner.create_plan_async(
    new_task, task_history
)
```

**Workflow de planification :**
```
Goal → Analysis → Plan → Execution → Adaptation → Success
```

**Utilisation :**
```bash
python planners.py
# Tester les différents planners (1-6)
```

### 4. 🧠 Memory Integration (`memory-integration.py`)

**Ce que vous apprendrez :**
- Types de mémoire dans Semantic Kernel
- Mémoire sémantique avec embeddings
- Persistance et récupération de contexte
- Personnalisation et préférences

**Types de mémoire :**

#### 🔍 Semantic Memory
```python
# Stockage avec embeddings
await semantic_memory.save_information_async(
    collection="knowledge",
    text="Information importante",
    id="info_1"
)

# Recherche sémantique
results = await semantic_memory.search_async(
    collection="knowledge",
    query="question",
    limit=3
)
```

#### 💬 Conversation Memory
```python
# Historique de conversation
conversation_memory = []
conversation_memory.append(f"User: {user_input}")
conversation_memory.append(f"Assistant: {response}")
```

#### 📋 Task Memory
```python
# Mémoire des tâches accomplies
task_memory = {
    "description": "Tâche X",
    "result": "Succès",
    "lessons_learned": ["Point 1", "Point 2"]
}
```

#### 👤 User Preferences
```python
# Préférences utilisateur
user_preferences = {
    "interface": {"language": "français", "theme": "dark"},
    "communication": {"tone": "professionnel"}
}
```

**Architecture mémoire :**
```
Kernel Memory
├── Semantic Memory (Embeddings + Vector Store)
├── Conversation Memory (Dialog History)
├── Task Memory (Execution History)
├── User Preferences (Personalization)
└── Skill Memory (Function Learning)
```

**Recherche multi-sources :**
```python
# Recherche dans toute la mémoire
memory_search = kernel.create_semantic_function(
    search_template,
    function_name="MemorySearch"
)
```

**Utilisation :**
```bash
python memory-integration.py
# Explorer les types de mémoire (1-6)
```

## 🎓 Projet Final - Agent Intelligent (15min)

### 🎯 **Objectif du Projet**
Intégrer planification et mémoire avancées qui démontrent la maîtrise de l'approche Microsoft Semantic Kernel.

### 📋 **Livrables Attendus**

#### ✅ **Fichiers à créer** :
- `my_intelligent_agent.py` - Agent principal avec SK
- `plugins/` - Dossier avec plugins personnalisés (min. 3)
- `memory_state.json` - État de mémoire persistante
- `README_project.md` - Documentation de votre agent

#### ✅ **Fonctionnalités obligatoires** :
1. **Plugins personnalisés** (minimum 3) :
   - Plugin spécifique à votre domaine
   - Plugin utilitaire (fichiers, calculs, etc.)
   - Plugin externe (API, web, etc.)
   - Documentation des fonctions SK

2. **Planification automatique** :
   - Sequential Planner configuré
   - Gestion d'adaptation d'erreurs
   - Plans multi-étapes complexes
   - Feedback loop pour amélioration

3. **Mémoire persistante** :
   - Mémoire sémantique avec embeddings
   - Préférences utilisateur sauvegardées
   - Historique des tâches accomplies
   - Contexte conversationnel maintenu

4. **Intégration hybride** :
   - Fonctions natives + sémantiques
   - Orchestration intelligente
   - Optimisation des appels LLM
   - Gestion d'erreurs robuste

### 📊 **Critères d'évaluation** :
- **Planification** : Plans multi-étapes cohérents
- **Mémoire** : Persistance entre sessions
- **Plugins** : Fonctionnalités modulaires
- **Performance** : < 10s pour tâches complexes

### 🎬 **Démonstration finale** :
Assistant personnel avec mémoire long-terme :
- Planification automatique de tâches complexes
- Mémorisation des préférences utilisateur
- Adaptation basée sur l'historique
- Récupération d'erreurs intelligente

### 📚 **Template de démarrage** :
```python
# my_intelligent_agent.py - Structure suggérée
class IntelligentAgent:
    def __init__(self):
        self.kernel = sk.Kernel()
        self.planner = SequentialPlanner(self.kernel)
        self.memory = SemanticTextMemory()
        self.plugins = {}
        self.user_preferences = {}
    
    def load_custom_plugins(self):
        # TODO: Charger vos plugins personnalisés
        pass
    
    def setup_memory_system(self):
        # TODO: Configuration mémoire complète
        pass
    
    def intelligent_planning(self, user_request):
        # TODO: Planification avec adaptation
        pass
    
    def execute_with_memory(self, plan):
        # TODO: Exécution avec contexte persistant
        pass
```

### 🔌 **Plugins suggérés à créer** :
- **DomainPlugin** : Spécifique à votre secteur
- **ProductivityPlugin** : Gestion tâches/calendrier
- **DataPlugin** : Traitement et analyse de données
- **CommunicationPlugin** : Email, messages, rapports

### 🧠 **Architecture Mémoire** :
```
Kernel Memory System
├── Semantic Memory (Long-term knowledge)
├── Episodic Memory (User sessions)
├── Procedural Memory (Learned skills)
└── Working Memory (Current context)
```

### 🎯 **Scénarios de test** :
1. **Planification complexe** : "Organise ma semaine de travail en optimisant ma productivité"
2. **Mémoire personnalisée** : "Rappelle-toi que je préfère les réunions le matin"
3. **Adaptation d'erreurs** : Gestion d'échecs avec plans alternatifs
4. **Plugins coordonnés** : Utilisation de plusieurs plugins ensemble

## 🎓 Exercices progressifs

### Niveau Débutant
1. **Créez votre première fonction sémantique** personnalisée
2. **Implémentez un plugin simple** pour votre domaine
3. **Testez le Basic Planner** avec des tâches simples

### Niveau Intermédiaire
1. **Développez un système de plugins** coordonnés
2. **Implémentez de la planification** adaptative
3. **Intégrez plusieurs types** de mémoire

### Niveau Avancé
1. **Créez un agent complet** avec mémoire persistante
2. **Optimisez les performances** avec caching
3. **Déployez en production** avec monitoring

## 🔧 Patterns avancés

### Pattern Plugin Ecosystem
```python
# Écosystème de plugins coordonnés
ecosystem = {
    "data": DataPlugin(),
    "communication": EmailPlugin(),
    "storage": FilePlugin(),
    "analysis": AnalyticsPlugin()
}
```

### Pattern Conditional Execution
```python
# Exécution conditionnelle intelligente
@sk_function(description="Fonction conditionnelle")
def conditional_function(self, context: SKContext) -> str:
    if context.get("condition") == "true":
        return execute_branch_a()
    return execute_branch_b()
```

### Pattern Memory Hierarchy
```python
# Hiérarchie de mémoire
class HierarchicalMemory:
    def __init__(self):
        self.short_term = []      # Session actuelle
        self.working = {}         # Tâche en cours
        self.long_term = {}       # Persistant
```

### Pattern Skill Composition
```python
# Composition de compétences
composite_skill = kernel.create_semantic_function(
    template_with_multiple_functions,
    function_name="CompositeSkill"
)
```

## 📊 Métriques de performance

### Performance kernel :
- **Latence functions** : < 1s pour natives, < 3s pour sémantiques
- **Memory retrieval** : < 500ms pour recherche sémantique
- **Planning time** : < 5s pour plans complexes
- **Token efficiency** : Optimisation des appels LLM

### Métriques mémoire :
- **Semantic search accuracy** : > 85% relevance
- **Memory persistence** : 100% après redémarrage
- **Context retention** : > 95% sur sessions longues

## 🚨 Troubleshooting

### Erreurs courantes :

**❌ "Function not found"**
```python
# Vérifiez l'import des skills
skills = kernel.import_skill(MySkills(), "MySkills")
function = skills["function_name"]
```

**❌ "Context variable missing"**
```python
# Vérifiez les paramètres requis
@sk_function_context_parameter(
    name="required_param",
    description="Parameter description"
)
```

**❌ "Planning fails"**
```python
# Simplifiez la tâche ou ajoutez plus de context
planner = SequentialPlanner(kernel, allow_missing_functions=True)
```

**❌ "Memory search empty"**
```python
# Vérifiez que la collection existe
collections = await memory_store.get_collections_async()
print("Available collections:", collections)
```

## 🔄 Best Practices

### 🎯 Design de fonctions :
- **Descriptions claires** pour le planner
- **Paramètres typés** et validés
- **Gestion d'erreurs** robuste

### 🔌 Architecture plugins :
- **Responsabilité unique** par plugin
- **Interface cohérente** entre plugins
- **Documentation complète** des fonctions

### 🧭 Planification :
- **Objectifs mesurables** et clairs
- **Feedback loops** pour adaptation
- **Fallback strategies** en cas d'échec

### 🧠 Gestion mémoire :
- **Nettoyage régulier** des données obsolètes
- **Indexation efficace** pour recherche rapide
- **Backup stratégie** pour données critiques

## 🔗 Ressources complémentaires

### Documentation officielle :
- [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/)
- [GitHub Repository](https://github.com/microsoft/semantic-kernel)
- [Samples Gallery](https://github.com/microsoft/semantic-kernel/tree/main/python/samples)

### Communauté :
- [GitHub Discussions](https://github.com/microsoft/semantic-kernel/discussions)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/semantic-kernel)

### Intégrations Microsoft :
- [Microsoft 365](https://learn.microsoft.com/en-us/semantic-kernel/integrations/microsoft-365)
- [Azure Services](https://learn.microsoft.com/en-us/semantic-kernel/integrations/azure)
- [Power Platform](https://learn.microsoft.com/en-us/semantic-kernel/integrations/power-platform)

## 💡 Cas d'usage Microsoft

### 🏢 Enterprise :
- **Microsoft Copilot** : Assistant intégré Office 365
- **Power Automate** : Workflows intelligents
- **Azure AI** : Services cloud orchestrés

### 🛠️ Development :
- **GitHub Copilot** : Assistance au développement
- **Visual Studio** : Intégration IDE
- **Azure DevOps** : CI/CD intelligent

### 📊 Analytics :
- **Power BI** : Insights automatisés
- **Azure Synapse** : Analyse de données
- **Microsoft Fabric** : Plateforme unifiée

## ⚡ Performance Tips

### 🚀 Optimisation functions :
```python
# Cache pour fonctions coûteuses
@lru_cache(maxsize=128)
def expensive_function(param):
    return compute_result(param)
```

### 💾 Optimisation mémoire :
```python
# Limite la taille des collections
await memory.save_information_async(
    collection="temp",
    text=text,
    id=id,
    additional_metadata={"ttl": 3600}  # Expiration
)
```

### 🔧 Optimisation planning :
```python
# Planner avec contraintes
planner = SequentialPlanner(
    kernel,
    max_iterations=5,  # Limite les itérations
    allow_missing_functions=False  # Strict mode
)
```

---

🎯 **Objectif final** : Maîtriser Semantic Kernel pour créer des agents IA intelligents et intégrés à l'écosystème Microsoft !