from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv

load_dotenv()

class ToolUsingAgent:
    def __init__(self, model="gpt-4", temperature=0.7):
        print("🛠️ Initializing Tool-Using Agent...")
        
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        self.tools = [
            DuckDuckGoSearchRun(
                name="web_search",
                description="Search the web for current information, news, and facts. Use this when you need up-to-date information or when the user asks about recent events."
            )
        ]
        
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to web search.
            
            Guidelines:
            - Use web search for current events, recent information, or facts you're unsure about
            - Don't search for basic knowledge you already have
            - When searching, use specific and relevant search terms
            - Always explain why you're using a tool
            """),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        self.agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,
            max_iterations=3,
            return_intermediate_steps=True
        )
        
        print(f"✅ Tool-Using Agent ready with {len(self.tools)} tools!")
    
    def run(self, user_input):
        print(f"\n🚀 Tool Agent processing: '{user_input}'")
        print("=" * 70)
        
        try:
            result = self.agent_executor.invoke({"input": user_input})
            print("=" * 70)
            print("✅ Tool Agent completed!")
            return result
        except Exception as e:
            print(f"❌ Error: {e}")
            return {"output": f"Sorry, I encountered an error: {e}"}

# Demo script
if __name__ == "__main__":
    print("🎓 TOOL-USING AGENT DEMO")
    print("=" * 50)
    
    agent = ToolUsingAgent()
    
    # Test 1: Basic knowledge (should NOT use web search)
    print("\n" + "="*80)
    print("TEST 1: Basic Knowledge - Should NOT use web search")
    print("="*80)
    result1 = agent.run("What is the capital of France?")
    print(f"📝 Answer: {result1['output']}")
    
    # Test 2: Current information (should use web search)
    print("\n" + "="*80)
    print("TEST 2: Current Information - Should use web search")
    print("="*80)
    result2 = agent.run("What are the latest AI developments in 2024?")
    print(f"📝 Answer: {result2['output']}")
    
    print(f"\n🎉 Tool-Using Agent demo completed!")
    print("🎓 Key Learning: The agent intelligently decides when to use tools vs. its training data!")