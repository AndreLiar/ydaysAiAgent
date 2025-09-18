"""
🎓 AI AGENTS COMPLETE TUTORIAL & DEMO
=====================================

This script demonstrates all three types of AI agents you've learned:
1. Simple Agent (Perceive → Plan → Act → Reflect)
2. Tool-Using Agent (Agent + External Tools)
3. Multi-Agent System (Collaborative Agents)

Author: Your AI Tutor
Date: 2024
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("🎓 AI AGENTS COMPLETE TUTORIAL")
    print("=" * 70)
    print("Welcome to your comprehensive AI agents tutorial!")
    print("You've successfully implemented 3 different types of AI agents:")
    print()
    
    # Demo menu
    while True:
        print("\n🤖 CHOOSE AN AGENT TO TEST:")
        print("=" * 40)
        print("1. 🧠 Simple Agent (Basic PPAR cycle)")
        print("2. 🛠️ Tool-Using Agent (Agent + Web Search)")
        print("3. 👥 Multi-Agent System (Collaborative team)")
        print("4. 📚 Learn about AI Agent concepts")
        print("5. 🚪 Exit")
        print()
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            demo_simple_agent()
        elif choice == "2":
            demo_tool_agent()
        elif choice == "3":
            demo_multi_agent()
        elif choice == "4":
            show_concepts()
        elif choice == "5":
            print("\n🎉 Thanks for learning about AI agents!")
            print("You now understand:")
            print("✅ Simple Agent Pattern (PPAR)")
            print("✅ Tool-Using Agents")
            print("✅ Multi-Agent Collaboration")
            print("Keep building amazing AI systems! 🚀")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")

def demo_simple_agent():
    """Demonstrate the Simple Agent"""
    print("\n🧠 SIMPLE AGENT DEMO")
    print("=" * 40)
    print("The Simple Agent follows: Perceive → Plan → Act → Reflect")
    
    try:
        from simple_agent import SimpleAgent
        
        agent = SimpleAgent(role="AI Tutor")
        question = input("\nAsk the Simple Agent a question: ")
        
        print(f"\n🚀 Running Simple Agent...")
        response = agent.run(question)
        
        print(f"\n📝 Response: {response}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure simple_agent.py is in the same directory!")

def demo_tool_agent():
    """Demonstrate the Tool-Using Agent"""
    print("\n🛠️ TOOL-USING AGENT DEMO")
    print("=" * 40)
    print("This agent can use external tools like web search!")
    
    try:
        from tool_agent_demo import ToolUsingAgent
        
        agent = ToolUsingAgent()
        question = input("\nAsk a question (try something that needs current info): ")
        
        print(f"\n🚀 Running Tool-Using Agent...")
        result = agent.run(question)
        
        print(f"\n📝 Response: {result['output']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure tool_agent_demo.py is in the same directory!")

def demo_multi_agent():
    """Demonstrate the Multi-Agent System"""
    print("\n👥 MULTI-AGENT SYSTEM DEMO")
    print("=" * 40)
    print("Watch two agents collaborate: Researcher + Writer!")
    
    try:
        from multi_agent_simple import SimpleMultiAgentSystem
        
        system = SimpleMultiAgentSystem()
        topic = input("\nEnter a topic for the agents to research and write about: ")
        
        print(f"\n🚀 Running Multi-Agent System...")
        result = system.run_workflow(topic)
        
        print(f"\n📝 Final Article:")
        print("-" * 50)
        print(result)
        print("-" * 50)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure multi_agent_simple.py is in the same directory!")

def show_concepts():
    """Show AI Agent concepts and patterns"""
    print("\n📚 AI AGENT CONCEPTS")
    print("=" * 40)
    
    concepts = {
        "🧠 What is an AI Agent?": [
            "An AI system that can perceive its environment",
            "Make decisions autonomously", 
            "Take actions to achieve goals",
            "Learn and adapt from experience"
        ],
        
        "🔄 PPAR Pattern": [
            "PERCEIVE: Understand the input/environment",
            "PLAN: Decide what actions to take",
            "ACT: Execute the planned actions", 
            "REFLECT: Evaluate results and learn"
        ],
        
        "🛠️ Tool Usage": [
            "Agents can use external tools (APIs, search, calculators)",
            "Function calling allows LLMs to invoke tools",
            "Tools extend agent capabilities beyond training data",
            "Enables real-time information access"
        ],
        
        "👥 Multi-Agent Systems": [
            "Multiple specialized agents working together",
            "Each agent has specific roles and expertise",
            "Agents collaborate and share information",
            "Emergent behavior: team > individual agents"
        ],
        
        "🏗️ Agent Architecture": [
            "LLM (brain): Language model for reasoning",
            "Tools (hands): External capabilities",
            "Memory (context): Conversation and knowledge storage",
            "Planning: Multi-step reasoning and execution"
        ]
    }
    
    for concept, details in concepts.items():
        print(f"\n{concept}")
        print("-" * 30)
        for detail in details:
            print(f"  • {detail}")
    
    print(f"\n🎯 Key Takeaway:")
    print("AI Agents = LLM + Tools + Memory + Planning Loop")
    print("This pattern can solve complex, real-world problems!")

if __name__ == "__main__":
    main()