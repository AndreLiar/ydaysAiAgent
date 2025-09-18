from crewai import Agent, Task, Crew
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class MultiAgentSystem:
    def __init__(self):
        """
        🎓 TUTORIAL: Multi-Agent System
        
        This demonstrates how multiple AI agents can work together as a team.
        Key concepts:
        - SPECIALIZATION: Each agent has a specific role and expertise
        - COLLABORATION: Agents work together and pass information between them
        - WORKFLOW: Tasks flow from one agent to another in a coordinated way
        
        Our team:
        - 🔍 Researcher: Finds and gathers information
        - ✍️ Writer: Creates content based on research
        """
        print("🎯 Initializing Multi-Agent System...")
        
        # Initialize tools
        self.search_tool = DuckDuckGoSearchRun()
        
        # Create specialized agents
        self._create_agents()
        
        print("✅ Multi-Agent System ready!")
        print(f"👥 Team: {len(self.agents)} agents")
        
    def _create_agents(self):
        """Create specialized agents with different roles"""
        
        # 🔍 RESEARCHER AGENT
        self.researcher = Agent(
            role='Senior Research Analyst',
            goal='Uncover cutting-edge developments and provide comprehensive research',
            backstory="""You are a seasoned research analyst with expertise in finding 
            and analyzing information. You have a keen eye for identifying credible sources 
            and extracting key insights. You're methodical and thorough in your research.""",
            
            verbose=True,
            allow_delegation=False,
            tools=[self.search_tool]
        )
        
        # ✍️ WRITER AGENT  
        self.writer = Agent(
            role='Tech Content Strategist',
            goal='Craft compelling and informative content based on research',
            backstory="""You are a skilled content strategist with years of experience 
            in creating engaging technical content. You excel at taking complex research 
            and turning it into accessible, well-structured articles that inform and 
            engage readers.""",
            
            verbose=True,
            allow_delegation=False,
            tools=[]  # Writer doesn't need search tools
        )
        
        self.agents = [self.researcher, self.writer]
        print("🔍 Created Researcher Agent")
        print("✍️ Created Writer Agent")
    
    def create_simple_workflow(self, topic):
        """Create a simple research and writing workflow"""
        print(f"\n📋 Creating workflow for topic: '{topic}'")
        
        # 🔍 RESEARCH TASK
        research_task = Task(
            description=f"""Research the topic: {topic}
            
            Find key information, trends, and insights about this topic.
            Provide a summary of your findings.
            """,
            expected_output="A research summary with key findings about the topic",
            agent=self.researcher
        )
        
        # ✍️ WRITING TASK  
        write_task = Task(
            description=f"""Create an informative article about: {topic}
            
            Based on the research provided, write a well-structured article that:
            - Has a clear introduction
            - Covers the main points
            - Includes key insights
            - Has a conclusion
            """,
            expected_output="A well-written article based on the research",
            agent=self.writer,
            context=[research_task]  # This task uses research from previous task
        )
        
        # 🎯 CREATE THE CREW
        crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[research_task, write_task],
            verbose=2
        )
        
        print("✅ Workflow created!")
        return crew
    
    def run_workflow(self, topic):
        """Execute the multi-agent workflow"""
        print(f"\n🚀 Starting multi-agent workflow for: '{topic}'")
        print("=" * 80)
        
        try:
            crew = self.create_simple_workflow(topic)
            result = crew.kickoff()
            
            print("=" * 80)
            print("✅ Multi-agent workflow completed!")
            return result
            
        except Exception as e:
            print(f"❌ Error in workflow: {e}")
            return f"Workflow failed: {e}"

# Demo script
if __name__ == "__main__":
    print("🎓 MULTI-AGENT SYSTEM DEMO")
    print("=" * 50)
    
    # Create the system
    system = MultiAgentSystem()
    
    # Run a simple example
    print("\n" + "="*80)
    print("EXAMPLE: Creating content about 'Python programming benefits'")
    print("="*80)
    
    result = system.run_workflow("Python programming benefits")
    
    print(f"\n📝 FINAL RESULT:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    
    print(f"\n🎉 Multi-Agent System demo completed!")
    print("🎓 Key Learning: Multiple agents can collaborate to create better results!")