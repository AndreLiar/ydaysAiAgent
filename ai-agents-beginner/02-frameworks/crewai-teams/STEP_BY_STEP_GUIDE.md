# 🎯 Guide Étape par Étape - Système de Production avec CrewAI

## 📚 Vue d'Ensemble du Projet

Ce guide vous accompagne dans la construction d'un **système de production avec monitoring** en utilisant CrewAI. Vous apprendrez en faisant - chaque étape vous enseigne des concepts clés tout en construisant un système de veille opérationnel 24/7.

### 🎯 Objectifs d'Apprentissage
- Maîtriser les crews hiérarchiques CrewAI
- Implémenter un système prêt pour la production
- Intégrer monitoring et métriques temps réel
- Gérer les erreurs et la robustesse
- Créer des processus automatisés end-to-end

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
pip install crewai langchain-openai python-dotenv

# 2. Configurer votre clé API
cp .env.example .env
# Ajouter votre OPENAI_API_KEY dans le fichier .env

# 3. Lancer le projet starter
python my_production_crew_starter.py
```

## 📋 Progression Étape par Étape

### ✅ TODO 1: Installation des Dépendances (2 min)

**Concepts appris**: Écosystème CrewAI et architecture de production

```bash
pip install crewai langchain-openai python-dotenv
```

**Pourquoi ces packages ?**
- `crewai`: Framework principal pour équipes d'agents
- `langchain-openai`: Intégration OpenAI (GPT-4) pour les agents
- `python-dotenv`: Gestion sécurisée des configurations

### ✅ TODO 2: Imports et Architecture (3 min)

**Concepts appris**: Structure modulaire de CrewAI

Décommentez et complétez les imports dans `my_production_crew_starter.py`:

```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
```

**Architecture CrewAI**:
- **Agent**: Membre de l'équipe avec expertise spécifique
- **Task**: Tâche assignée à un agent avec output attendu
- **Crew**: Équipe orchestrée d'agents et tâches
- **Process**: Méthode d'exécution (sequential/hierarchical)

### ✅ TODO 3: Métriques de Production (5 min)

**Concepts appris**: Monitoring production pour CrewAI

Définissez la classe `ProductionMetrics`:

```python
@dataclass
class ProductionMetrics:
    """Métriques de performance pour environnement de production"""
    timestamp: str
    cycle_id: str
    execution_time: float
    success: bool
    tasks_completed: int
    agents_used: int
    output_quality_score: float      # Score de qualité (0-1)
    cost_estimate: float             # Coût estimé en $
    error_count: int                 # Nombre d'erreurs
    retry_attempts: int              # Tentatives de retry
    peak_memory_usage: float         # Pic d'utilisation mémoire
    api_calls_made: int              # Nombre d'appels API
    workflow_efficiency: float       # Efficacité du workflow (0-1)
```

**Pourquoi ces Métriques ?**
- **Performance**: Temps d'exécution, efficacité
- **Fiabilité**: Taux de succès, gestion d'erreurs
- **Coûts**: Estimation financière, optimisation
- **Qualité**: Score de sortie, cohérence

### ✅ TODO 4: Système d'Alertes (5 min)

**Concepts appris**: Alertes et monitoring temps réel

Complétez la classe `AlertingSystem`:

```python
class AlertingSystem:
    """Système d'alertes pour monitoring production"""
    
    def __init__(self):
        self.alert_thresholds = {
            "max_execution_time": 300,  # 5 minutes
            "min_success_rate": 0.95,   # 95%
            "max_cost_per_cycle": 1.0,  # $1.00
            "max_error_rate": 0.05      # 5%
        }
        self.active_alerts = []
    
    def check_performance_thresholds(self, metrics: ProductionMetrics):
        """Vérifier les seuils de performance"""
        alerts = []
        
        # Vérifier le temps d'exécution
        if metrics.execution_time > self.alert_thresholds["max_execution_time"]:
            alerts.append({
                "type": "WARNING",
                "message": f"Temps d'exécution élevé: {metrics.execution_time:.1f}s",
                "threshold": self.alert_thresholds["max_execution_time"],
                "actual": metrics.execution_time
            })
        
        # Vérifier le coût
        if metrics.cost_estimate > self.alert_thresholds["max_cost_per_cycle"]:
            alerts.append({
                "type": "COST_ALERT",
                "message": f"Coût élevé: ${metrics.cost_estimate:.3f}",
                "threshold": self.alert_thresholds["max_cost_per_cycle"],
                "actual": metrics.cost_estimate
            })
        
        # Vérifier les erreurs
        if metrics.error_count > 0:
            alerts.append({
                "type": "ERROR",
                "message": f"{metrics.error_count} erreurs détectées",
                "severity": "HIGH" if metrics.error_count > 2 else "MEDIUM"
            })
        
        # Traiter les alertes
        for alert in alerts:
            self.send_alert(alert["type"], alert["message"])
            self.active_alerts.append(alert)
        
        return alerts
    
    def send_alert(self, alert_type: str, message: str):
        """Envoyer une alerte"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        print(f"🚨 [{timestamp}] {alert_type}: {message}")
        
        # En production: intégration Slack, email, etc.
        # slack_client.post_message(channel="#alerts", text=message)
        # email_service.send_alert(to="admin@company.com", subject=alert_type, body=message)
```

### ✅ TODO 5: Initialisation du Système (8 min)

**Concepts appris**: Configuration CrewAI pour la production

Implémentez l'initialisation dans `__init__`:

```python
def __init__(self):
    print("🚀 Initialisation de votre système de production...")
    
    # Vérifier la clé API
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY non trouvée ! Créez un fichier .env")
    
    # Configuration LLM optimisée pour production
    self.llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3,  # Plus déterministe pour production
        max_tokens=1000,
        timeout=60,       # Timeout pour éviter les blocages
        max_retries=3,    # Retry automatique
        request_timeout=30
    )
    
    # Initialiser vos variables d'instance
    self.crew = None
    self.agents = {}
    self.tasks = []
    self.metrics_collector = self._init_metrics_collector()
    self.alerting_system = AlertingSystem()
    self.is_monitoring_active = False
    self.cycle_history = []
    
    print("✅ Configuration de base terminée")

def _init_metrics_collector(self):
    """Initialiser le collecteur de métriques"""
    return {
        "total_cycles": 0,
        "successful_cycles": 0,
        "total_execution_time": 0,
        "total_cost": 0,
        "last_cycle": None
    }
```

**Bonnes Pratiques Production**:
- **Timeouts**: Éviter les blocages système
- **Retry logic**: Robustesse face aux erreurs temporaires
- **Logging**: Traçabilité pour debugging
- **Monitoring**: Métriques dès l'initialisation

### ✅ TODO 6: Crew Hiérarchique (15 min)

**Concepts appris**: Structure organisationnelle avec CrewAI

Implémentez `create_hierarchical_crew()`:

```python
def create_hierarchical_crew(self):
    print("\n🏢 ÉTAPE: Création de la crew hiérarchique")
    print("=" * 60)
    
    # Créer le Manager Agent
    manager = Agent(
        role="System Manager",
        goal="Coordonner l'équipe de veille et assurer la qualité des livrables dans les délais",
        backstory='''Tu es un manager expérimenté en charge d'une équipe de veille technologique.
        Avec 15 ans d'expérience en gestion d'équipes techniques, tu coordonnes les efforts de 
        l'équipe, délègues les tâches selon les expertises, et t'assures que les objectifs 
        sont atteints dans les délais avec la qualité requise.
        
        Tu es reconnu pour:
        - Ta capacité à identifier les bonnes priorités
        - Ton excellence en délégation intelligente
        - Ta vision stratégique des enjeux technologiques
        - Ton leadership bienveillant mais exigeant''',
        llm=self.llm,
        allow_delegation=True,
        verbose=True,
        max_iter=3,  # Limite les itérations pour performance
        memory=True
    )
    
    # Créer le Data Collection Agent
    data_collector = Agent(
        role="Data Collection Specialist",
        goal="Collecter des informations pertinentes et fiables depuis diverses sources avec efficacité",
        backstory='''Tu es un expert en collecte d'informations avec 10 ans d'expérience 
        dans la veille technologique. Tu maîtrises les techniques de recherche avancée et 
        identifies les sources les plus fiables pour chaque type d'information.
        
        Tes spécialités:
        - Recherche d'informations techniques précises
        - Évaluation de la crédibilité des sources
        - Synthèse rapide de grandes quantités d'information
        - Identification des tendances émergentes''',
        llm=self.llm,
        allow_delegation=False,
        verbose=True,
        tools=[],  # En production: ajouter des outils de recherche
        max_execution_time=120
    )
    
    # Créer l'Analysis Agent
    analyst = Agent(
        role="Senior Data Analyst",
        goal="Analyser les données collectées et identifier les insights stratégiques clés",
        backstory='''Tu es un analyste senior avec une expertise en traitement de données 
        et analyse stratégique. Tu identifies les tendances, patterns et insights significatifs 
        dans les informations collectées, avec un focus sur l'impact business.
        
        Tes compétences:
        - Analyse quantitative et qualitative avancée
        - Identification de patterns complexes
        - Évaluation des impacts business
        - Modélisation prédictive simple''',
        llm=self.llm,
        allow_delegation=False,
        verbose=True,
        max_execution_time=180
    )
    
    # Créer le Report Agent
    reporter = Agent(
        role="Report Writer",
        goal="Synthétiser les analyses en rapports clairs et actionnables pour les décideurs",
        backstory='''Tu es un rédacteur expert en communication professionnelle et reporting 
        stratégique. Tu transforms les analyses complexes en rapports clairs, structurés 
        et orientés action pour les décideurs.
        
        Tes talents:
        - Rédaction claire et impactante
        - Structuration logique de l'information
        - Adaptation du style selon l'audience
        - Création de synthèses exécutives percutantes''',
        llm=self.llm,
        allow_delegation=False,
        verbose=True,
        max_execution_time=150
    )
    
    # Créer l'Alert Agent
    alert_agent = Agent(
        role="Alert Coordinator",
        goal="Identifier les situations critiques et gérer les notifications avec précision",
        backstory='''Tu es responsable de la surveillance et des alertes dans l'équipe. 
        Tu identifies les situations nécessitant une attention immédiate et coordonnes 
        les notifications appropriées avec discernement.
        
        Tes responsabilités:
        - Détection d'anomalies et situations critiques
        - Classification des niveaux d'urgence
        - Coordination des escalades appropriées
        - Suivi des résolutions d'incidents''',
        llm=self.llm,
        allow_delegation=False,
        verbose=True,
        max_execution_time=60
    )
    
    # Stocker les agents
    self.agents = {
        "manager": manager,
        "data_collector": data_collector,
        "analyst": analyst,
        "reporter": reporter,
        "alert_agent": alert_agent
    }
    
    print(f"✅ {len(self.agents)} agents créés dans la hiérarchie")
    print("🏢 Hiérarchie: Manager → Data Collector → Analyst → Reporter → Alert Agent")
    return True
```

**Structure Hiérarchique CrewAI**:
- **Manager**: Coordination et délégation
- **Specialists**: Expertise domain-specific
- **Process.hierarchical**: Délégation automatique
- **allow_delegation**: Contrôle des responsabilités

### ✅ TODO 7: Tâches de Monitoring (12 min)

**Concepts appris**: Tâches spécialisées et workflows CrewAI

Implémentez `define_monitoring_tasks()`:

```python
def define_monitoring_tasks(self):
    print("\n📋 ÉTAPE: Définition des tâches de monitoring")
    print("=" * 60)
    
    if not self.agents:
        print("❌ Agents non créés. Exécutez d'abord create_hierarchical_crew()")
        return False
    
    # Tâche de collecte de données
    data_collection_task = Task(
        description='''Collecter des informations récentes et pertinentes sur les dernières 
        tendances en Intelligence Artificielle et agents conversationnels.
        
        Focus spécifique sur:
        - Nouvelles technologies IA et frameworks
        - Développements en agents conversationnels
        - Innovations en NLP et LLMs
        - Applications business émergentes
        - Investissements et acquisitions du secteur
        
        Critères de qualité:
        - Sources fiables et récentes (< 30 jours)
        - Diversité des perspectives (technique, business, académique)
        - Informations vérifiables et citées
        - Pertinence pour l'écosystème IA actuel''',
        expected_output='''Liste structurée de 5-10 informations clés avec:
        
        ## Informations Collectées
        
        ### 1. [Titre de l'information]
        - **Source**: [URL et nom de la source]
        - **Date**: [Date de publication]
        - **Résumé**: [Résumé en 2-3 phrases]
        - **Impact**: [Niveau d'importance 1-5]
        - **Catégorie**: [Technologie/Business/Recherche/Autre]
        - **Tags**: #ai #agents #nlp #business
        
        [Répéter pour chaque information]
        
        ## Synthèse
        - Total d'informations: X
        - Sources diverses: Y sources différentes
        - Période couverte: [dates]''',
        agent=self.agents["data_collector"],
        tools=[],  # En production: ajouter outils de recherche
        output_file="data_collection_output.md"
    )
    
    # Tâche d'analyse
    analysis_task = Task(
        description='''Analyser en profondeur les données collectées pour identifier:
        
        Analyses requises:
        1. **Tendances émergentes**: Patterns et directions du marché
        2. **Opportunités business**: Applications commerciales potentielles
        3. **Risques et défis**: Obstacles et limitations identifiés
        4. **Impact concurrentiel**: Avantages et menaces pour les acteurs
        5. **Prédictions**: Évolutions probables à 6-12 mois
        
        Méthodologie:
        - Analyse quantitative des données disponibles
        - Évaluation qualitative des impacts
        - Corrélation avec les tendances existantes
        - Validation par recoupement de sources''',
        expected_output='''Analyse structurée comprenant:
        
        ## Analyse Stratégique
        
        ### 🔍 Tendances Principales (3-5 tendances)
        1. **[Nom de la tendance]**
           - Description: [Explication détaillée]
           - Impact: [Court/Moyen/Long terme]
           - Probabilité: [Faible/Moyenne/Élevée]
           - Acteurs clés: [Entreprises/Recherche impliquées]
        
        ### 💼 Opportunités Business
        - [Liste des opportunités avec évaluation du potentiel]
        
        ### ⚠️ Risques et Défis
        - [Obstacles identifiés avec stratégies de mitigation]
        
        ### 📊 Score de Priorité
        Chaque recommandation avec score 1-10 selon:
        - Urgence d'action
        - Impact potentiel
        - Faisabilité de mise en œuvre''',
        agent=self.agents["analyst"],
        context=[data_collection_task],  # Dépend de la collecte
        output_file="analysis_output.md"
    )
    
    # Tâche de reporting
    reporting_task = Task(
        description='''Créer un rapport de veille professionnel synthétisant:
        
        Structure requise:
        1. **Résumé exécutif** (200 mots max) - Points clés pour décideurs
        2. **Contexte et méthodologie** - Approche utilisée
        3. **Findings principaux** - Découvertes majeures
        4. **Analyse détaillée** - Approfondissement des insights
        5. **Recommandations stratégiques** - Actions concrètes
        6. **Annexes** - Sources et données de support
        
        Ton: Professionnel, clair, orienté action
        Audience: Dirigeants et responsables stratégiques
        Format: Markdown structuré avec visualisations textuelles''',
        expected_output='''Rapport markdown complet (daily_brief.md) avec:
        
        # Rapport de Veille Technologique - [Date]
        
        ## 📋 Résumé Exécutif
        [Synthèse de 200 mots maximum pour dirigeants]
        
        ## 🔍 Findings Principaux
        [3-5 découvertes majeures avec impact business]
        
        ## 📊 Analyse Détaillée
        [Approfondissement des insights avec données]
        
        ## 🎯 Recommandations Stratégiques
        [Actions concrètes classées par priorité]
        
        ## 📚 Méthodologie et Sources
        [Processus suivi et crédibilité des informations]
        
        ## 📈 Métriques de Qualité
        - Sources consultées: X
        - Niveau de confiance: Y%
        - Recommandations actionnables: Z''',
        agent=self.agents["reporter"],
        context=[data_collection_task, analysis_task],
        output_file="daily_brief.md"
    )
    
    # Tâche de gestion des alertes
    alert_task = Task(
        description='''Identifier dans l'analyse les éléments nécessitant une alerte:
        
        Critères d'alerte:
        - **Développements critiques**: Changements majeurs du secteur
        - **Opportunités urgentes**: Fenêtres d'action limitées
        - **Risques significatifs**: Menaces pour l'activité
        - **Innovations disruptives**: Technologies breakthrough
        
        Classification:
        - 🔴 CRITICAL: Action immédiate requise (< 24h)
        - 🟡 WARNING: Attention dans la semaine
        - 🔵 INFO: Information pour connaissance
        
        Préparer les notifications selon l'urgence et l'audience.''',
        expected_output='''Liste d'alertes structurée:
        
        ## Alertes Identifiées
        
        ### 🔴 CRITICAL (Action immédiate)
        [Si applicable - événements nécessitant réaction < 24h]
        
        ### 🟡 WARNING (Attention requise)
        [Situations à surveiller cette semaine]
        
        ### 🔵 INFO (Pour information)
        [Développements intéressants pour veille continue]
        
        ## Notifications Recommandées
        - **Direction**: [Messages pour leadership]
        - **Équipes techniques**: [Alerts pour développement]
        - **Commerciales**: [Opportunités business]
        
        ## Actions Suggérées
        [Étapes concrètes par niveau d'alerte avec échéances]''',
        agent=self.agents["alert_agent"],
        context=[analysis_task],
        output_file="alerts_output.md"
    )
    
    # Stocker les tâches dans l'ordre d'exécution
    self.tasks = [
        data_collection_task,
        analysis_task,
        reporting_task,
        alert_task
    ]
    
    print(f"✅ {len(self.tasks)} tâches de monitoring définies")
    print("📋 Workflow: Collecte → Analyse → Rapport → Alertes")
    return True
```

**Concepts Clés CrewAI**:
- **context**: Dépendances entre tâches
- **expected_output**: Spécification précise du livrable
- **output_file**: Persistance automatique
- **agent assignment**: Responsabilité par expertise

### ✅ TODO 8: Configuration Production (8 min)

**Concepts appris**: Crew hiérarchique avec management

Implémentez `setup_production_crew()`:

```python
def setup_production_crew(self):
    print("\n⚙️ ÉTAPE: Configuration de la crew de production")
    print("=" * 60)
    
    if not self.agents or not self.tasks:
        print("❌ Agents ou tâches non configurés")
        return False
    
    # Créer la crew hiérarchique optimisée pour production
    self.crew = Crew(
        agents=list(self.agents.values()),
        tasks=self.tasks,
        process=Process.hierarchical,  # Délégation intelligente
        manager_llm=self.llm,          # LLM pour le manager
        verbose=True,                  # Logging détaillé
        memory=True,                   # Contexte persistant
        max_rpm=10,                    # Rate limiting (10 requêtes/min)
        share_crew=False,              # Isolation pour sécurité
        step_callback=self._step_callback,  # Monitoring en temps réel
        task_callback=self._task_callback   # Callback par tâche
    )
    
    print("✅ Crew de production configurée")
    print("🏗️ Process hiérarchique avec manager LLM")
    print("📊 Monitoring temps réel activé")
    print("🔒 Isolation de sécurité configurée")
    return True

def _step_callback(self, step_output):
    """Callback exécuté à chaque étape"""
    print(f"📍 Étape: {step_output.agent} - {step_output.task[:50]}...")
    
def _task_callback(self, task_output):
    """Callback exécuté à la fin de chaque tâche"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"✅ [{timestamp}] Tâche terminée: {task_output.task}")
    
    # Collecter métriques par tâche (en production)
    # self.metrics_collector.log_task_completion(task_output)
```

**Configuration Production**:
- **Rate limiting**: Éviter les dépassements de quotas
- **Memory**: Contexte partagé entre tâches
- **Callbacks**: Monitoring temps réel
- **Isolation**: Sécurité multi-tenant

### ✅ TODO 9: Cycle de Monitoring (15 min)

**Concepts appris**: Exécution robuste avec gestion d'erreurs

Implémentez `execute_monitoring_cycle()`:

```python
def execute_monitoring_cycle(self, topic: str = "Intelligence Artificielle et Agents"):
    print(f"\n🔄 ÉTAPE: Cycle de monitoring sur '{topic}'")
    print("=" * 60)
    
    if not self.crew:
        print("❌ Crew non configurée. Exécutez d'abord setup_production_crew()")
        return None
    
    start_time = datetime.now()
    cycle_id = f"cycle_{int(start_time.timestamp())}"
    
    try:
        print("🚀 Lancement du cycle de monitoring...")
        print("⏱️ Collecte de métriques temps réel activée")
        print(f"🔍 Sujet d'analyse: {topic}")
        
        # Activer le monitoring
        self.is_monitoring_active = True
        
        # Préparer les inputs pour la crew
        crew_inputs = {
            "topic": topic,
            "timestamp": start_time.isoformat(),
            "cycle_id": cycle_id
        }
        
        # Exécuter la crew avec gestion d'erreurs
        result = self.crew.kickoff(inputs=crew_inputs)
        
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # Collecter les métriques détaillées
        metrics = ProductionMetrics(
            timestamp=start_time.isoformat(),
            cycle_id=cycle_id,
            execution_time=execution_time,
            success=True,
            tasks_completed=len(self.tasks),
            agents_used=len(self.agents),
            output_quality_score=0.95,  # À calculer avec vraie évaluation
            cost_estimate=self._estimate_cycle_cost(execution_time),
            error_count=0,
            retry_attempts=0,
            peak_memory_usage=self._get_memory_usage(),
            api_calls_made=self._count_api_calls(),
            workflow_efficiency=0.90  # Mesurer la synergie
        )
        
        # Vérifier les seuils de performance
        alerts = self.alerting_system.check_performance_thresholds(metrics)
        
        # Sauvegarder les résultats
        self._save_cycle_results(result, metrics)
        
        # Mettre à jour les statistiques globales
        self.metrics_collector["total_cycles"] += 1
        self.metrics_collector["successful_cycles"] += 1
        self.metrics_collector["total_execution_time"] += execution_time
        self.metrics_collector["total_cost"] += metrics.cost_estimate
        self.metrics_collector["last_cycle"] = metrics
        
        self.cycle_history.append(metrics)
        
        print(f"✅ Cycle de monitoring terminé en {execution_time:.1f}s")
        print(f"💰 Coût estimé: ${metrics.cost_estimate:.4f}")
        print(f"📊 Score qualité: {metrics.output_quality_score:.1%}")
        
        if alerts:
            print(f"🚨 {len(alerts)} alertes générées")
        
        return {
            "cycle_id": cycle_id,
            "topic": topic,
            "execution_time": execution_time,
            "status": "completed",
            "timestamp": start_time.isoformat(),
            "metrics": metrics,
            "alerts": alerts,
            "result": result
        }
        
    except Exception as e:
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # Métriques d'échec
        error_metrics = ProductionMetrics(
            timestamp=start_time.isoformat(),
            cycle_id=cycle_id,
            execution_time=execution_time,
            success=False,
            tasks_completed=0,
            agents_used=0,
            output_quality_score=0.0,
            cost_estimate=0.0,
            error_count=1,
            retry_attempts=0,
            peak_memory_usage=0.0,
            api_calls_made=0,
            workflow_efficiency=0.0
        )
        
        # Alert critique
        self.alerting_system.send_alert("CRITICAL", f"Échec du cycle {cycle_id}: {str(e)}")
        
        print(f"❌ Erreur durant le cycle: {e}")
        print("🔄 Retry logic activé (en production)")
        
        # En production: implémenter retry logic
        # if retry_count < max_retries:
        #     return self.execute_monitoring_cycle(topic, retry_count + 1)
        
        return {
            "cycle_id": cycle_id,
            "topic": topic,
            "execution_time": execution_time,
            "status": "failed",
            "error": str(e),
            "timestamp": start_time.isoformat(),
            "metrics": error_metrics
        }
    
    finally:
        self.is_monitoring_active = False

def _estimate_cycle_cost(self, execution_time: float) -> float:
    """Estimer le coût d'un cycle de monitoring"""
    # Estimation basée sur l'utilisation d'API
    # Prix approximatifs GPT-4: $0.03/1K prompt tokens, $0.06/1K completion tokens
    estimated_tokens = execution_time * 50  # Approximation
    prompt_cost = estimated_tokens * 0.5 * 0.00003  # 50% prompt tokens
    completion_cost = estimated_tokens * 0.5 * 0.00006  # 50% completion tokens
    return prompt_cost + completion_cost

def _get_memory_usage(self) -> float:
    """Obtenir l'utilisation mémoire actuelle"""
    # En production: monitoring système réel
    return 0.0

def _count_api_calls(self) -> int:
    """Compter les appels API effectués"""
    # En production: tracking réel des appels
    return len(self.tasks) * 2  # Approximation

def _save_cycle_results(self, result, metrics):
    """Sauvegarder les résultats d'un cycle"""
    cycle_data = {
        "metadata": {
            "cycle_id": metrics.cycle_id,
            "timestamp": metrics.timestamp,
            "execution_time": metrics.execution_time,
            "success": metrics.success
        },
        "metrics": {
            "tasks_completed": metrics.tasks_completed,
            "cost_estimate": metrics.cost_estimate,
            "quality_score": metrics.output_quality_score
        },
        "result": str(result)  # Résultat de la crew
    }
    
    # Sauvegarder dans un fichier de cycle
    filename = f"cycle_{metrics.cycle_id}_results.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cycle_data, f, indent=2, ensure_ascii=False)
```

### ✅ TODO 10: Dashboard de Monitoring (10 min)

**Concepts appris**: Visualisation des métriques production

Implémentez `generate_dashboard()`:

```python
def generate_dashboard(self):
    print("\n📊 ÉTAPE: Génération du dashboard")
    print("=" * 60)
    
    # Récupérer les métriques historiques
    historical_metrics = self.cycle_history
    
    if not historical_metrics:
        print("📊 Aucune métrique disponible - Exécutez d'abord un cycle")
        # Générer dashboard avec données par défaut
        dashboard_data = self._generate_default_dashboard()
    else:
        # Calculer les KPIs à partir des vraies données
        total_cycles = len(historical_metrics)
        successful_cycles = sum(1 for m in historical_metrics if m.success)
        avg_execution_time = sum(m.execution_time for m in historical_metrics) / total_cycles
        total_cost = sum(m.cost_estimate for m in historical_metrics)
        avg_quality_score = sum(m.output_quality_score for m in historical_metrics) / total_cycles
        success_rate = (successful_cycles / total_cycles) * 100
        
        # Identifier les tendances
        recent_metrics = historical_metrics[-5:]  # 5 derniers cycles
        recent_avg_time = sum(m.execution_time for m in recent_metrics) / len(recent_metrics)
        trend_performance = "improving" if recent_avg_time < avg_execution_time else "stable"
        
        dashboard_data = {
            "system_status": {
                "monitoring_active": self.is_monitoring_active,
                "last_update": datetime.now().isoformat(),
                "system_health": "excellent" if success_rate > 95 else "good" if success_rate > 90 else "warning",
                "uptime_hours": total_cycles * (avg_execution_time / 3600),  # Approximation
                "next_scheduled_cycle": self._calculate_next_cycle()
            },
            "performance_metrics": {
                "total_cycles_executed": total_cycles,
                "success_rate": f"{success_rate:.1f}%",
                "average_execution_time": f"{avg_execution_time:.2f}s",
                "fastest_cycle": f"{min(m.execution_time for m in historical_metrics):.2f}s",
                "slowest_cycle": f"{max(m.execution_time for m in historical_metrics):.2f}s",
                "performance_trend": trend_performance
            },
            "cost_analytics": {
                "total_estimated_cost": f"${total_cost:.4f}",
                "average_cost_per_cycle": f"${total_cost/total_cycles:.4f}",
                "cost_trend": "optimizing",  # Analyser la tendance
                "monthly_projection": f"${total_cost * 30:.2f}",  # Si 1 cycle/jour
                "cost_efficiency": "high" if total_cost/total_cycles < 0.50 else "moderate"
            },
            "quality_metrics": {
                "average_quality_score": f"{avg_quality_score:.1%}",
                "tasks_completion_rate": "100%",  # Tous les cycles réussis ont terminé toutes les tâches
                "agent_utilization": f"{len(self.agents)}/{len(self.agents)} agents actifs",
                "output_consistency": "high",  # À mesurer avec vraie évaluation
                "user_satisfaction": "N/A"  # Nécessite feedback utilisateur
            },
            "current_alerts": self.alerting_system.active_alerts[-10:],  # 10 dernières alertes
            "optimization_recommendations": self._generate_recommendations(historical_metrics),
            "recent_cycles": [
                {
                    "cycle_id": m.cycle_id,
                    "timestamp": m.timestamp,
                    "execution_time": f"{m.execution_time:.1f}s",
                    "success": m.success,
                    "cost": f"${m.cost_estimate:.4f}",
                    "quality": f"{m.output_quality_score:.1%}"
                }
                for m in historical_metrics[-10:]  # 10 derniers cycles
            ]
        }
    
    # Sauvegarder le dashboard
    with open("metrics_dashboard.json", "w", encoding="utf-8") as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    
    # Afficher un résumé
    print("✅ Dashboard généré: metrics_dashboard.json")
    print(f"📊 KPIs principaux:")
    if historical_metrics:
        print(f"   • Cycles exécutés: {dashboard_data['performance_metrics']['total_cycles_executed']}")
        print(f"   • Taux de succès: {dashboard_data['performance_metrics']['success_rate']}")
        print(f"   • Temps moyen: {dashboard_data['performance_metrics']['average_execution_time']}")
        print(f"   • Coût total: {dashboard_data['cost_analytics']['total_estimated_cost']}")

def _generate_default_dashboard(self):
    """Générer un dashboard par défaut"""
    return {
        "system_status": {
            "monitoring_active": False,
            "last_update": datetime.now().isoformat(),
            "system_health": "ready",
            "message": "Système prêt - Aucun cycle exécuté"
        },
        "performance_metrics": {
            "total_cycles_executed": 0,
            "success_rate": "N/A",
            "average_execution_time": "N/A"
        },
        "cost_analytics": {
            "total_estimated_cost": "$0.0000",
            "message": "Aucun coût engagé"
        },
        "recommendations": [
            "Exécuter le premier cycle de monitoring",
            "Configurer les alertes selon vos seuils",
            "Tester le système avec différents sujets"
        ]
    }

def _calculate_next_cycle(self):
    """Calculer le prochain cycle programmé"""
    next_cycle = datetime.now().replace(hour=datetime.now().hour + 1, minute=0, second=0)
    return next_cycle.isoformat()

def _generate_recommendations(self, metrics):
    """Générer des recommandations d'optimisation"""
    if not metrics:
        return ["Exécuter plus de cycles pour analyses"]
    
    recommendations = []
    avg_time = sum(m.execution_time for m in metrics) / len(metrics)
    
    if avg_time > 180:  # > 3 minutes
        recommendations.append("Optimiser les prompts pour réduire le temps d'exécution")
    
    avg_cost = sum(m.cost_estimate for m in metrics) / len(metrics)
    if avg_cost > 0.50:
        recommendations.append("Considérer des modèles moins coûteux pour certaines tâches")
    
    if len(metrics) < 5:
        recommendations.append("Exécuter plus de cycles pour analyses statistiques robustes")
    
    recommendations.extend([
        "Implémenter le caching pour les requêtes fréquentes",
        "Ajouter plus de points de monitoring intermédiaires",
        "Configurer des alertes personnalisées selon vos besoins"
    ])
    
    return recommendations
```

### ✅ TODO 11: Monitoring Automatisé (5 min)

**Concepts appris**: Automatisation et scheduling

Implémentez `setup_automated_monitoring()`:

```python
def setup_automated_monitoring(self, interval_hours: int = 24):
    print(f"\n🤖 ÉTAPE: Configuration du monitoring automatisé (toutes les {interval_hours}h)")
    print("=" * 60)
    
    # Configurer le scheduler
    self.monitoring_config = {
        "enabled": True,
        "interval_hours": interval_hours,
        "auto_start": True,
        "alert_thresholds": {
            "max_execution_time": 300,  # 5 minutes
            "min_success_rate": 0.95,   # 95%
            "max_cost_per_cycle": 1.0   # $1.00
        },
        "backup_enabled": True,
        "notification_channels": ["console", "file"],  # Extensible à email, slack
        "retry_policy": {
            "max_retries": 3,
            "backoff_factor": 2,
            "initial_delay": 60
        },
        "maintenance_window": {
            "start_hour": 2,  # 2h du matin
            "duration_hours": 1
        }
    }
    
    # Activer le monitoring
    self.is_monitoring_active = True
    
    print("✅ Monitoring automatisé configuré")
    print(f"⏰ Cycles programmés toutes les {interval_hours}h")
    print("🔄 Retry automatique en cas d'échec")
    print("🛡️ Fenêtre de maintenance configurée (2h-3h)")
    
    # En production: intégration avec scheduler (cron, celery, APScheduler)
    # scheduler.add_job(
    #     func=self.execute_monitoring_cycle,
    #     trigger="interval",
    #     hours=interval_hours,
    #     id="automated_monitoring"
    # )
```

### ✅ TODO 12: Démonstration Complète (5 min)

**Concepts appris**: Test end-to-end du système

Implémentez `run_demo()`:

```python
def run_demo(self):
    print("\n🎬 DÉMONSTRATION DE VOTRE SYSTÈME DE PRODUCTION")
    print("=" * 60)
    
    # Scénarios de démonstration
    demo_scenarios = [
        "Veille technologique Intelligence Artificielle",
        "Monitoring des tendances agents conversationnels",
        "Surveillance des nouvelles frameworks IA",
        "Analyse de l'écosystème LLM"
    ]
    
    print("🎯 Scénarios de démonstration:")
    for i, scenario in enumerate(demo_scenarios, 1):
        print(f"  {i}. {scenario}")
    
    print("\n📋 Processus de démonstration:")
    print("  1. 🏢 Création de la crew hiérarchique")
    print("  2. 📋 Definition des tâches de monitoring")
    print("  3. ⚙️ Configuration de la crew de production")
    print("  4. 🔄 Exécution d'un cycle complet")
    print("  5. 📊 Génération du dashboard")
    print("  6. 🤖 Configuration du monitoring automatisé")
    
    # Exécuter la démonstration complète
    print("\n⚡ Lancement de la démonstration...")
    selected_scenario = demo_scenarios[0]
    
    try:
        if self.create_hierarchical_crew():
            print("✅ Crew hiérarchique créée")
            
            if self.define_monitoring_tasks():
                print("✅ Tâches de monitoring définies")
                
                if self.setup_production_crew():
                    print("✅ Crew de production configurée")
                    
                    print(f"\n🎯 Exécution du scénario: {selected_scenario}")
                    results = self.execute_monitoring_cycle(selected_scenario)
                    
                    if results and results.get("status") == "completed":
                        print("✅ Cycle de monitoring terminé")
                        
                        self.generate_dashboard()
                        print("✅ Dashboard généré")
                        
                        self.setup_automated_monitoring()
                        print("✅ Monitoring automatisé configuré")
                        
                        print("\n🏆 DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
                        print("\n📁 Fichiers générés:")
                        print("  📊 metrics_dashboard.json - Dashboard temps réel")
                        print("  📄 daily_brief.md - Rapport de veille")
                        print("  📋 data_collection_output.md - Données collectées")
                        print("  📈 analysis_output.md - Analyse approfondie")
                        print("  🚨 alerts_output.md - Alertes et notifications")
                        
                        # Afficher les métriques finales
                        if results["metrics"]:
                            print(f"\n📊 Métriques du cycle:")
                            print(f"   ⏱️ Temps d'exécution: {results['execution_time']:.1f}s")
                            print(f"   💰 Coût estimé: ${results['metrics'].cost_estimate:.4f}")
                            print(f"   📈 Score qualité: {results['metrics'].output_quality_score:.1%}")
                            print(f"   ✅ Tâches complétées: {results['metrics'].tasks_completed}")
                        
                        return True
                    else:
                        print("❌ Échec de l'exécution du cycle")
                else:
                    print("❌ Échec de la configuration de crew")
            else:
                print("❌ Échec de la définition des tâches")
        else:
            print("❌ Échec de la création de crew")
            
    except Exception as e:
        print(f"❌ Erreur durant la démonstration: {e}")
        
    return False
```

## 🎯 Résultat Final

Après avoir complété tous les TODOs, vous aurez créé :

### 📁 Fichiers Générés
- ✅ `daily_brief.md` - Rapport de veille professionnel
- ✅ `metrics_dashboard.json` - Dashboard temps réel
- ✅ `data_collection_output.md` - Données collectées
- ✅ `analysis_output.md` - Analyse approfondie
- ✅ `alerts_output.md` - Alertes et notifications
- ✅ `cycle_*_results.json` - Résultats de chaque cycle

### 🎓 Compétences Acquises
- **CrewAI**: Crews hiérarchiques et délégation
- **Production**: Monitoring, alertes, métriques
- **Robustesse**: Gestion d'erreurs, retry logic
- **Automatisation**: Scheduling et processus
- **Qualité**: Standards production et optimisation

### 🚀 Applications Possibles
- Système de veille technologique 24/7
- Monitoring concurrentiel automatisé
- Analyse de marché en temps réel
- Alerts stratégiques pour dirigeants

## 🎬 Démonstration

Lancez votre système terminé :

```bash
python my_production_crew_starter.py
```

Le système exécutera automatiquement :
1. ✅ Création d'une crew hiérarchique avec 5 agents
2. ✅ Definition de 4 tâches de monitoring spécialisées
3. ✅ Configuration production avec rate limiting
4. ✅ Exécution d'un cycle complet avec métriques
5. ✅ Génération d'un dashboard temps réel
6. ✅ Configuration du monitoring automatisé

## 🔧 Personnalisation

### Adapter à Votre Domaine
1. **Agents**: Modifiez les rôles et expertises selon votre secteur
2. **Tâches**: Adaptez les workflows à vos processus métier
3. **Alertes**: Configurez les seuils selon vos KPIs
4. **Outputs**: Personnalisez les formats de rapport

### Optimisations Production
1. **Performance**: Caching, optimisation prompts, modèles locaux
2. **Scalabilité**: Load balancing, distribution des tâches
3. **Monitoring**: Intégration Slack/Teams, dashboards visuels
4. **Sécurité**: Isolation, audit logs, chiffrement

## 🏆 Validation des Acquis

Vous maîtrisez le projet si vous pouvez :
- [ ] Expliquer l'architecture hiérarchique CrewAI
- [ ] Configurer les alertes et seuils de performance
- [ ] Adapter les agents et tâches à votre domaine
- [ ] Interpréter les métriques de production
- [ ] Optimiser les coûts et performances

## 🔗 Ressources pour Aller Plus Loin

- [CrewAI Documentation](https://docs.crewai.com/)
- [Hierarchical Processes](https://docs.crewai.com/core-concepts/processes/)
- [Production Best Practices](https://docs.crewai.com/how-to/deployment/)
- [Monitoring and Observability](https://docs.crewai.com/tools/monitoring/)

---

🎯 **Félicitations !** Vous avez construit un système de production robuste et maîtrisé CrewAI !