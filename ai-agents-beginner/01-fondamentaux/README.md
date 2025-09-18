# 📖 Module 1: Fondamentaux des Agents IA

## 🎯 Objectifs d'Apprentissage (3h)

À la fin de ce module, vous saurez :
- ✅ Implémenter la boucle agentique fondamentale 
- ✅ Comprendre l'équation : **LLM + Tools + Memory = Agent**
- ✅ Appliquer les 8 design patterns essentiels

## 🔄 Le Loop Agentique Universel

**Perception → Plan → Act → Reflect**

Tous les agents, qu'ils soient simples ou complexes, suivent cette boucle :

```python
class BaseAgent:
    def perceive(self, input_data) -> Dict[str, Any]:
        """Analyser l'input et le contexte"""
        pass
    
    def plan(self, perception) -> List[Dict[str, Any]]:
        """Créer un plan d'action"""
        pass
    
    def act(self, plan) -> List[Dict[str, Any]]:
        """Exécuter les actions planifiées"""
        pass
    
    def reflect(self, results, expected_outcome) -> Dict[str, Any]:
        """Évaluer les résultats et s'améliorer"""
        pass
```

## 📝 Exercices Pratiques

### 1. `agentic-loop.py` - Votre Premier Agent
Implémentez un agent simple qui :
- Perçoit une question utilisateur
- Planifie sa réponse 
- Agit en appelant un LLM
- Réfléchit sur la qualité de sa réponse

### 2. `llm-tools-memory.py` - Les 3 Composants
Créez un agent avec :
- **LLM** : GPT-4 pour le raisonnement
- **Tools** : calculatrice + recherche web
- **Memory** : historique des conversations

### 3. `design-patterns.py` - 8 Patterns Essentiels
Implémentez et testez chacun des 8 patterns :

1. **Single Agent** → Q&A simple
2. **Multi-Agent** → Orchestrateur + spécialistes
3. **Human-in-Loop** → Validation humaine
4. **Self-Correction** → Auto-amélioration
5. **Tool Use** → Sélection dynamique d'outils
6. **RAG Agent** → Récupération intelligente
7. **Planning Agent** → Décomposition de tâches
8. **Multi-Agent System** → Équipe collaborative

## ✅ Validation

À la fin du module, votre agent devra :
- [ ] Suivre la boucle Perception → Plan → Act → Reflect
- [ ] Utiliser au moins 2 outils différents
- [ ] Maintenir un historique des conversations
- [ ] Démontrer au moins 3 design patterns

## 🚀 Next Steps

Une fois ce module maîtrisé, passez au **Module 2: Frameworks** pour découvrir LangChain, AutoGen, CrewAI et Semantic Kernel.

---

💡 **Astuce**: Gardez vos implémentations simples au début. La complexité viendra naturellement avec l'expérience !