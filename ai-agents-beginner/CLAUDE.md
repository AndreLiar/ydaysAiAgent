# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Setup and Environment
```bash
# Initial setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.template .env

# Quick test
cd 01-fondamentaux && python agentic-loop.py
```

### Module Development
```bash
# Run module examples
cd 01-fondamentaux && python agentic-loop.py
cd 02-frameworks/langchain-langgraph && python workflow-demo.py
cd 04-portfolio-projects/customer-service && python chat-support-bot.py

# Test portfolio projects
cd 04-portfolio-projects/ecommerce && python product-recommender.py --demo
cd 04-portfolio-projects/research-team && python orchestrator.py --query "AI agents"
```

### Production Deployment
```bash
# Build and run with Docker
cd 05-deployment/docker && docker build -t ai-agent .
docker run -p 8000:8000 ai-agent

# Start FastAPI development server
cd 04-portfolio-projects/customer-service && uvicorn api:app --reload
```

### Code Quality
```bash
# Format code (if black is installed)
black src/ tests/

# Lint code (if ruff is installed) 
ruff check src/ tests/

# Type checking (if mypy is installed)
mypy src/
```

## Architecture Overview

### Ydays Lab Structure
This is a **2-day intensive lab** focused on building **portfolio-ready AI agent projects**. The structure prioritizes hands-on development of real-world applications over comprehensive theory.

### Agentic Loop Foundation
All agents implement the universal **Perception → Plan → Act → Reflect** pattern. This is demonstrated in `01-fondamentaux/agentic-loop.py` and used consistently across all portfolio projects.

### Module Organization
The lab is organized in 5 focused modules:

1. **01-fondamentaux**: Core agentic patterns and design principles
2. **02-frameworks**: Modern AI frameworks (LangChain, AutoGen, CrewAI, Semantic Kernel)
3. **03-design-patterns**: 8 essential patterns for different use cases
4. **04-portfolio-projects**: 5 real-world applications with business metrics
5. **05-deployment**: Production deployment with Docker and monitoring

### Shared Components
- **shared/base_agent.py**: Universal agentic loop implementation
- **shared/tools.py**: Common tools (calculator, search, API integration)
- **shared/memory.py**: Memory systems (conversation, vector storage)
- **shared/protocols.py**: Communication protocols for multi-agent systems

### Configuration Management
Uses layered configuration with `.env.template` → `.env` → environment variables. Supports multiple LLM providers (OpenAI, Anthropic, Google) and local models (Ollama) through provider-agnostic interfaces.

## Key Development Patterns

### Agent Implementation
When implementing new agents, inherit from `BaseAgent` and implement the four required methods. Use the existing tool registry pattern for adding capabilities. Memory integration follows the established BaseMemory interface.

### Topic Creation
New topics should follow the established pattern:
- `README.md` with learning objectives and setup instructions
- Main script demonstrating the concept
- `test_*.py` for verification  
- `requirements.txt` for any additional dependencies
- Output artifacts saved to `../../outputs/topicXX_completion.json`

### Multi-Provider LLM Integration
The course abstracts LLM providers through consistent interfaces. When adding new providers, follow the pattern of fallback mechanisms and error handling established in existing topics.

### Testing Strategy
Tests operate at three levels:
1. **Environment tests**: Project structure, dependencies, shared components
2. **Topic tests**: Individual topic functionality and artifacts
3. **Integration tests**: Cross-topic functionality and progression

### Error Handling Philosophy
The codebase prioritizes **graceful degradation** - missing API keys default to local models, missing optional dependencies are handled cleanly, and validation provides clear next steps rather than just failing.

## Course Runner Integration

The `run_course.py` script manages learning progression through JSON-based state tracking. It automatically executes topic scripts, runs tests, and maintains completion statistics. When adding new topics, ensure they're discoverable by the runner and produce the expected completion artifacts.

## Local vs Cloud Development

The architecture supports both cloud APIs and local models. Local development uses Ollama for models and SQLite for persistence. Cloud development can leverage external APIs and services. The configuration system handles both scenarios transparently.

## Production Readiness

Despite being educational, the course teaches production patterns from the start:
- Structured logging with configurable formats
- Environment-based configuration
- Error handling and retry logic
- Metrics collection and observability
- Docker containerization and CI/CD integration
- API deployment patterns with FastAPI

When working on this codebase, prioritize these production-ready patterns over quick-and-dirty solutions to maintain the educational value.