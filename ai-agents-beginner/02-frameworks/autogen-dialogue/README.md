# 🤖 AutoGen - Apprentissage par Projet

## 📚 Vue d'ensemble

AutoGen de Microsoft permet de créer des conversations naturelles entre plusieurs agents IA spécialisés. Chaque agent a un rôle défini et peut collaborer avec d'autres pour résoudre des problèmes complexes.

### 🎯 Cas d'usage principaux
- **Brainstorming collaboratif** : Équipes créatives multi-perspectives
- **Code review automatisé** : Analyse technique par spécialistes
- **Analyse collaborative** : Recherche et synthèse d'informations
- **Human-in-the-loop** : Intégration de validation humaine

## 📂 Structure du Projet

```
autogen-dialogue/
├── my_research_team_starter.py  # 🎯 Template principal avec TODOs guidés
├── STEP_BY_STEP_GUIDE.md         # 📖 Guide d'apprentissage progressif
└── [Fichiers générés]            # 📄 Outputs du projet (auto-générés)
```

### 🎓 Approche Pédagogique
Ce module utilise l'**apprentissage par projet** : vous apprenez AutoGen en construisant une équipe collaborative avec 11 étapes guidées.

## 🚀 Installation

```bash
# Dépendance principale
pip install autogen-agentchat

# Dépendances pour les LLMs
pip install openai

# Pour les fonctionnalités avancées
pip install python-dotenv
```

## ⚙️ Configuration

Créez un fichier `.env` :

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Configuration LLM dans AutoGen :
```python
llm_config = {
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.7
}
```

## 🚀 Démarrage du Projet

### 📖 Guide Complet d'Apprentissage

1. **Lisez le guide étape par étape** : [`STEP_BY_STEP_GUIDE.md`](./STEP_BY_STEP_GUIDE.md)
2. **Ouvrez le template** : [`my_research_team_starter.py`](./my_research_team_starter.py)
3. **Suivez les 11 TODOs** dans l'ordre pour apprendre

### 🎯 Progression d'Apprentissage

```bash
# 1. Installer et configurer
pip install autogen-agentchat openai python-dotenv
cp .env.example .env  # Ajouter votre OPENAI_API_KEY

# 2. Lancer le template
python my_research_team_starter.py

# 3. Suivre les TODOs dans l'ordre :
#    TODO 1-2: Setup et imports
#    TODO 3-4: Métriques et logging
#    TODO 5-6: Initialisation et agents
#    TODO 7-8: GroupChat et recherche collaborative
#    TODO 9-11: Rapport, performances et démo
```

### 📚 Ce que Vous Apprendrez

| TODO | Concept | Durée |
|------|---------|-------|
| 1-2 | **Écosystème AutoGen** - Imports et architecture | 5 min |
| 3-4 | **Métriques et logging** - Traçabilité multi-agents | 10 min |
| 5-6 | **Agents spécialisés** - Rôles et personnalités | 23 min |
| 7-8 | **GroupChat et collaboration** - Orchestration | 30 min |
| 9-11 | **Rapports et métriques** - Production | 15 min |

## 🎬 Votre Équipe Collaborative en Action

### 🤖 **Ce que Votre Équipe AutoGen Fera Concrètement**

**Démonstration avec le sujet "Impact de l'IA sur l'éducation"** :

```
🎯 USER: "Analysez l'impact de l'IA sur l'éducation"

👥 ÉQUIPE COLLABORATIVE AUTOGEN:

🔍 Researcher: "Je vais explorer 3 dimensions clés:
   - Transformation pédagogique (IA tuteurs, apprentissage adaptatif)
   - Impact sur les enseignants (automatisation, nouvelles compétences)
   - Enjeux éthiques (équité numérique, protection données)"

📊 Analyst: "Analysant les données du Researcher:
   - 67% des enseignants utilisent déjà des outils IA (source: EdTech Report 2024)
   - Apprentissage adaptatif améliore performances de 30% (MIT Study)
   - Risque: creuser fossé numérique entre établissements"

✍️ Writer: "Synthèse structurée:
   ## Impact Positif
   - Personnalisation apprentissage à grande échelle
   - Libération temps enseignant pour accompagnement
   
   ## Défis Critiques  
   - Formation massive nécessaire
   - Investissements infrastructure"

👤 Human Validator: "Points à valider avec vous:
   1. Cette analyse couvre-t-elle vos priorités stratégiques?
   2. Faut-il approfondir l'aspect formation des enseignants?
   3. Quels sont vos enjeux spécifiques d'établissement?"

📝 RAPPORT FINAL GÉNÉRÉ:
   "Rapport_IA_Education_2024.md" - 15 pages structurées
   "Conversation_log.md" - Historique complet des échanges
   "Performance_metrics.json" - Métriques de l'équipe

⏱️ Temps total: 8 minutes | 🤝 Validation humaine: 3 points | ✅ Consensus atteint
```

### 🏆 **Résultat Final Concret**

À la fin, vous aurez une **équipe collaborative intelligente** qui :
- **Orchestration naturelle** : Researcher → Analyst → Writer → Human Validator  
- **Validation temps réel** : Points de contrôle humain intégrés dans le flux
- **Rapports professionnels** : Documents markdown structurés avec sources
- **Métriques d'équipe** : Performance, collaboration, consensus
- **Historique complet** : Traçabilité de toutes les conversations

## 🎓 Validation des Compétences

### ✅ **Critères de Réussite**

Votre projet est réussi quand vous avez complété **tous les TODOs** et votre système :

#### 📊 **Performance** :
- Génère des conversations < 15 tours
- Intègre la validation humaine naturellement
- Produit des rapports structurés

#### 🎯 **Fonctionnalités** :
- Équipe d'agents spécialisés (Researcher, Analyst, Writer, Human Validator)
- Conversation collaborative orchestrée intelligemment
- Human-in-the-loop avec validation en temps réel
- Génération automatique de rapports et métriques

#### 🎬 **Démonstration** :
Votre système doit réussir la démonstration automatique avec un sujet de recherche complexe.

### 📁 **Fichiers Générés**

Après complétion des TODOs, vous aurez créé :
```
autogen-dialogue/
├── my_research_team_starter.py  # ✅ Votre implémentation complète
├── final_report.md              # ✅ Rapport de recherche structuré
├── conversation_log.md          # ✅ Transcription des échanges
├── team_performance.json        # ✅ Métriques de l'équipe
└── STEP_BY_STEP_GUIDE.md        # 📖 Guide de référence
```

### 🏆 **Validation Finale**

Pour valider vos acquis, vous devez pouvoir :
- [ ] Expliquer l'orchestration de conversations multi-agents
- [ ] Modifier les rôles d'agents pour votre domaine
- [ ] Intégrer efficacement la validation humaine
- [ ] Analyser les métriques de performance d'équipe
- [ ] Adapter le workflow pour différents types de recherche

## 🎓 Exercices progressifs

### Niveau Débutant
1. **Modifiez les rôles** dans `two-agent-chat.py`
2. **Ajoutez un 3ème agent** à une conversation simple
3. **Testez différentes températures** et observez les variations

### Niveau Intermédiaire
1. **Créez votre équipe spécialisée** pour votre domaine
2. **Implémentez un workflow** avec validation humaine
3. **Optimisez la sélection** des speakers dans GroupChat

### Niveau Avancé
1. **Intégrez des outils externes** aux agents
2. **Implémentez de la mémoire persistante** entre sessions
3. **Créez un système de scoring** pour la qualité des réponses

## 🔧 Patterns avancés

### Pattern Agent avec Tools
```python
from autogen import UserProxyAgent

user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)
```

### Pattern Conditional Routing
```python
def custom_speaker_selection(last_speaker, groupchat):
    if "technical" in last_speaker.last_message:
        return tech_expert
    elif "business" in last_speaker.last_message:
        return business_expert
    return None
```

### Pattern Memory Integration
```python
class MemoryAgent(ConversableAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = []
    
    def remember(self, information):
        self.memory.append(information)
```

## 📊 Métriques de qualité

### Performance conversations :
- **Pertinence** : Agents restent dans leur rôle
- **Cohérence** : Pas de contradictions
- **Progression** : Avancement vers l'objectif
- **Engagement** : Participation équilibrée

### Métriques techniques :
- **Latence moyenne** : < 3s par réponse
- **Taux d'erreur** : < 5%
- **Satisfaction utilisateur** : > 85%

## 🚨 Troubleshooting

### Erreurs courantes :

**❌ "Conversation stuck in loop"**
```python
# Limitez les tours automatiques
max_consecutive_auto_reply=3
```

**❌ "Agent doesn't follow role"**
```python
# Renforcez le system_message
system_message="Tu es STRICTEMENT un expert en... Tu ne sors JAMAIS de ce rôle."
```

**❌ "Too many API calls"**
```python
# Optimisez le GroupChat
groupchat = GroupChat(
    max_round=8,  # Limitez les tours
    speaker_selection_method="manual"  # Contrôle précis
)
```

**❌ "Human input timeout"**
```python
# Mode non-interactif pour tests
human_input_mode="NEVER"
```

## 🔄 Best Practices

### 🎯 Design d'agents :
- **Rôles clairs** et spécifiques
- **Personnalités distinctes** pour éviter la redondance
- **Objectifs alignés** avec la tâche globale

### 💬 Gestion conversations :
- **Limiter les tours** pour éviter les boucles
- **Surveiller la pertinence** des échanges
- **Intervenir humainement** si nécessaire

### 🔧 Optimisation :
- **Caching** des réponses similaires
- **Batching** des requêtes API
- **Monitoring** des performances

## 🔗 Ressources complémentaires

### Documentation officielle :
- [AutoGen GitHub](https://github.com/microsoft/autogen)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Examples Gallery](https://github.com/microsoft/autogen/tree/main/notebook)

### Communauté :
- [AutoGen Discussions](https://github.com/microsoft/autogen/discussions)
- [Discord AutoGen](https://discord.gg/pAbnFJrkgZ)

### Tutoriels :
- [Multi-Agent Conversations](https://microsoft.github.io/autogen/docs/tutorial/conversation-patterns)
- [Human Feedback](https://microsoft.github.io/autogen/docs/tutorial/human-in-the-loop)

## 💡 Cas d'usage inspirants

### 🏢 Entreprise :
- **Comité de direction IA** pour décisions stratégiques
- **Équipe R&D virtuelle** pour innovation produit
- **Support client multi-niveau** avec escalation

### 🎓 Éducation :
- **Débats académiques** entre perspectives différentes
- **Tutorat collaboratif** avec spécialistes
- **Évaluation par les pairs** automatisée

### 🏥 Santé :
- **Consultation pluridisciplinaire** virtuelle
- **Analyse de cas cliniques** collaborative
- **Formation médicale** par simulation

---

🎯 **Objectif final** : Maîtriser AutoGen pour créer des équipes d'agents collaboratifs intelligents et naturels !