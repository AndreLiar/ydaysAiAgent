from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv

load_dotenv()

class ToolUsingAgent:
    def __init__(self, model="gpt-4", temperature=0.7):
        """
        🎓 TUTORIAL: Tool-Using Agent
        
        This agent demonstrates how to give AI agents access to external tools.
        Key concepts:
        - TOOLS: External functions the agent can call (web search, calculators, APIs)
        - FUNCTION CALLING: LLM decides when and how to use tools
        - REASONING: Agent reasons about which tool to use and when
        
        The agent can:
        - Search the web for current information
        - Reason about when to use tools vs. internal knowledge
        - Chain multiple tool calls together
        
        Args:
            model (str): The LLM model to use
            temperature (float): Creativity level (0.0 = focused, 1.0 = creative)
        """
        print("🛠️ Initializing Tool-Using Agent...")
        
        # Initialize the language model
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Initialize tools - these are the "hands" of our agent
        self.tools = [
            DuckDuckGoSearchRun(
                name="web_search",
                description="Search the web for current information, news, and facts. Use this when you need up-to-date information or when the user asks about recent events."
            )
        ]
        
        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to web search.
            
            🎓 TUTORIAL: How to use tools effectively:
            - Use web search for current events, recent information, or facts you're unsure about
            - Don't search for basic knowledge you already have
            - When searching, use specific and relevant search terms
            - Always explain why you're using a tool
            
            Guidelines:
            - Be helpful and informative
            - Explain your reasoning when using tools
            - Provide sources when you find information online
            - If you can answer from your training data, do so without searching
            """),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        # Create the agent using LangChain's function calling
        self.agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )
        
        # Create an executor to run the agent
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            verbose=True,  # This shows the agent's reasoning process
            max_iterations=3,  # Prevent infinite loops
            return_intermediate_steps=True
        )
        
        print(f"✅ Tool-Using Agent ready with {len(self.tools)} tools!")
        print(f"🔧 Available tools: {[tool.name for tool in self.tools]}")
    
    def run(self, user_input):
        """
        🎓 Execute the agent with tool access
        
        The agent will:
        1. Analyze the user's question
        2. Decide if it needs to use tools
        3. Use tools if necessary
        4. Provide a comprehensive answer
        
        Args:
            user_input (str): The user's question or request
            
        Returns:
            dict: Contains the final output and intermediate steps
        """
        print(f"\n🚀 Tool Agent processing: '{user_input}'")
        print("=" * 70)
        
        try:
            # Run the agent
            result = self.agent_executor.invoke({"input": user_input})
            
            print("=" * 70)
            print("✅ Tool Agent completed!")
            
            return {
                "output": result["output"],
                "intermediate_steps": result.get("intermediate_steps", []),
                "success": True
            }
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return {
                "output": f"Sorry, I encountered an error: {e}",
                "intermediate_steps": [],
                "success": False
            }
    
    def explain_tools(self):
        """
        🎓 Explain what tools are available and how they work
        """
        print("\n🛠️ AVAILABLE TOOLS:")
        print("=" * 50)
        
        for tool in self.tools:
            print(f"📋 {tool.name}")
            print(f"   Description: {tool.description}")
            print(f"   Type: {type(tool).__name__}")
            print()
        
        print("🎓 HOW TOOL SELECTION WORKS:")
        print("1. Agent analyzes the user's question")
        print("2. Determines if external information is needed")
        print("3. Selects appropriate tool based on the task")
        print("4. Executes tool and processes results")
        print("5. Provides final answer combining tool results with reasoning")

# Example usage and demonstrations
if __name__ == "__main__":
    print("🎓 TOOL-USING AGENT TUTORIAL")
    print("This demonstrates an AI agent that can use external tools!")
    print("\n")
    
    # Create the agent
    agent = ToolUsingAgent()
    
    # Show available tools
    agent.explain_tools()
    
    # Test cases that demonstrate different scenarios
    test_cases = [
        {
            "question": "What is the capital of France?",
            "explanation": "🎓 This should NOT use web search - it's basic knowledge"
        },
        {
            "question": "What are the latest developments in artificial intelligence in 2024?",
            "explanation": "🎓 This SHOULD use web search - needs current information"
        },
        {
            "question": "What's the current weather in Tokyo?",
            "explanation": "🎓 This SHOULD use web search - needs real-time data"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"TEST CASE {i}: {test_case['question']}")
        print(test_case['explanation'])
        print('='*80)
        
        result = agent.run(test_case['question'])
        
        if result['success']:
            print(f"\n📝 FINAL ANSWER:\n{result['output']}")
            
            # Show tool usage summary
            if result['intermediate_steps']:
                print(f"\n🔧 TOOLS USED:")
                for step in result['intermediate_steps']:
                    action = step[0]
                    print(f"   - {action.tool}: {action.tool_input}")
            else:
                print(f"\n🔧 NO TOOLS USED (answered from training data)")
        else:
            print(f"\n❌ FAILED: {result['output']}")
        
        # Pause between test cases
        if i < len(test_cases):
            input("\nPress Enter to continue to next test case...")

    print(f"\n🎉 Tool-Using Agent tutorial completed!")
    print("You've learned how agents can use external tools to access real-time information!")