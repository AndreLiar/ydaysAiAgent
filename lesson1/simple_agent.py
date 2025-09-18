from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class SimpleAgent:
    def __init__(self, role="Assistant"):
        """
        🎓 TUTORIAL: Simple Agent Architecture
        
        This agent demonstrates the core AI agent pattern:
        - PERCEIVE: Take in information from the environment
        - PLAN: Decide what actions to take
        - ACT: Execute the planned actions
        - REFLECT: Evaluate the results
        
        Args:
            role (str): The role/persona of the agent
        """
        self.role = role
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        print(f"🤖 Simple Agent initialized with role: {role}")
    
    def perceive(self, input_data):
        """
        🎓 PERCEIVE Phase: Process and understand the input
        
        This is where the agent takes in information from its environment.
        In a more complex agent, this might include:
        - Parsing different data types
        - Context from memory
        - Sensor data
        - Previous conversation history
        
        Args:
            input_data: Raw input from the user or environment
            
        Returns:
            dict: Structured perception of the input
        """
        perception = {
            "user_input": input_data,
            "context": self.role,
            "timestamp": None  # You could add timestamp here
        }
        print(f"👁️ PERCEIVE: {perception}")
        return perception
    
    def plan(self, perception):
        """
        🎓 PLAN Phase: Decide what actions to take
        
        Based on what we perceived, create a plan of action.
        In simple agents, this might just be "respond to user".
        In complex agents, this could involve:
        - Multi-step planning
        - Tool selection
        - Strategy decisions
        
        Args:
            perception (dict): The structured perception from perceive()
            
        Returns:
            list: List of planned actions
        """
        plan = [{"action": "respond", "data": perception}]
        print(f"🧠 PLAN: {plan}")
        return plan
    
    def act(self, plan):
        """
        🎓 ACT Phase: Execute the planned actions
        
        This is where the agent actually does something with the LLM.
        The agent sends the request to OpenAI and gets a response.
        
        Args:
            plan (list): List of actions from plan()
            
        Returns:
            str: The result of the action (LLM response)
        """
        print("⚡ ACT: Sending request to OpenAI...")
        
        # Get the first (and only) action from our simple plan
        action = plan[0]
        user_input = action["data"]["user_input"]
        
        # Create messages for the chat completion
        messages = [
            {"role": "system", "content": f"You are a helpful {self.role}."},
            {"role": "user", "content": user_input}
        ]
        
        # Call OpenAI API
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        
        result = response.choices[0].message.content
        print(f"💬 ACT Result: {result[:100]}...")  # Show first 100 chars
        return result
    
    def reflect(self, result):
        """
        🎓 REFLECT Phase: Evaluate and learn from the results
        
        This is where the agent can:
        - Evaluate if the action was successful
        - Learn from the interaction
        - Store information for future use
        - Decide if additional actions are needed
        
        Args:
            result: The result from act()
            
        Returns:
            dict: Reflection summary
        """
        reflection = {
            "success": True,
            "output": result,
            "feedback": "Response generated successfully"
        }
        print(f"🔄 REFLECT: {reflection['feedback']}")
        return reflection
    
    def run(self, user_input):
        """
        🎓 Main execution loop - runs the full Perceive → Plan → Act → Reflect cycle
        
        This is the main method that ties everything together and runs
        the complete agent cycle.
        
        Args:
            user_input (str): The user's input/question
            
        Returns:
            str: The agent's response
        """
        print(f"\n🚀 Starting agent cycle for input: '{user_input}'")
        print("=" * 60)
        
        # Step 1: Perceive the input
        perception = self.perceive(user_input)
        
        # Step 2: Plan what to do
        plan = self.plan(perception)
        
        # Step 3: Act on the plan
        result = self.act(plan)
        
        # Step 4: Reflect on the results
        reflection = self.reflect(result)
        
        print("=" * 60)
        print("✅ Agent cycle completed!")
        
        return reflection["output"]

# Example usage and test
if __name__ == "__main__":
    print("🎓 SIMPLE AGENT TUTORIAL")
    print("This demonstrates the basic AI Agent pattern: Perceive → Plan → Act → Reflect")
    print("\n")
    
    # Create an agent
    agent = SimpleAgent(role="Python Programming Tutor")
    
    # Test the agent
    test_questions = [
        "What is a Python list?",
        "How do I create a function in Python?",
        "Explain the difference between a list and a tuple."
    ]
    
    for question in test_questions:
        print(f"\n{'='*80}")
        print(f"TEST QUESTION: {question}")
        print('='*80)
        
        try:
            response = agent.run(question)
            print(f"\n📝 FINAL ANSWER:\n{response}")
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Make sure you have set OPENAI_API_KEY in your .env file!")