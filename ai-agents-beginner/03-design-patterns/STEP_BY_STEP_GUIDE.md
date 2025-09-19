# 🎯 Guide Étape par Étape - Patterns Avancés des Agents IA

## 📚 Vue d'Ensemble du Projet

Ce guide vous accompagne dans la maîtrise des **5 patterns avancés** pour créer des systèmes d'agents IA sophistiqués. Vous apprendrez en faisant - chaque étape vous enseigne des concepts complexes tout en construisant un écosystème d'agents collaboratifs.

### 🎯 Objectifs d'Apprentissage
- Maîtriser les patterns avancés de conception d'agents
- Implémenter la collaboration multi-agents
- Créer des systèmes auto-correcteurs
- Intégrer RAG (Retrieval-Augmented Generation)
- Développer la planification automatique avancée
- Construire des architectures distribuées

### 💡 Prérequis
- ✅ Module 1 complété (patterns de base : Single Agent, Tool Use, Human-in-Loop)
- ✅ Connaissance de la boucle agentique
- ✅ Expérience avec LLM + Tools + Memory

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances avancées
pip install openai chromadb sentence-transformers langchain-community faiss-cpu

# 2. Configurer votre environnement
cp .env.example .env
# Ajouter votre OPENAI_API_KEY dans le fichier .env

# 3. Lancer le projet avancé
python my_advanced_agent_system_starter.py
```

## 📋 Progression Étape par Étape

### ✅ TODO 1: Architecture Avancée et Setup (5 min)

**Concepts appris**: Architecture multi-agents et dépendances avancées

```bash
pip install openai chromadb sentence-transformers langchain-community faiss-cpu networkx
```

**Pourquoi ces packages ?**
- `chromadb`: Base de données vectorielle pour RAG
- `sentence-transformers`: Embeddings sémantiques
- `langchain-community`: Outils communautaires LangChain  
- `faiss-cpu`: Recherche vectorielle haute performance
- `networkx`: Gestion de graphes pour multi-agents

Implémentez l'architecture de base:

```python
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Callable, Union
from datetime import datetime
from enum import Enum
import json
import asyncio
import uuid

class AgentRole(Enum):
    """Rôles des agents dans le système"""
    ORCHESTRATOR = "orchestrator"
    SPECIALIST = "specialist"
    VALIDATOR = "validator"
    RESEARCHER = "researcher"
    PLANNER = "planner"
    EXECUTOR = "executor"

class PatternType(Enum):
    """Types de patterns avancés"""
    MULTI_AGENT_COLLAB = "multi_agent_collaboration"
    SELF_CORRECTION = "self_correction"
    RAG_AGENT = "rag_agent"
    PLANNING_AGENT = "planning_agent"
    MULTI_AGENT_SYSTEM = "multi_agent_system"

@dataclass
class AgentMessage:
    """Message standardisé entre agents"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    sender_id: str = ""
    recipient_id: str = ""
    content: str = ""
    message_type: str = "communication"
    priority: int = 1
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class AgentState:
    """État avancé d'un agent"""
    agent_id: str
    role: AgentRole
    capabilities: List[str]
    knowledge_base: Dict[str, Any] = field(default_factory=dict)
    conversation_history: List[Dict] = field(default_factory=list)
    collaboration_history: List[AgentMessage] = field(default_factory=list)
    performance_metrics: Dict[str, float] = field(default_factory=dict)
    current_tasks: List[Dict] = field(default_factory=list)
    learning_insights: List[str] = field(default_factory=list)

class AdvancedAgentBase:
    """Classe de base pour tous les agents avancés"""
    
    def __init__(self, agent_id: str, role: AgentRole, capabilities: List[str]):
        self.state = AgentState(
            agent_id=agent_id,
            role=role,
            capabilities=capabilities
        )
        self.message_queue = asyncio.Queue()
        self.collaboration_network = {}
        self.is_active = True
        
        print(f"🤖 Agent {agent_id} initialisé - Rôle: {role.value}")
        print(f"🎯 Capacités: {', '.join(capabilities)}")
    
    async def send_message(self, recipient_id: str, content: str, message_type: str = "communication") -> bool:
        """Envoyer un message à un autre agent"""
        message = AgentMessage(
            sender_id=self.state.agent_id,
            recipient_id=recipient_id,
            content=content,
            message_type=message_type
        )
        
        self.state.collaboration_history.append(message)
        
        # En production: vraie messagerie inter-agents
        print(f"📤 {self.state.agent_id} → {recipient_id}: {content[:50]}...")
        return True
    
    async def receive_message(self, message: AgentMessage) -> Dict[str, Any]:
        """Recevoir et traiter un message"""
        print(f"📥 {self.state.agent_id} reçoit de {message.sender_id}: {message.content[:50]}...")
        
        await self.message_queue.put(message)
        return await self.process_message(message)
    
    async def process_message(self, message: AgentMessage) -> Dict[str, Any]:
        """Traiter un message reçu - à implémenter par les sous-classes"""
        return {"processed": True, "response": "Message traité"}
    
    def update_performance_metric(self, metric_name: str, value: float):
        """Mettre à jour une métrique de performance"""
        self.state.performance_metrics[metric_name] = value
        
    def add_learning_insight(self, insight: str):
        """Ajouter un insight d'apprentissage"""
        self.state.learning_insights.append({
            "insight": insight,
            "timestamp": datetime.now().isoformat()
        })
```

### ✅ TODO 2: Pattern 1 - Multi-Agent Collaboration (20 min)

**Concepts appris**: Orchestration et spécialisation d'agents

Implémentez le système de collaboration multi-agents:

```python
class OrchestratorAgent(AdvancedAgentBase):
    """Agent orchestrateur pour la collaboration multi-agents"""
    
    def __init__(self):
        super().__init__(
            agent_id="orchestrator_001",
            role=AgentRole.ORCHESTRATOR,
            capabilities=["coordination", "task_distribution", "result_synthesis"]
        )
        self.specialist_agents = {}
        self.current_workflow = None
        
    def register_specialist(self, specialist_agent):
        """Enregistrer un agent spécialiste"""
        self.specialist_agents[specialist_agent.state.agent_id] = specialist_agent
        print(f"✅ Spécialiste enregistré: {specialist_agent.state.agent_id} ({specialist_agent.state.role.value})")
    
    async def coordinate_task(self, task: str) -> Dict[str, Any]:
        """Coordonner une tâche complexe entre spécialistes"""
        print(f"\n🎯 COORDINATION MULTI-AGENTS: {task}")
        print("=" * 60)
        
        # Analyser la tâche et identifier les spécialistes nécessaires
        required_specialists = self._identify_required_specialists(task)
        
        # Créer un workflow de collaboration
        workflow = await self._create_collaboration_workflow(task, required_specialists)
        self.current_workflow = workflow
        
        # Exécuter le workflow
        results = await self._execute_workflow(workflow)
        
        # Synthétiser les résultats
        final_result = await self._synthesize_results(task, results)
        
        return {
            "task": task,
            "specialists_involved": list(required_specialists.keys()),
            "workflow_steps": len(workflow["steps"]),
            "individual_results": results,
            "synthesized_result": final_result,
            "success": final_result.get("success", False),
            "collaboration_quality": self._assess_collaboration_quality(results)
        }
    
    def _identify_required_specialists(self, task: str) -> Dict[str, Any]:
        """Identifier les spécialistes nécessaires pour une tâche"""
        task_lower = task.lower()
        required = {}
        
        # Logique de sélection basée sur les capacités
        for agent_id, agent in self.specialist_agents.items():
            relevance_score = 0
            
            # Calculer la pertinence selon les capacités
            for capability in agent.state.capabilities:
                if any(keyword in task_lower for keyword in self._get_capability_keywords(capability)):
                    relevance_score += 1
            
            if relevance_score > 0:
                required[agent_id] = {
                    "agent": agent,
                    "relevance": relevance_score,
                    "role": agent.state.role,
                    "capabilities": agent.state.capabilities
                }
        
        # Trier par pertinence
        required = dict(sorted(required.items(), key=lambda x: x[1]["relevance"], reverse=True))
        
        print(f"🔍 Spécialistes identifiés: {len(required)}")
        for agent_id, info in required.items():
            print(f"   • {agent_id}: {info['role'].value} (pertinence: {info['relevance']})")
        
        return required
    
    def _get_capability_keywords(self, capability: str) -> List[str]:
        """Obtenir les mots-clés associés à une capacité"""
        keyword_map = {
            "research": ["recherche", "information", "étude", "analyse", "investigation"],
            "analysis": ["analyse", "évaluation", "examen", "diagnostic", "assessment"],
            "writing": ["écriture", "rédaction", "texte", "contenu", "rapport"],
            "calculation": ["calcul", "mathématique", "nombre", "statistique", "computation"],
            "validation": ["validation", "vérification", "contrôle", "test", "quality"],
            "synthesis": ["synthèse", "résumé", "compilation", "agrégation", "fusion"]
        }
        return keyword_map.get(capability, [capability])
    
    async def _create_collaboration_workflow(self, task: str, specialists: Dict) -> Dict[str, Any]:
        """Créer un workflow de collaboration"""
        workflow = {
            "id": f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "task": task,
            "participants": list(specialists.keys()),
            "steps": [],
            "dependencies": {},
            "estimated_duration": 0
        }
        
        # Créer les étapes selon les spécialistes disponibles
        step_id = 1
        
        # Étape 1: Recherche (si disponible)
        research_agents = [aid for aid, info in specialists.items() 
                          if info["role"] == AgentRole.RESEARCHER]
        if research_agents:
            workflow["steps"].append({
                "id": step_id,
                "type": "research",
                "assigned_to": research_agents[0],
                "description": f"Rechercher des informations sur: {task}",
                "priority": 1
            })
            step_id += 1
        
        # Étape 2: Analyse (si disponible)
        analysis_agents = [aid for aid, info in specialists.items() 
                          if "analysis" in info["capabilities"]]
        if analysis_agents:
            workflow["steps"].append({
                "id": step_id,
                "type": "analysis",
                "assigned_to": analysis_agents[0],
                "description": f"Analyser les données pour: {task}",
                "priority": 2,
                "depends_on": [1] if research_agents else []
            })
            step_id += 1
        
        # Étape 3: Synthèse finale
        workflow["steps"].append({
            "id": step_id,
            "type": "synthesis",
            "assigned_to": self.state.agent_id,
            "description": "Synthétiser tous les résultats",
            "priority": 3,
            "depends_on": list(range(1, step_id))
        })
        
        print(f"📋 Workflow créé: {len(workflow['steps'])} étapes")
        return workflow
    
    async def _execute_workflow(self, workflow: Dict) -> Dict[str, Any]:
        """Exécuter le workflow de collaboration"""
        results = {}
        
        for step in workflow["steps"]:
            print(f"\n⚡ Exécution étape {step['id']}: {step['description']}")
            
            # Vérifier les dépendances
            dependencies_met = all(
                dep_id in results for dep_id in step.get("depends_on", [])
            )
            
            if not dependencies_met:
                print(f"⏳ En attente des dépendances pour l'étape {step['id']}")
                continue
            
            # Exécuter l'étape
            if step["assigned_to"] == self.state.agent_id:
                # L'orchestrateur fait la synthèse
                result = await self._orchestrator_synthesis(workflow, results)
            else:
                # Déléguer à un spécialiste
                specialist = self.specialist_agents[step["assigned_to"]]
                
                # Préparer le contexte
                context = {
                    "task": workflow["task"],
                    "step_description": step["description"],
                    "previous_results": {k: v for k, v in results.items() if k in step.get("depends_on", [])}
                }
                
                result = await specialist.execute_specialized_task(context)
            
            results[step["id"]] = {
                "step": step,
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "success": result.get("success", True)
            }
            
            print(f"✅ Étape {step['id']} terminée: {result.get('success', True)}")
        
        return results
    
    async def _orchestrator_synthesis(self, workflow: Dict, step_results: Dict) -> Dict[str, Any]:
        """Synthèse par l'orchestrateur"""
        synthesis_content = f"Synthèse de la tâche: {workflow['task']}\n\n"
        
        for step_id, step_data in step_results.items():
            step_info = step_data["step"]
            result = step_data["result"]
            
            synthesis_content += f"Étape {step_id} ({step_info['type']}):\n"
            synthesis_content += f"- Description: {step_info['description']}\n"
            synthesis_content += f"- Résultat: {result.get('content', 'Pas de contenu')}\n"
            synthesis_content += f"- Succès: {result.get('success', 'Unknown')}\n\n"
        
        return {
            "content": synthesis_content,
            "synthesis_quality": len(step_results) / len(workflow["steps"]),
            "success": all(r["success"] for r in step_results.values()),
            "type": "orchestrator_synthesis"
        }
    
    async def _synthesize_results(self, task: str, results: Dict) -> Dict[str, Any]:
        """Synthétiser les résultats finaux"""
        successful_steps = sum(1 for r in results.values() if r["success"])
        total_steps = len(results)
        
        # Compiler les contenus
        all_content = []
        for step_id, step_data in results.items():
            content = step_data["result"].get("content", "")
            if content:
                all_content.append(f"Étape {step_id}: {content}")
        
        synthesis = {
            "task_completed": task,
            "total_steps": total_steps,
            "successful_steps": successful_steps,
            "success_rate": successful_steps / total_steps if total_steps > 0 else 0,
            "final_synthesis": "\n".join(all_content),
            "success": successful_steps == total_steps,
            "quality_score": successful_steps / total_steps if total_steps > 0 else 0
        }
        
        return synthesis
    
    def _assess_collaboration_quality(self, results: Dict) -> float:
        """Évaluer la qualité de la collaboration"""
        if not results:
            return 0.0
        
        # Facteurs de qualité
        completion_rate = sum(1 for r in results.values() if r["success"]) / len(results)
        
        # Communication quality (basé sur les messages échangés)
        communication_quality = min(1.0, len(self.state.collaboration_history) / len(results))
        
        # Temps de traitement (simulation)
        timing_quality = 0.8  # Simulé
        
        overall_quality = (completion_rate * 0.5 + communication_quality * 0.3 + timing_quality * 0.2)
        
        return overall_quality

class ResearchSpecialist(AdvancedAgentBase):
    """Agent spécialisé en recherche d'informations"""
    
    def __init__(self):
        super().__init__(
            agent_id="researcher_001",
            role=AgentRole.RESEARCHER,
            capabilities=["research", "information_gathering", "fact_checking"]
        )
    
    async def execute_specialized_task(self, context: Dict) -> Dict[str, Any]:
        """Exécuter une tâche de recherche spécialisée"""
        task = context.get("step_description", "")
        main_task = context.get("task", "")
        
        print(f"🔍 RECHERCHE SPÉCIALISÉE: {task}")
        
        # Simuler une recherche approfondie
        research_results = {
            "search_queries": self._generate_search_queries(main_task),
            "information_found": self._simulate_research(main_task),
            "sources": self._generate_sources(main_task),
            "confidence_level": 0.85
        }
        
        # Compiler le rapport de recherche
        content = self._compile_research_report(research_results)
        
        return {
            "content": content,
            "research_data": research_results,
            "success": True,
            "confidence": research_results["confidence_level"],
            "specialist": "researcher"
        }
    
    def _generate_search_queries(self, task: str) -> List[str]:
        """Générer des requêtes de recherche"""
        base_terms = task.split()
        queries = [
            f"what is {task}",
            f"{task} definition explanation",
            f"{task} examples applications",
            f"latest research {task}",
            f"best practices {task}"
        ]
        return queries[:3]  # Limiter pour la démo
    
    def _simulate_research(self, task: str) -> Dict[str, Any]:
        """Simuler des résultats de recherche"""
        return {
            "key_concepts": [f"Concept A de {task}", f"Concept B de {task}", f"Concept C de {task}"],
            "main_benefits": [f"Bénéfice 1", f"Bénéfice 2", f"Bénéfice 3"],
            "challenges": [f"Défi 1", f"Défi 2"],
            "current_trends": [f"Tendance 1 en {task}", f"Tendance 2 en {task}"]
        }
    
    def _generate_sources(self, task: str) -> List[Dict]:
        """Générer des sources simulées"""
        return [
            {"title": f"Guide complet sur {task}", "url": f"https://expert-guide.com/{task.replace(' ', '-')}", "reliability": 0.9},
            {"title": f"Recherche récente: {task}", "url": f"https://research.org/papers/{task.replace(' ', '_')}", "reliability": 0.95},
            {"title": f"Best practices pour {task}", "url": f"https://bestpractices.com/{task.replace(' ', '-')}", "reliability": 0.8}
        ]
    
    def _compile_research_report(self, research_data: Dict) -> str:
        """Compiler un rapport de recherche"""
        report = f"""RAPPORT DE RECHERCHE

Concepts clés identifiés:
"""
        for concept in research_data["information_found"]["key_concepts"]:
            report += f"• {concept}\n"
        
        report += f"\nBénéfices principaux:\n"
        for benefit in research_data["information_found"]["main_benefits"]:
            report += f"• {benefit}\n"
        
        report += f"\nDéfis identifiés:\n"
        for challenge in research_data["information_found"]["challenges"]:
            report += f"• {challenge}\n"
        
        report += f"\nTendances actuelles:\n"
        for trend in research_data["information_found"]["current_trends"]:
            report += f"• {trend}\n"
        
        report += f"\nSources consultées: {len(research_data['sources'])} sources fiables"
        report += f"\nNiveau de confiance: {research_data['confidence_level']:.1%}"
        
        return report

class AnalysisSpecialist(AdvancedAgentBase):
    """Agent spécialisé en analyse de données"""
    
    def __init__(self):
        super().__init__(
            agent_id="analyst_001",
            role=AgentRole.SPECIALIST,
            capabilities=["analysis", "data_processing", "insights_generation"]
        )
    
    async def execute_specialized_task(self, context: Dict) -> Dict[str, Any]:
        """Exécuter une tâche d'analyse spécialisée"""
        task = context.get("step_description", "")
        previous_results = context.get("previous_results", {})
        
        print(f"📊 ANALYSE SPÉCIALISÉE: {task}")
        
        # Analyser les données des étapes précédentes
        analysis_results = self._perform_analysis(previous_results, task)
        
        # Générer des insights
        insights = self._generate_insights(analysis_results)
        
        # Compiler le rapport d'analyse
        content = self._compile_analysis_report(analysis_results, insights)
        
        return {
            "content": content,
            "analysis_data": analysis_results,
            "insights": insights,
            "success": True,
            "confidence": 0.88,
            "specialist": "analyst"
        }
    
    def _perform_analysis(self, previous_results: Dict, task: str) -> Dict[str, Any]:
        """Effectuer l'analyse des données précédentes"""
        analysis = {
            "data_quality": self._assess_data_quality(previous_results),
            "key_patterns": self._identify_patterns(previous_results),
            "statistical_summary": self._generate_statistics(previous_results),
            "correlations": self._find_correlations(previous_results)
        }
        
        return analysis
    
    def _assess_data_quality(self, data: Dict) -> Dict[str, Any]:
        """Évaluer la qualité des données"""
        if not data:
            return {"score": 0.0, "issues": ["Aucune donnée disponible"]}
        
        completeness = len([r for r in data.values() if r.get("success", False)]) / len(data)
        
        return {
            "score": completeness,
            "completeness": completeness,
            "issues": [] if completeness > 0.8 else ["Données incomplètes"],
            "recommendations": ["Données de qualité acceptable"] if completeness > 0.8 else ["Améliorer la collecte de données"]
        }
    
    def _identify_patterns(self, data: Dict) -> List[str]:
        """Identifier des patterns dans les données"""
        patterns = []
        
        if data:
            successful_steps = sum(1 for r in data.values() if r.get("success", False))
            total_steps = len(data)
            
            if successful_steps == total_steps:
                patterns.append("Workflow exécuté avec succès complet")
            elif successful_steps > total_steps * 0.5:
                patterns.append("Majorité des étapes réussies")
            else:
                patterns.append("Performance workflow à améliorer")
        
        return patterns
    
    def _generate_statistics(self, data: Dict) -> Dict[str, Any]:
        """Générer des statistiques"""
        if not data:
            return {"total_steps": 0, "success_rate": 0.0}
        
        total_steps = len(data)
        successful_steps = sum(1 for r in data.values() if r.get("success", False))
        
        return {
            "total_steps": total_steps,
            "successful_steps": successful_steps,
            "success_rate": successful_steps / total_steps if total_steps > 0 else 0,
            "failure_rate": 1 - (successful_steps / total_steps) if total_steps > 0 else 0
        }
    
    def _find_correlations(self, data: Dict) -> List[str]:
        """Trouver des corrélations"""
        correlations = []
        
        if len(data) >= 2:
            correlations.append("Corrélation positive entre qualité des données et succès")
            correlations.append("Les étapes séquentielles montrent une dépendance logique")
        
        return correlations
    
    def _generate_insights(self, analysis: Dict) -> List[str]:
        """Générer des insights basés sur l'analyse"""
        insights = []
        
        quality_score = analysis["data_quality"]["score"]
        if quality_score > 0.8:
            insights.append("Excellent niveau de qualité des données collectées")
        elif quality_score > 0.6:
            insights.append("Qualité des données acceptable avec marge d'amélioration")
        else:
            insights.append("Qualité des données insuffisante, révision nécessaire")
        
        success_rate = analysis["statistical_summary"]["success_rate"]
        if success_rate > 0.9:
            insights.append("Performance exceptionnelle du workflow")
        elif success_rate > 0.7:
            insights.append("Bonne performance globale")
        else:
            insights.append("Performance à optimiser")
        
        return insights
    
    def _compile_analysis_report(self, analysis: Dict, insights: List[str]) -> str:
        """Compiler le rapport d'analyse"""
        report = f"""RAPPORT D'ANALYSE

Qualité des données:
• Score global: {analysis['data_quality']['score']:.1%}
• Complétude: {analysis['data_quality']['completeness']:.1%}

Statistiques clés:
• Total d'étapes: {analysis['statistical_summary']['total_steps']}
• Taux de succès: {analysis['statistical_summary']['success_rate']:.1%}

Patterns identifiés:
"""
        for pattern in analysis["key_patterns"]:
            report += f"• {pattern}\n"
        
        report += f"\nInsights principaux:\n"
        for insight in insights:
            report += f"• {insight}\n"
        
        report += f"\nCorrélations détectées:\n"
        for correlation in analysis["correlations"]:
            report += f"• {correlation}\n"
        
        return report

# Fonction de démonstration
async def demo_multi_agent_collaboration():
    """Démonstration du pattern Multi-Agent Collaboration"""
    print(f"\n🎬 DÉMONSTRATION: Pattern Multi-Agent Collaboration")
    print("=" * 80)
    
    # Créer l'orchestrateur
    orchestrator = OrchestratorAgent()
    
    # Créer les spécialistes
    researcher = ResearchSpecialist()
    analyst = AnalysisSpecialist()
    
    # Enregistrer les spécialistes
    orchestrator.register_specialist(researcher)
    orchestrator.register_specialist(analyst)
    
    # Tâches de test pour collaboration
    test_tasks = [
        "Recherche et analyse des tendances en intelligence artificielle",
        "Étude de marché pour les agents conversationnels",
        "Analyse comparative des frameworks d'IA"
    ]
    
    results = []
    
    for i, task in enumerate(test_tasks, 1):
        print(f"\n--- Tâche collaborative {i}/{len(test_tasks)} ---")
        
        result = await orchestrator.coordinate_task(task)
        results.append(result)
        
        print(f"\n📊 Résultats tâche {i}:")
        print(f"   • Spécialistes impliqués: {len(result['specialists_involved'])}")
        print(f"   • Étapes du workflow: {result['workflow_steps']}")
        print(f"   • Succès global: {'Oui' if result['success'] else 'Non'}")
        print(f"   • Qualité collaboration: {result['collaboration_quality']:.2f}")
        print(f"   • Synthèse: {result['synthesized_result']['final_synthesis'][:100]}...")
    
    # Statistiques finales
    print(f"\n📈 STATISTIQUES COLLABORATION")
    print("=" * 60)
    total_tasks = len(results)
    successful_tasks = sum(1 for r in results if r["success"])
    avg_quality = sum(r["collaboration_quality"] for r in results) / total_tasks
    
    print(f"📊 Total tâches: {total_tasks}")
    print(f"✅ Tâches réussies: {successful_tasks} ({successful_tasks/total_tasks:.1%})")
    print(f"🏆 Qualité moyenne: {avg_quality:.2f}")
    
    return results
```

### ✅ TODO 3: Pattern 2 - Self-Correction (15 min)

**Concepts appris**: Auto-amélioration et boucles de feedback

Implémentez le système d'auto-correction:

```python
class SelfCorrectionAgent(AdvancedAgentBase):
    """Agent avec capacités d'auto-correction et d'amélioration continue"""
    
    def __init__(self):
        super().__init__(
            agent_id="self_corrector_001",
            role=AgentRole.VALIDATOR,
            capabilities=["self_assessment", "error_detection", "improvement", "learning"]
        )
        
        self.correction_history = []
        self.quality_thresholds = {
            "accuracy": 0.8,
            "completeness": 0.7,
            "relevance": 0.75,
            "coherence": 0.8
        }
        self.max_correction_iterations = 3
        
    async def process_with_self_correction(self, task: str, initial_response: str = None) -> Dict[str, Any]:
        """Traiter une tâche avec auto-correction"""
        print(f"\n🔄 SELF-CORRECTION: {task}")
        print("=" * 60)
        
        # Générer une réponse initiale si non fournie
        if initial_response is None:
            initial_response = await self._generate_initial_response(task)
        
        current_response = initial_response
        iteration = 0
        correction_log = []
        
        while iteration < self.max_correction_iterations:
            iteration += 1
            print(f"\n🔍 Itération {iteration}: Évaluation et correction")
            
            # Évaluer la qualité de la réponse actuelle
            quality_assessment = await self._assess_quality(task, current_response)
            
            print(f"📊 Scores de qualité:")
            for metric, score in quality_assessment["scores"].items():
                status = "✅" if score >= self.quality_thresholds[metric] else "❌"
                print(f"   • {metric}: {score:.2f} {status}")
            
            # Vérifier si des corrections sont nécessaires
            needs_correction = quality_assessment["needs_correction"]
            
            if not needs_correction:
                print(f"✅ Qualité satisfaisante atteinte à l'itération {iteration}")
                break
            
            # Identifier les problèmes spécifiques
            issues = quality_assessment["identified_issues"]
            print(f"🚨 Problèmes identifiés: {len(issues)}")
            for issue in issues:
                print(f"   • {issue}")
            
            # Générer une version corrigée
            correction_strategy = self._develop_correction_strategy(quality_assessment)
            corrected_response = await self._apply_corrections(
                current_response, 
                correction_strategy, 
                task
            )
            
            # Enregistrer le cycle de correction
            correction_cycle = {
                "iteration": iteration,
                "original_response": current_response,
                "quality_scores": quality_assessment["scores"],
                "issues_found": issues,
                "correction_strategy": correction_strategy,
                "corrected_response": corrected_response,
                "timestamp": datetime.now().isoformat()
            }
            
            correction_log.append(correction_cycle)
            current_response = corrected_response
            
            print(f"🔧 Correction appliquée pour l'itération {iteration}")
        
        # Évaluation finale
        final_assessment = await self._assess_quality(task, current_response)
        
        # Apprendre de cette expérience
        learning_insights = self._extract_learning_insights(correction_log, final_assessment)
        for insight in learning_insights:
            self.add_learning_insight(insight)
        
        result = {
            "task": task,
            "initial_response": initial_response,
            "final_response": current_response,
            "correction_iterations": iteration,
            "correction_log": correction_log,
            "final_quality_scores": final_assessment["scores"],
            "improvement_achieved": self._calculate_improvement(correction_log, final_assessment),
            "learning_insights": learning_insights,
            "success": not final_assessment["needs_correction"],
            "quality_threshold_met": all(
                score >= threshold 
                for metric, (score, threshold) in zip(
                    final_assessment["scores"].keys(),
                    zip(final_assessment["scores"].values(), self.quality_thresholds.values())
                )
            )
        }
        
        self.correction_history.append(result)
        
        print(f"\n🏆 RÉSULTAT FINAL:")
        print(f"   • Itérations: {iteration}")
        print(f"   • Qualité finale: {sum(final_assessment['scores'].values())/len(final_assessment['scores']):.2f}")
        print(f"   • Seuils atteints: {'Oui' if result['quality_threshold_met'] else 'Non'}")
        
        return result
    
    async def _generate_initial_response(self, task: str) -> str:
        """Générer une réponse initiale"""
        # Simulation d'une réponse LLM initiale
        initial_response = f"""Réponse initiale pour: {task}

Voici une première approche de réponse qui pourrait contenir des imprécisions ou être incomplète. Cette réponse sera ensuite évaluée et améliorée par le système d'auto-correction.

Contenu principal: {task} est un sujet important qui nécessite une analyse approfondie. Les aspects clés incluent plusieurs éléments qu'il faut considérer attentivement.

Points à développer:
- Aspect technique
- Considérations pratiques  
- Implications futures

Cette réponse initiale sera affinée lors des itérations suivantes."""
        
        return initial_response
    
    async def _assess_quality(self, task: str, response: str) -> Dict[str, Any]:
        """Évaluer la qualité d'une réponse"""
        
        # Évaluation de l'exactitude
        accuracy_score = self._assess_accuracy(task, response)
        
        # Évaluation de la complétude
        completeness_score = self._assess_completeness(task, response)
        
        # Évaluation de la pertinence
        relevance_score = self._assess_relevance(task, response)
        
        # Évaluation de la cohérence
        coherence_score = self._assess_coherence(response)
        
        scores = {
            "accuracy": accuracy_score,
            "completeness": completeness_score,
            "relevance": relevance_score,
            "coherence": coherence_score
        }
        
        # Identifier les problèmes
        issues = []
        for metric, score in scores.items():
            if score < self.quality_thresholds[metric]:
                issues.append(f"{metric} insuffisant ({score:.2f} < {self.quality_thresholds[metric]})")
        
        # Déterminer si une correction est nécessaire
        needs_correction = len(issues) > 0
        
        assessment = {
            "scores": scores,
            "average_score": sum(scores.values()) / len(scores),
            "identified_issues": issues,
            "needs_correction": needs_correction,
            "quality_level": self._determine_quality_level(scores)
        }
        
        return assessment
    
    def _assess_accuracy(self, task: str, response: str) -> float:
        """Évaluer l'exactitude de la réponse"""
        # Simulation d'évaluation d'exactitude
        response_lower = response.lower()
        task_lower = task.lower()
        
        # Vérifier la correspondance avec la tâche
        task_relevance = 0.7  # Score de base
        
        # Bonus pour des termes techniques appropriés
        if "analyse" in response_lower and "analyse" in task_lower:
            task_relevance += 0.1
        if "important" in response_lower:
            task_relevance += 0.05
        
        # Pénalité pour des réponses trop vagues
        if len(response.split()) < 50:
            task_relevance -= 0.2
        
        return max(0.0, min(1.0, task_relevance))
    
    def _assess_completeness(self, task: str, response: str) -> float:
        """Évaluer la complétude de la réponse"""
        expected_elements = [
            "introduction", "développement", "conclusion",
            "exemples", "aspects", "points"
        ]
        
        response_lower = response.lower()
        elements_present = sum(1 for element in expected_elements if element in response_lower)
        
        # Score basé sur la présence d'éléments attendus
        completeness = elements_present / len(expected_elements)
        
        # Bonus pour la longueur appropriée
        word_count = len(response.split())
        if word_count >= 100:
            completeness += 0.1
        elif word_count < 30:
            completeness -= 0.2
        
        return max(0.0, min(1.0, completeness))
    
    def _assess_relevance(self, task: str, response: str) -> float:
        """Évaluer la pertinence de la réponse"""
        task_words = set(task.lower().split())
        response_words = set(response.lower().split())
        
        # Intersection des mots-clés
        common_words = task_words.intersection(response_words)
        
        if len(task_words) == 0:
            return 0.5  # Score neutre si pas de mots dans la tâche
        
        keyword_overlap = len(common_words) / len(task_words)
        
        # Bonus pour la mention explicite de la tâche
        if task.lower() in response.lower():
            keyword_overlap += 0.2
        
        return max(0.0, min(1.0, keyword_overlap))
    
    def _assess_coherence(self, response: str) -> float:
        """Évaluer la cohérence de la réponse"""
        sentences = response.split('.')
        
        # Score de base pour les réponses structurées
        coherence = 0.6
        
        # Bonus pour la structure
        if len(sentences) >= 3:
            coherence += 0.1
        
        # Bonus pour la présence de connecteurs logiques
        connectors = ["donc", "ainsi", "par conséquent", "cependant", "en effet", "de plus"]
        connector_count = sum(1 for conn in connectors if conn in response.lower())
        coherence += min(0.3, connector_count * 0.1)
        
        # Pénalité pour répétitions excessives
        words = response.lower().split()
        unique_words = set(words)
        if len(words) > 0:
            repetition_ratio = len(unique_words) / len(words)
            if repetition_ratio < 0.5:
                coherence -= 0.2
        
        return max(0.0, min(1.0, coherence))
    
    def _determine_quality_level(self, scores: Dict[str, float]) -> str:
        """Déterminer le niveau de qualité global"""
        avg_score = sum(scores.values()) / len(scores)
        
        if avg_score >= 0.9:
            return "Excellent"
        elif avg_score >= 0.8:
            return "Très bon"
        elif avg_score >= 0.7:
            return "Bon"
        elif avg_score >= 0.6:
            return "Acceptable"
        else:
            return "Insuffisant"
    
    def _develop_correction_strategy(self, quality_assessment: Dict) -> Dict[str, Any]:
        """Développer une stratégie de correction"""
        scores = quality_assessment["scores"]
        issues = quality_assessment["identified_issues"]
        
        strategy = {
            "corrections_needed": [],
            "priority_order": [],
            "specific_actions": []
        }
        
        # Identifier les corrections par priorité
        for metric, score in scores.items():
            if score < self.quality_thresholds[metric]:
                deficit = self.quality_thresholds[metric] - score
                strategy["corrections_needed"].append({
                    "metric": metric,
                    "current_score": score,
                    "target_score": self.quality_thresholds[metric],
                    "deficit": deficit,
                    "priority": deficit  # Plus le déficit est grand, plus la priorité est haute
                })
        
        # Trier par priorité
        strategy["corrections_needed"].sort(key=lambda x: x["deficit"], reverse=True)
        strategy["priority_order"] = [c["metric"] for c in strategy["corrections_needed"]]
        
        # Actions spécifiques selon le type de problème
        for correction in strategy["corrections_needed"]:
            metric = correction["metric"]
            
            if metric == "accuracy":
                strategy["specific_actions"].append("Vérifier et corriger les faits inexacts")
                strategy["specific_actions"].append("Ajouter des détails précis")
                
            elif metric == "completeness":
                strategy["specific_actions"].append("Développer les sections manquantes")
                strategy["specific_actions"].append("Ajouter des exemples concrets")
                
            elif metric == "relevance":
                strategy["specific_actions"].append("Recentrer sur le sujet principal")
                strategy["specific_actions"].append("Supprimer les éléments hors-sujet")
                
            elif metric == "coherence":
                strategy["specific_actions"].append("Améliorer les transitions entre idées")
                strategy["specific_actions"].append("Restructurer le contenu logiquement")
        
        return strategy
    
    async def _apply_corrections(self, original_response: str, strategy: Dict, task: str) -> str:
        """Appliquer les corrections selon la stratégie"""
        corrected_response = original_response
        
        # Appliquer les corrections selon la priorité
        for action in strategy["specific_actions"]:
            if "Vérifier et corriger les faits" in action:
                corrected_response = self._improve_accuracy(corrected_response, task)
            elif "Développer les sections" in action:
                corrected_response = self._improve_completeness(corrected_response, task)
            elif "Recentrer sur le sujet" in action:
                corrected_response = self._improve_relevance(corrected_response, task)
            elif "Améliorer les transitions" in action:
                corrected_response = self._improve_coherence(corrected_response)
        
        return corrected_response
    
    def _improve_accuracy(self, response: str, task: str) -> str:
        """Améliorer l'exactitude de la réponse"""
        # Ajout de précisions et corrections factuelles
        improved = response + f"\n\n[Correction d'exactitude] Précisions importantes concernant {task}:\n"
        improved += "- Informations vérifiées et validées\n"
        improved += "- Sources fiables consultées\n"
        improved += "- Données mises à jour selon les dernières recherches\n"
        
        return improved
    
    def _improve_completeness(self, response: str, task: str) -> str:
        """Améliorer la complétude de la réponse"""
        # Ajout de sections manquantes
        improved = response + f"\n\n[Amélioration complétude] Développements supplémentaires:\n"
        improved += f"• Contexte détaillé: {task} s'inscrit dans un cadre plus large qu'il convient d'analyser.\n"
        improved += "• Exemples pratiques: Plusieurs cas d'usage illustrent concrètement les concepts.\n"
        improved += "• Implications futures: Les tendances émergentes suggèrent des évolutions importantes.\n"
        improved += "• Considérations techniques: Les aspects méthodologiques méritent une attention particulière.\n"
        
        return improved
    
    def _improve_relevance(self, response: str, task: str) -> str:
        """Améliorer la pertinence de la réponse"""
        # Recentrage sur le sujet principal
        improved = f"[Recentrage sur {task}]\n\n" + response
        improved += f"\n\n[Synthèse pertinence] En résumé, concernant spécifiquement {task}:\n"
        improved += "- Les éléments clés ont été identifiés et analysés\n"
        improved += "- La réponse se concentre sur les aspects les plus pertinents\n"
        improved += "- Les informations périphériques ont été écartées pour plus de clarté\n"
        
        return improved
    
    def _improve_coherence(self, response: str) -> str:
        """Améliorer la cohérence de la réponse"""
        # Amélioration de la structure et des transitions
        sections = response.split('\n\n')
        
        improved_sections = []
        for i, section in enumerate(sections):
            if i > 0:
                # Ajouter des connecteurs logiques
                connectors = ["Par ailleurs,", "En outre,", "De plus,", "Cependant,", "Ainsi,"]
                if not any(conn.lower() in section.lower() for conn in connectors):
                    connector = connectors[i % len(connectors)]
                    section = f"{connector} {section}"
            
            improved_sections.append(section)
        
        improved = '\n\n'.join(improved_sections)
        improved += "\n\n[Amélioration cohérence] La structure logique a été renforcée avec des transitions appropriées entre les différentes sections."
        
        return improved
    
    def _calculate_improvement(self, correction_log: List[Dict], final_assessment: Dict) -> Dict[str, Any]:
        """Calculer l'amélioration réalisée"""
        if not correction_log:
            return {"improvement": 0, "details": "Aucune correction effectuée"}
        
        initial_scores = correction_log[0]["quality_scores"]
        final_scores = final_assessment["scores"]
        
        improvements = {}
        total_improvement = 0
        
        for metric in initial_scores.keys():
            initial = initial_scores[metric]
            final = final_scores[metric]
            improvement = final - initial
            improvements[metric] = {
                "initial": initial,
                "final": final,
                "improvement": improvement,
                "improvement_percentage": (improvement / initial * 100) if initial > 0 else 0
            }
            total_improvement += improvement
        
        return {
            "total_improvement": total_improvement,
            "average_improvement": total_improvement / len(initial_scores),
            "by_metric": improvements,
            "significant_improvement": total_improvement > 0.2,
            "best_improved_metric": max(improvements.keys(), key=lambda x: improvements[x]["improvement"])
        }
    
    def _extract_learning_insights(self, correction_log: List[Dict], final_assessment: Dict) -> List[str]:
        """Extraire des insights d'apprentissage"""
        insights = []
        
        if correction_log:
            iterations_needed = len(correction_log)
            
            if iterations_needed == 1:
                insights.append("Corrections mineures nécessaires - bon niveau initial")
            elif iterations_needed == 2:
                insights.append("Corrections modérées - processus d'amélioration efficace")
            else:
                insights.append("Corrections importantes nécessaires - révision du processus initial recommandée")
            
            # Analyser les patterns de correction
            common_issues = []
            for log_entry in correction_log:
                for issue in log_entry["issues_found"]:
                    if "accuracy" in issue:
                        common_issues.append("accuracy")
                    elif "completeness" in issue:
                        common_issues.append("completeness")
                    elif "relevance" in issue:
                        common_issues.append("relevance")
                    elif "coherence" in issue:
                        common_issues.append("coherence")
            
            from collections import Counter
            issue_counts = Counter(common_issues)
            
            if issue_counts:
                most_common_issue = issue_counts.most_common(1)[0][0]
                insights.append(f"Problème récurrent identifié: {most_common_issue}")
        
        # Analyser la qualité finale
        final_avg_score = sum(final_assessment["scores"].values()) / len(final_assessment["scores"])
        if final_avg_score >= 0.9:
            insights.append("Excellente qualité finale atteinte")
        elif final_avg_score >= 0.8:
            insights.append("Bonne qualité finale avec marge d'amélioration")
        else:
            insights.append("Qualité finale insuffisante - révision du processus nécessaire")
        
        return insights
    
    async def demonstrate_self_correction(self):
        """Démonstration des capacités d'auto-correction"""
        print(f"\n🎬 DÉMONSTRATION: Pattern Self-Correction")
        print("=" * 80)
        
        demo_tasks = [
            "Expliquer les principes de l'intelligence artificielle",
            "Analyser les avantages et inconvénients du télétravail",
            "Présenter les enjeux de la cybersécurité moderne"
        ]
        
        results = []
        
        for i, task in enumerate(demo_tasks, 1):
            print(f"\n--- Tâche d'auto-correction {i}/{len(demo_tasks)} ---")
            print(f"📝 Tâche: {task}")
            
            result = await self.process_with_self_correction(task)
            results.append(result)
            
            print(f"\n📊 Résultats pour la tâche {i}:")
            print(f"   • Itérations de correction: {result['correction_iterations']}")
            print(f"   • Seuils de qualité atteints: {'Oui' if result['quality_threshold_met'] else 'Non'}")
            print(f"   • Amélioration totale: {result['improvement_achieved']['total_improvement']:.2f}")
            print(f"   • Métrique la plus améliorée: {result['improvement_achieved'].get('best_improved_metric', 'N/A')}")
            print(f"   • Insights d'apprentissage: {len(result['learning_insights'])}")
        
        # Statistiques globales
        print(f"\n📈 STATISTIQUES SELF-CORRECTION")
        print("=" * 60)
        
        total_tasks = len(results)
        successful_corrections = sum(1 for r in results if r["quality_threshold_met"])
        avg_iterations = sum(r["correction_iterations"] for r in results) / total_tasks
        total_insights = sum(len(r["learning_insights"]) for r in results)
        
        print(f"📊 Total tâches: {total_tasks}")
        print(f"✅ Corrections réussies: {successful_corrections} ({successful_corrections/total_tasks:.1%})")
        print(f"🔄 Itérations moyennes: {avg_iterations:.1f}")
        print(f"🧠 Insights d'apprentissage: {total_insights}")
        print(f"📚 Historique total: {len(self.correction_history)} expériences")
        
        return results
```

### ✅ TODO 4: Pattern 3 - RAG Agent (20 min)

**Concepts appris**: Retrieval-Augmented Generation et base de connaissances

Implémentez le système RAG avancé:

```python
import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict, Any, Optional

class AdvancedRAGAgent(AdvancedAgentBase):
    """Agent RAG avancé avec base de connaissances vectorielle"""
    
    def __init__(self):
        super().__init__(
            agent_id="rag_agent_001",
            role=AgentRole.RESEARCHER,
            capabilities=["knowledge_retrieval", "semantic_search", "context_generation", "fact_verification"]
        )
        
        # Configuration RAG
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chroma_client = chromadb.Client()
        self.knowledge_collections = {}
        self.retrieval_config = {
            "top_k": 5,
            "similarity_threshold": 0.6,
            "max_context_length": 2000,
            "rerank_results": True
        }
        
        # Initialiser les collections de connaissances
        self._initialize_knowledge_base()
        
    def _initialize_knowledge_base(self):
        """Initialiser la base de connaissances vectorielle"""
        print("🧠 Initialisation de la base de connaissances RAG...")
        
        # Créer les collections thématiques
        collection_configs = {
            "ai_knowledge": {
                "description": "Connaissances sur l'intelligence artificielle",
                "metadata": {"domain": "ai", "language": "fr"}
            },
            "technical_docs": {
                "description": "Documentation technique et programmation",
                "metadata": {"domain": "tech", "language": "fr"}
            },
            "business_context": {
                "description": "Contexte business et stratégique",
                "metadata": {"domain": "business", "language": "fr"}
            }
        }
        
        for collection_name, config in collection_configs.items():
            try:
                collection = self.chroma_client.create_collection(
                    name=collection_name,
                    metadata=config["metadata"]
                )
                self.knowledge_collections[collection_name] = collection
                print(f"✅ Collection créée: {collection_name}")
            except Exception as e:
                # Collection existe déjà
                collection = self.chroma_client.get_collection(collection_name)
                self.knowledge_collections[collection_name] = collection
                print(f"♻️ Collection existante: {collection_name}")
        
        # Peupler avec des connaissances de base
        self._seed_knowledge_base()
        
        print(f"🎯 Base de connaissances initialisée: {len(self.knowledge_collections)} collections")
    
    def _seed_knowledge_base(self):
        """Peupler la base avec des connaissances initiales"""
        
        # Connaissances IA
        ai_documents = [
            {
                "id": "ai_001",
                "content": "L'intelligence artificielle (IA) est une technologie qui permet aux machines de simuler l'intelligence humaine. Elle comprend l'apprentissage automatique, le traitement du langage naturel, la vision par ordinateur et la robotique.",
                "metadata": {"category": "definition", "importance": "high"}
            },
            {
                "id": "ai_002", 
                "content": "Les agents IA sont des systèmes autonomes capables de percevoir leur environnement, de prendre des décisions et d'agir pour atteindre des objectifs spécifiques. Ils suivent généralement une boucle Perception → Plan → Act → Reflect.",
                "metadata": {"category": "agents", "importance": "high"}
            },
            {
                "id": "ai_003",
                "content": "Le RAG (Retrieval-Augmented Generation) combine la récupération d'informations avec la génération de texte. Il permet aux modèles de langage d'accéder à des connaissances externes spécifiques et actualisées.",
                "metadata": {"category": "rag", "importance": "medium"}
            },
            {
                "id": "ai_004",
                "content": "Les LLM (Large Language Models) comme GPT-4 sont des modèles de langage pré-entraînés sur de vastes corpus de texte. Ils excellent dans la compréhension et la génération de langage naturel.",
                "metadata": {"category": "llm", "importance": "high"}
            }
        ]
        
        # Documents techniques
        tech_documents = [
            {
                "id": "tech_001",
                "content": "Python est un langage de programmation polyvalent largement utilisé en IA. Il offre de nombreuses bibliothèques comme TensorFlow, PyTorch, scikit-learn pour le machine learning et OpenAI pour les LLM.",
                "metadata": {"category": "programming", "importance": "medium"}
            },
            {
                "id": "tech_002",
                "content": "Les bases de données vectorielles comme ChromaDB, Pinecone ou Weaviate sont essentielles pour implémenter des systèmes RAG efficaces. Elles permettent la recherche sémantique basée sur la similarité.",
                "metadata": {"category": "databases", "importance": "medium"}
            },
            {
                "id": "tech_003",
                "content": "Les embeddings sont des représentations vectorielles de texte qui capturent le sens sémantique. Des modèles comme sentence-transformers génèrent des embeddings de haute qualité pour la recherche sémantique.",
                "metadata": {"category": "embeddings", "importance": "high"}
            }
        ]
        
        # Contexte business
        business_documents = [
            {
                "id": "biz_001",
                "content": "L'implémentation d'agents IA en entreprise nécessite une stratégie claire, une gouvernance des données et une formation des équipes. Les ROI peuvent être significatifs mais les risques doivent être gérés.",
                "metadata": {"category": "strategy", "importance": "high"}
            },
            {
                "id": "biz_002",
                "content": "Les cas d'usage d'IA les plus rentables incluent l'automatisation des processus, l'analyse prédictive, la personnalisation client et l'optimisation opérationnelle.",
                "metadata": {"category": "use_cases", "importance": "medium"}
            }
        ]
        
        # Ajouter les documents aux collections
        self._add_documents_to_collection("ai_knowledge", ai_documents)
        self._add_documents_to_collection("technical_docs", tech_documents) 
        self._add_documents_to_collection("business_context", business_documents)
        
        print("📚 Base de connaissances peuplée avec les documents initiaux")
    
    def _add_documents_to_collection(self, collection_name: str, documents: List[Dict]):
        """Ajouter des documents à une collection"""
        collection = self.knowledge_collections[collection_name]
        
        # Préparer les données
        ids = [doc["id"] for doc in documents]
        contents = [doc["content"] for doc in documents]
        metadatas = [doc["metadata"] for doc in documents]
        
        # Générer les embeddings
        embeddings = self.embedding_model.encode(contents).tolist()
        
        # Ajouter à la collection
        collection.add(
            ids=ids,
            documents=contents,
            embeddings=embeddings,
            metadatas=metadatas
        )
        
        print(f"   📄 {len(documents)} documents ajoutés à {collection_name}")
    
    async def process_rag_query(self, query: str, collections: Optional[List[str]] = None) -> Dict[str, Any]:
        """Traiter une requête avec RAG"""
        print(f"\n🔍 RAG QUERY: {query}")
        print("=" * 60)
        
        # Sélectionner les collections à interroger
        if collections is None:
            collections = list(self.knowledge_collections.keys())
        
        # Phase 1: Récupération (Retrieval)
        retrieval_results = await self._retrieve_relevant_knowledge(query, collections)
        
        # Phase 2: Reranking et filtrage
        filtered_results = self._rerank_and_filter_results(query, retrieval_results)
        
        # Phase 3: Construction du contexte
        context = self._build_rag_context(filtered_results)
        
        # Phase 4: Génération augmentée
        generated_response = await self._generate_with_context(query, context)
        
        # Phase 5: Vérification et validation
        verification = await self._verify_response_accuracy(query, generated_response, filtered_results)
        
        # Compiler les résultats
        result = {
            "query": query,
            "collections_searched": collections,
            "retrieved_documents": len(retrieval_results),
            "filtered_documents": len(filtered_results),
            "context_length": len(context),
            "generated_response": generated_response,
            "source_documents": filtered_results,
            "verification": verification,
            "rag_quality_score": self._calculate_rag_quality(retrieval_results, generated_response, verification),
            "success": verification.get("factual_accuracy", 0) > 0.7
        }
        
        print(f"✅ RAG traitement terminé:")
        print(f"   • Documents récupérés: {result['retrieved_documents']}")
        print(f"   • Documents pertinents: {result['filtered_documents']}")
        print(f"   • Score qualité RAG: {result['rag_quality_score']:.2f}")
        print(f"   • Exactitude factuelle: {verification.get('factual_accuracy', 0):.2f}")
        
        return result
    
    async def _retrieve_relevant_knowledge(self, query: str, collections: List[str]) -> List[Dict]:
        """Récupérer les connaissances pertinentes"""
        all_results = []
        
        # Générer l'embedding de la requête
        query_embedding = self.embedding_model.encode([query])[0].tolist()
        
        print(f"🔎 Recherche dans {len(collections)} collections...")
        
        for collection_name in collections:
            collection = self.knowledge_collections[collection_name]
            
            # Rechercher dans la collection
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=self.retrieval_config["top_k"],
                include=["documents", "metadatas", "distances"]
            )
            
            # Traiter les résultats
            if results["documents"] and len(results["documents"]) > 0:
                for i, (doc, metadata, distance) in enumerate(zip(
                    results["documents"][0],
                    results["metadatas"][0], 
                    results["distances"][0]
                )):
                    similarity = 1 - distance  # Convertir distance en similarité
                    
                    if similarity >= self.retrieval_config["similarity_threshold"]:
                        all_results.append({
                            "collection": collection_name,
                            "document": doc,
                            "metadata": metadata,
                            "similarity": similarity,
                            "distance": distance,
                            "rank": i + 1
                        })
            
            print(f"   📚 {collection_name}: {len([r for r in all_results if r['collection'] == collection_name])} documents pertinents")
        
        # Trier par similarité globale
        all_results.sort(key=lambda x: x["similarity"], reverse=True)
        
        return all_results
    
    def _rerank_and_filter_results(self, query: str, results: List[Dict]) -> List[Dict]:
        """Reranker et filtrer les résultats"""
        if not self.retrieval_config["rerank_results"]:
            return results
        
        print("🔄 Reranking et filtrage des résultats...")
        
        # Filtrer par seuil de similarité
        filtered = [r for r in results if r["similarity"] >= self.retrieval_config["similarity_threshold"]]
        
        # Reranking basé sur plusieurs critères
        for result in filtered:
            rerank_score = result["similarity"]
            
            # Bonus pour l'importance
            importance = result["metadata"].get("importance", "medium")
            if importance == "high":
                rerank_score *= 1.2
            elif importance == "low":
                rerank_score *= 0.8
            
            # Bonus pour la correspondance de catégorie
            query_lower = query.lower()
            category = result["metadata"].get("category", "")
            if category and category in query_lower:
                rerank_score *= 1.15
            
            result["rerank_score"] = rerank_score
        
        # Re-trier par score de reranking
        filtered.sort(key=lambda x: x["rerank_score"], reverse=True)
        
        # Limiter le nombre de résultats
        max_results = min(self.retrieval_config["top_k"], len(filtered))
        final_results = filtered[:max_results]
        
        print(f"   🎯 {len(final_results)} documents après reranking")
        
        return final_results
    
    def _build_rag_context(self, filtered_results: List[Dict]) -> str:
        """Construire le contexte RAG"""
        if not filtered_results:
            return "Aucune information pertinente trouvée dans la base de connaissances."
        
        context_parts = ["Informations pertinentes de la base de connaissances:\n"]
        current_length = len(context_parts[0])
        
        for i, result in enumerate(filtered_results, 1):
            doc_context = f"{i}. [{result['collection']}] {result['document']}\n"
            doc_context += f"   Pertinence: {result['similarity']:.2f}\n\n"
            
            # Vérifier la limite de longueur
            if current_length + len(doc_context) > self.retrieval_config["max_context_length"]:
                break
            
            context_parts.append(doc_context)
            current_length += len(doc_context)
        
        context = "".join(context_parts)
        
        print(f"📝 Contexte construit: {len(context)} caractères")
        
        return context
    
    async def _generate_with_context(self, query: str, context: str) -> str:
        """Générer une réponse avec le contexte RAG"""
        system_prompt = """Tu es un assistant IA expert qui utilise des informations de base de connaissances pour répondre aux questions.

Instructions importantes:
- Utilise UNIQUEMENT les informations fournies dans le contexte
- Si l'information n'est pas dans le contexte, dis-le clairement
- Cite les sources quand tu utilises des informations spécifiques
- Sois précis et factuel
- Indique ton niveau de confiance dans la réponse"""
        
        user_prompt = f"""Contexte de la base de connaissances:
{context}

Question de l'utilisateur: {query}

Réponds en utilisant les informations du contexte ci-dessus. Si certaines informations manquent, indique-le clairement."""
        
        # Simulation de génération LLM avec contexte
        # En production: appel réel à l'API OpenAI avec le contexte
        generated_response = f"""Basé sur les informations de la base de connaissances, voici ma réponse à votre question "{query}":

D'après les documents consultés, {query.lower()} implique plusieurs aspects importants. Les informations disponibles indiquent que ce sujet est bien documenté dans notre base de connaissances.

Les points clés identifiés sont:
- Les concepts fondamentaux sont clairement définis
- Les applications pratiques sont documentées
- Les considérations techniques sont détaillées

Cette réponse est basée sur {len(context.split('.'))} éléments d'information de la base de connaissances, avec un niveau de confiance élevé pour les aspects couverts.

Note: Cette réponse utilise exclusivement les informations disponibles dans la base de connaissances consultée."""
        
        return generated_response
    
    async def _verify_response_accuracy(self, query: str, response: str, source_docs: List[Dict]) -> Dict[str, Any]:
        """Vérifier l'exactitude de la réponse"""
        verification = {
            "factual_accuracy": 0.0,
            "source_alignment": 0.0,
            "completeness": 0.0,
            "confidence_level": 0.0,
            "verification_notes": []
        }
        
        # Vérifier l'alignement avec les sources
        if source_docs:
            # Calculer l'alignement sémantique
            response_words = set(response.lower().split())
            source_words = set()
            
            for doc in source_docs:
                doc_words = set(doc["document"].lower().split())
                source_words.update(doc_words)
            
            if source_words:
                alignment = len(response_words.intersection(source_words)) / len(response_words.union(source_words))
                verification["source_alignment"] = alignment
            
            # Évaluer l'exactitude factuelle (basée sur la similarité avec les sources)
            avg_similarity = sum(doc["similarity"] for doc in source_docs) / len(source_docs)
            verification["factual_accuracy"] = avg_similarity
            
            verification["verification_notes"].append(f"Alignement avec {len(source_docs)} sources")
        
        # Évaluer la complétude
        query_concepts = len(query.split())
        response_concepts = len(response.split())
        
        if query_concepts > 0:
            completeness = min(1.0, response_concepts / (query_concepts * 10))  # Heuristique
            verification["completeness"] = completeness
        
        # Niveau de confiance global
        verification["confidence_level"] = (
            verification["factual_accuracy"] * 0.4 +
            verification["source_alignment"] * 0.3 +
            verification["completeness"] * 0.3
        )
        
        if verification["confidence_level"] > 0.8:
            verification["verification_notes"].append("Haute confiance dans la réponse")
        elif verification["confidence_level"] > 0.6:
            verification["verification_notes"].append("Confiance modérée")
        else:
            verification["verification_notes"].append("Confiance faible - vérification recommandée")
        
        return verification
    
    def _calculate_rag_quality(self, retrieval_results: List[Dict], response: str, verification: Dict) -> float:
        """Calculer la qualité globale du processus RAG"""
        quality_factors = {
            "retrieval_quality": 0.0,
            "context_relevance": 0.0,
            "generation_quality": 0.0,
            "factual_accuracy": verification.get("factual_accuracy", 0.0)
        }
        
        # Qualité de récupération
        if retrieval_results:
            avg_similarity = sum(r["similarity"] for r in retrieval_results) / len(retrieval_results)
            quality_factors["retrieval_quality"] = avg_similarity
        
        # Pertinence du contexte
        high_similarity_docs = [r for r in retrieval_results if r["similarity"] > 0.8]
        if retrieval_results:
            quality_factors["context_relevance"] = len(high_similarity_docs) / len(retrieval_results)
        
        # Qualité de génération (basée sur la longueur et structure de la réponse)
        if response:
            # Heuristiques simples pour évaluer la qualité
            word_count = len(response.split())
            has_structure = any(marker in response for marker in [":", "-", "•", "1.", "2."])
            
            generation_quality = 0.5  # Score de base
            if word_count >= 50:
                generation_quality += 0.2
            if word_count >= 100:
                generation_quality += 0.1
            if has_structure:
                generation_quality += 0.2
            
            quality_factors["generation_quality"] = min(1.0, generation_quality)
        
        # Score global pondéré
        overall_quality = (
            quality_factors["retrieval_quality"] * 0.25 +
            quality_factors["context_relevance"] * 0.25 +
            quality_factors["generation_quality"] * 0.25 +
            quality_factors["factual_accuracy"] * 0.25
        )
        
        return overall_quality
    
    async def add_knowledge_document(self, collection_name: str, document: Dict[str, Any]) -> bool:
        """Ajouter un nouveau document à la base de connaissances"""
        try:
            if collection_name not in self.knowledge_collections:
                print(f"❌ Collection {collection_name} n'existe pas")
                return False
            
            # Ajouter le document
            self._add_documents_to_collection(collection_name, [document])
            
            print(f"✅ Document ajouté à {collection_name}: {document['id']}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur lors de l'ajout du document: {e}")
            return False
    
    async def demonstrate_rag_capabilities(self):
        """Démonstration des capacités RAG"""
        print(f"\n🎬 DÉMONSTRATION: Pattern RAG Agent")
        print("=" * 80)
        
        demo_queries = [
            "Qu'est-ce que l'intelligence artificielle ?",
            "Comment fonctionnent les agents IA ?", 
            "Quels sont les avantages du RAG ?",
            "Quel langage de programmation utiliser pour l'IA ?",
            "Comment implémenter l'IA en entreprise ?",
            "Que sont les embeddings ?"
        ]
        
        results = []
        
        for i, query in enumerate(demo_queries, 1):
            print(f"\n--- Requête RAG {i}/{len(demo_queries)} ---")
            print(f"❓ Question: {query}")
            
            result = await self.process_rag_query(query)
            results.append(result)
            
            print(f"\n📊 Résultats pour la requête {i}:")
            print(f"   • Documents trouvés: {result['retrieved_documents']}")
            print(f"   • Documents pertinents: {result['filtered_documents']}")
            print(f"   • Exactitude factuelle: {result['verification']['factual_accuracy']:.2f}")
            print(f"   • Score qualité RAG: {result['rag_quality_score']:.2f}")
            print(f"   • Succès: {'Oui' if result['success'] else 'Non'}")
            print(f"   • Réponse: {result['generated_response'][:150]}...")
        
        # Statistiques globales
        print(f"\n📈 STATISTIQUES RAG")
        print("=" * 60)
        
        total_queries = len(results)
        successful_queries = sum(1 for r in results if r["success"])
        avg_quality = sum(r["rag_quality_score"] for r in results) / total_queries
        avg_accuracy = sum(r["verification"]["factual_accuracy"] for r in results) / total_queries
        total_docs_retrieved = sum(r["retrieved_documents"] for r in results)
        
        print(f"📊 Total requêtes: {total_queries}")
        print(f"✅ Requêtes réussies: {successful_queries} ({successful_queries/total_queries:.1%})")
        print(f"🎯 Qualité RAG moyenne: {avg_quality:.2f}")
        print(f"📚 Exactitude factuelle moyenne: {avg_accuracy:.2f}")
        print(f"🔍 Total documents récupérés: {total_docs_retrieved}")
        print(f"💾 Collections actives: {len(self.knowledge_collections)}")
        
        return results
```

I'll continue with the remaining TODOs in my next response to complete the comprehensive guide for Module 3.