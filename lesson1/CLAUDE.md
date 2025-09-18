# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Setup and Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env to add your OpenAI API key
```

### Running the Code
```bash
# Run complete interactive demo with all agent types
python ai_agents_complete_demo.py

# Run individual agent demonstrations
python simple_agent.py               # Basic PPAR agent
python tool_agent_demo.py            # Tool-using agent with web search
python multi_agent_simple.py         # Multi-agent collaborative system
```

## Architecture Overview

This is an AI agents tutorial codebase implementing three fundamental agent patterns:

### 1. Simple Agent (`simple_agent.py`)
- **Pattern**: PPAR (Perceive-Plan-Act-Reflect) cycle
- **Core Class**: `SimpleAgent`
- Uses OpenAI API directly for basic agent functionality
- Demonstrates the foundational agent architecture

### 2. Tool-Using Agent (`tool_agent_demo.py`, `tool_agent.py`)
- **Pattern**: Agent + External Tools integration
- **Framework**: LangChain with OpenAI Functions
- **Tools**: DuckDuckGo web search capability
- **Core Class**: `ToolUsingAgent`
- Shows how agents can interact with external systems

### 3. Multi-Agent System (`multi_agent_simple.py`, `multi_agent_system.py`)
- **Pattern**: Collaborative specialist agents
- **Framework**: CrewAI for agent orchestration
- **Agents**: Researcher Agent + Writer Agent working in sequence
- **Core Class**: `SimpleMultiAgentSystem`
- Demonstrates agent collaboration and workflow management

### Key Dependencies
- **OpenAI API**: Core language model capabilities
- **LangChain**: Tool integration and agent framework
- **CrewAI**: Multi-agent collaboration framework
- **DuckDuckGo Search**: Web search tool for current information

### Environment Setup
- Requires `OPENAI_API_KEY` in `.env` file
- All agents use OpenAI models (default: GPT-4)
- Web search functionality requires internet access

### Agent Communication Patterns
- Simple Agent: Direct user ↔ agent interaction
- Tool Agent: User → Agent → Tools → Agent → User
- Multi-Agent: User → Researcher → Writer → User (sequential workflow)