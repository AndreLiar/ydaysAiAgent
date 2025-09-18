#!/usr/bin/env python3
"""
Pattern Chooser - Assistant pour choisir le bon design pattern
Analyse votre cas d'usage et recommande le pattern optimal

🎯 Objectif: Simplifier le choix du design pattern selon le contexte
"""

import json
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from enum import Enum

class PatternType(Enum):
    SINGLE_AGENT = "single_agent"
    MULTI_AGENT_COLLAB = "multi_agent_collaboration"
    HUMAN_IN_LOOP = "human_in_loop"
    SELF_CORRECTION = "self_correction"
    TOOL_USE = "tool_use"
    RAG_AGENT = "rag_agent"
    PLANNING_AGENT = "planning_agent"
    MULTI_AGENT_SYSTEM = "multi_agent_system"

@dataclass
class PatternRecommendation:
    pattern: PatternType
    confidence: float
    reasoning: List[str]
    implementation_complexity: str  # "Low", "Medium", "High"
    estimated_dev_time: str
    pros: List[str]
    cons: List[str]
    example_use_cases: List[str]

class PatternChooser:
    """
    Assistant intelligent pour choisir le bon design pattern
    """
    
    def __init__(self):
        self.pattern_definitions = self._load_pattern_definitions()
    
    def _load_pattern_definitions(self) -> Dict[PatternType, Dict]:
        """Définitions complètes des patterns"""
        return {
            PatternType.SINGLE_AGENT: {
                "name": "Single Agent",
                "description": "Un seul agent gère la tâche complètement",
                "complexity": "Low",
                "dev_time": "1-2 jours",
                "best_for": ["FAQ", "Classification", "Résumé", "Q&A simple"],
                "signals": ["tâche simple", "réponse directe", "pas d'interaction externe"],
                "pros": ["Simple", "Rapide", "Facile à debug", "Peu de ressources"],
                "cons": ["Limité", "Pas d'expertise multiple", "Pas de validation"]
            },
            
            PatternType.MULTI_AGENT_COLLAB: {
                "name": "Multi-Agent Collaboration",
                "description": "Agents spécialisés collaborent séquentiellement",
                "complexity": "Medium",
                "dev_time": "3-5 jours",
                "best_for": ["Recherche+Analyse", "Code Review", "Content Pipeline"],
                "signals": ["pipeline clair", "expertises différentes", "étapes séquentielles"],
                "pros": ["Spécialisation", "Qualité élevée", "Modulaire"],
                "cons": ["Plus complexe", "Dépendances", "Plus lent"]
            },
            
            PatternType.HUMAN_IN_LOOP: {
                "name": "Human-in-the-Loop",
                "description": "Validation humaine aux points critiques",
                "complexity": "Medium",
                "dev_time": "2-4 jours",
                "best_for": ["Décisions critiques", "Créativité", "Conformité"],
                "signals": ["fort impact", "subjectivité", "réglementation"],
                "pros": ["Sécurité", "Contrôle", "Qualité garantie"],
                "cons": ["Plus lent", "Dépendant humains", "Interruptions"]
            },
            
            PatternType.SELF_CORRECTION: {
                "name": "Self-Correction",
                "description": "Agent s'améliore par auto-validation",
                "complexity": "Medium",
                "dev_time": "2-3 jours",
                "best_for": ["Code generation", "Writing", "Data cleaning"],
                "signals": ["qualité variable", "auto-validation possible", "itératif"],
                "pros": ["Amélioration auto", "Moins d'erreurs", "Robuste"],
                "cons": ["Plus lent", "Complexe", "Peut boucler"]
            },
            
            PatternType.TOOL_USE: {
                "name": "Tool Use Agent",
                "description": "Agent sélectionne et utilise outils dynamiquement",
                "complexity": "Medium",
                "dev_time": "3-4 jours",
                "best_for": ["APIs", "Calculateur", "Données temps réel"],
                "signals": ["données externes", "calculs", "intégrations"],
                "pros": ["Très capable", "Extensible", "Intelligent"],
                "cons": ["Dépendances externes", "Gestion d'erreurs", "Sécurité"]
            },
            
            PatternType.RAG_AGENT: {
                "name": "RAG Agent",
                "description": "Récupération intelligente dans base de connaissances",
                "complexity": "Medium",
                "dev_time": "2-4 jours",
                "best_for": ["Support technique", "Documentation", "Knowledge base"],
                "signals": ["documents privés", "expertise spécialisée", "citations"],
                "pros": ["Connaissance spécialisée", "Citations", "Précis"],
                "cons": ["Setup DB vectorielle", "Qualité docs", "Maintenance"]
            },
            
            PatternType.PLANNING_AGENT: {
                "name": "Planning Agent",
                "description": "Planification multi-étapes avant exécution",
                "complexity": "High",
                "dev_time": "4-6 jours",
                "best_for": ["Gestion projet", "Stratégie", "Architecture"],
                "signals": ["multi-étapes", "dépendances", "planification"],
                "pros": ["Structuré", "Prévisible", "Optimisé"],
                "cons": ["Complexe", "Rigide", "Over-engineering"]
            },
            
            PatternType.MULTI_AGENT_SYSTEM: {
                "name": "Multi-Agent System",
                "description": "Système d'agents autonomes coordinés",
                "complexity": "High", 
                "dev_time": "1-3 semaines",
                "best_for": ["Plateforme complète", "Simulation", "Écosystème"],
                "signals": ["très complexe", "autonomie", "scalabilité"],
                "pros": ["Très puissant", "Scalable", "Autonome"],
                "cons": ["Très complexe", "Coûteux", "Debug difficile"]
            }
        }
    
    def analyze_use_case(self, description: str, requirements: Dict[str, Any]) -> PatternRecommendation:
        """
        Analyser un cas d'usage et recommander le meilleur pattern
        """
        
        # Extraire les signaux du cas d'usage
        signals = self._extract_signals(description.lower(), requirements)
        
        # Scorer chaque pattern
        pattern_scores = {}
        
        for pattern_type, pattern_def in self.pattern_definitions.items():
            score = self._score_pattern(signals, pattern_def, requirements)
            pattern_scores[pattern_type] = score
        
        # Trouver le meilleur pattern
        best_pattern = max(pattern_scores.items(), key=lambda x: x[1])
        pattern_type, confidence = best_pattern
        
        # Générer la recommandation
        return self._generate_recommendation(pattern_type, confidence, signals, requirements)
    
    def _extract_signals(self, description: str, requirements: Dict[str, Any]) -> List[str]:
        """Extraire les signaux du cas d'usage"""
        
        signals = []
        
        # Signaux de complexité
        complexity_keywords = {
            "simple": ["faq", "classification", "résumé", "simple"],
            "medium": ["analyse", "recherche", "validation", "pipeline"],
            "complex": ["système", "plateforme", "orchestration", "coordination"]
        }
        
        for level, keywords in complexity_keywords.items():
            if any(keyword in description for keyword in keywords):
                signals.append(f"complexity_{level}")
        
        # Signaux d'interaction
        if any(word in description for word in ["temps réel", "api", "base de données"]):
            signals.append("external_data")
        
        if any(word in description for word in ["validation", "approbation", "humain"]):
            signals.append("human_validation_needed")
        
        if any(word in description for word in ["documents", "connaissances", "recherche"]):
            signals.append("knowledge_intensive")
        
        # Signaux des requirements
        if requirements.get("real_time", False):
            signals.append("real_time")
            
        if requirements.get("high_accuracy", False):
            signals.append("high_accuracy_needed")
            
        if requirements.get("scalability", False):
            signals.append("scalability_needed")
            
        if requirements.get("cost_sensitive", False):
            signals.append("cost_sensitive")
        
        return signals
    
    def _score_pattern(self, signals: List[str], pattern_def: Dict, requirements: Dict) -> float:
        """Scorer un pattern selon les signaux"""
        
        score = 0.5  # Score de base
        
        # Correspondance avec signaux pattern
        pattern_signals = pattern_def.get("signals", [])
        
        for signal in signals:
            if signal.replace("_", " ") in " ".join(pattern_signals):
                score += 0.2
        
        # Ajustements selon requirements
        complexity = requirements.get("complexity_preference", "medium").lower()
        pattern_complexity = pattern_def["complexity"].lower()
        
        if complexity == pattern_complexity:
            score += 0.1
        elif abs(["low", "medium", "high"].index(complexity) - 
                 ["low", "medium", "high"].index(pattern_complexity)) > 1:
            score -= 0.2
        
        # Time constraints
        if requirements.get("tight_timeline", False) and pattern_complexity == "high":
            score -= 0.3
            
        if requirements.get("high_quality_over_speed", False) and pattern_complexity == "low":
            score -= 0.2
        
        return min(1.0, max(0.0, score))
    
    def _generate_recommendation(self, pattern_type: PatternType, confidence: float, 
                                signals: List[str], requirements: Dict) -> PatternRecommendation:
        """Générer une recommandation détaillée"""
        
        pattern_def = self.pattern_definitions[pattern_type]
        
        # Raisonnement
        reasoning = [
            f"Pattern recommandé basé sur une analyse de {len(signals)} signaux",
            f"Complexité '{pattern_def['complexity']}' correspond à vos besoins"
        ]
        
        if "external_data" in signals:
            reasoning.append("Intégration de données externes détectée")
            
        if "human_validation_needed" in signals:
            reasoning.append("Besoin de validation humaine identifié")
            
        if "knowledge_intensive" in signals:
            reasoning.append("Tâche nécessitant une base de connaissances")
        
        return PatternRecommendation(
            pattern=pattern_type,
            confidence=confidence,
            reasoning=reasoning,
            implementation_complexity=pattern_def["complexity"],
            estimated_dev_time=pattern_def["dev_time"],
            pros=pattern_def["pros"],
            cons=pattern_def["cons"],
            example_use_cases=pattern_def["best_for"]
        )
    
    def get_pattern_comparison(self, top_n: int = 3) -> Dict[PatternType, Dict]:
        """Obtenir une comparaison des top N patterns"""
        return dict(list(self.pattern_definitions.items())[:top_n])
    
    def interactive_chooser(self):
        """Mode interactif pour choisir un pattern"""
        
        print("🎯 Pattern Chooser - Assistant Interactif")
        print("=" * 50)
        
        # Collecter les informations
        print("📝 Décrivez votre cas d'usage:")
        description = input("Description: ").strip()
        
        print(f"\n⚙️ Paramètres additionnels:")
        
        # Requirements interactifs
        requirements = {}
        
        questions = [
            ("Temps réel nécessaire?", "real_time", "y"),
            ("Haute précision critique?", "high_accuracy", "y"), 
            ("Scalabilité importante?", "scalability", "y"),
            ("Budget serré?", "cost_sensitive", "y"),
            ("Timeline serrée?", "tight_timeline", "y")
        ]
        
        for question, key, positive in questions:
            answer = input(f"{question} (y/n): ").lower().strip()
            requirements[key] = answer == positive
        
        complexity_pref = input("Préférence complexité (low/medium/high): ").lower().strip()
        if complexity_pref in ["low", "medium", "high"]:
            requirements["complexity_preference"] = complexity_pref
        
        # Générer recommandation
        recommendation = self.analyze_use_case(description, requirements)
        
        # Afficher résultats
        self._display_recommendation(recommendation)
        
        return recommendation
    
    def _display_recommendation(self, rec: PatternRecommendation):
        """Afficher une recommandation formatée"""
        
        pattern_def = self.pattern_definitions[rec.pattern]
        
        print(f"\n🎯 RECOMMANDATION")
        print("=" * 50)
        print(f"📋 Pattern: {pattern_def['name']}")
        print(f"🎯 Confiance: {rec.confidence*100:.1f}%")
        print(f"⚡ Complexité: {rec.implementation_complexity}")
        print(f"⏱️ Temps dev estimé: {rec.estimated_dev_time}")
        
        print(f"\n💡 Pourquoi ce pattern?")
        for reason in rec.reasoning:
            print(f"   • {reason}")
        
        print(f"\n✅ Avantages:")
        for pro in rec.pros:
            print(f"   • {pro}")
        
        print(f"\n⚠️ Inconvénients:")
        for con in rec.cons:
            print(f"   • {con}")
        
        print(f"\n🎯 Exemples d'usage:")
        for example in rec.example_use_cases:
            print(f"   • {example}")
        
        print(f"\n📄 Description:")
        print(f"   {pattern_def['description']}")

def demo_pattern_chooser():
    """Démonstration avec cas d'usage prédéfinis"""
    
    print("🎯 Démonstration Pattern Chooser")
    print("=" * 50)
    
    chooser = PatternChooser()
    
    # Cas de test
    test_cases = [
        {
            "name": "Chatbot FAQ Simple",
            "description": "Bot qui répond aux questions fréquentes de l'entreprise",
            "requirements": {
                "real_time": True,
                "high_accuracy": False,
                "scalability": False,
                "cost_sensitive": True,
                "complexity_preference": "low"
            }
        },
        {
            "name": "Système d'Analyse Marketing",
            "description": "Analyser les données de marché, générer des insights et rédiger des rapports",
            "requirements": {
                "real_time": False,
                "high_accuracy": True,
                "scalability": True,
                "cost_sensitive": False,
                "complexity_preference": "medium"
            }
        },
        {
            "name": "Assistant Trading Automatisé",
            "description": "Agent qui analyse les marchés financiers et prend des décisions d'investissement",
            "requirements": {
                "real_time": True,
                "high_accuracy": True,
                "scalability": True,
                "cost_sensitive": False,
                "tight_timeline": False,
                "high_quality_over_speed": True
            }
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n📋 Cas {i}: {case['name']}")
        print(f"Description: {case['description']}")
        
        recommendation = chooser.analyze_use_case(case['description'], case['requirements'])
        
        pattern_name = chooser.pattern_definitions[recommendation.pattern]['name']
        print(f"🎯 Recommandation: {pattern_name} ({recommendation.confidence*100:.1f}%)")
        print(f"⏱️ Temps dev: {recommendation.estimated_dev_time}")
        
        print("💡 Justification principale:")
        print(f"   {recommendation.reasoning[0]}")
        
        print("-" * 40)

def main():
    """Point d'entrée principal"""
    
    print("🎯 AI Agent Pattern Chooser")
    print("=" * 60)
    
    chooser = PatternChooser()
    
    print("Choisissez un mode:")
    print("1. Mode interactif (décrivez votre cas)")
    print("2. Démonstration avec cas prédéfinis")
    print("3. Voir tous les patterns disponibles")
    
    choice = input("\nVotre choix (1-3): ").strip()
    
    if choice == "1":
        chooser.interactive_chooser()
    elif choice == "2":
        demo_pattern_chooser()
    elif choice == "3":
        print(f"\n📋 Patterns Disponibles:")
        print("=" * 30)
        for pattern_type, pattern_def in chooser.pattern_definitions.items():
            print(f"\n🎯 {pattern_def['name']}")
            print(f"   Complexité: {pattern_def['complexity']}")
            print(f"   Temps dev: {pattern_def['dev_time']}")
            print(f"   Idéal pour: {', '.join(pattern_def['best_for'][:2])}")
    else:
        print("❌ Choix invalide, lancement démo")
        demo_pattern_chooser()
    
    print(f"\n💡 Pro Tip: Commencez simple, ajoutez la complexité seulement quand nécessaire!")

if __name__ == "__main__":
    main()