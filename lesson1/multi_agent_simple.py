from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv()

class SimpleMultiAgentSystem:
    def __init__(self):
        """
        🎓 TUTORIAL: Multi-Agent System (Simplified)
        
        This demonstrates how multiple AI agents can work together as a team.
        Key concepts:
        - SPECIALIZATION: Each agent has a specific role and expertise
        - COLLABORATION: Agents work together and pass information between them
        - WORKFLOW: Tasks flow from one agent to another in a coordinated way
        
        Our team:
        - 🔍 Researcher: Analyzes topics and provides insights
        - ✍️ Writer: Creates content based on research
        """
        print("🎯 Initializing Multi-Agent System...")
        
        # Create specialized agents without external tools
        self._create_agents()
        
        print("✅ Multi-Agent System ready!")
        print(f"👥 Team: {len(self.agents)} agents")
        
    def _create_agents(self):
        """Create specialized agents with different roles"""
        
        # 🔍 RESEARCHER AGENT
        self.researcher = Agent(
            role='Senior Research Analyst',
            goal='Analyze topics and provide comprehensive insights',
            backstory="""You are a seasoned research analyst with deep knowledge across 
            many fields. You excel at breaking down complex topics, identifying key themes, 
            and providing structured analysis. You draw from your extensive knowledge to 
            provide valuable insights.""",
            
            verbose=True,
            allow_delegation=False
        )
        
        # ✍️ WRITER AGENT  
        self.writer = Agent(
            role='Tech Content Strategist',
            goal='Craft compelling and informative content based on research',
            backstory="""You are a skilled content strategist with years of experience 
            in creating engaging technical content. You excel at taking complex research 
            and turning it into accessible, well-structured articles that inform and 
            engage readers. You have a talent for clear explanations and engaging writing.""",
            
            verbose=True,
            allow_delegation=False
        )
        
        self.agents = [self.researcher, self.writer]
        print("🔍 Created Researcher Agent")
        print("✍️ Created Writer Agent")
    
    def create_content_workflow(self, topic):
        """Create a research and writing workflow"""
        print(f"\n📋 Creating workflow for topic: '{topic}'")
        
        # 🔍 RESEARCH TASK
        research_task = Task(
            description=f"""Analyze the topic: {topic}
            
            Please provide a comprehensive analysis including:
            1. Key concepts and definitions
            2. Main benefits and advantages
            3. Common use cases or applications
            4. Important considerations or challenges
            5. Current trends or developments
            
            Use your knowledge to provide detailed insights about this topic.
            """,
            expected_output="A detailed research analysis with key findings, benefits, use cases, and trends",
            agent=self.researcher
        )
        
        # ✍️ WRITING TASK  
        write_task = Task(
            description=f"""Create an informative and engaging article about: {topic}
            
            Based on the research analysis provided, write a well-structured article that:
            - Has an engaging introduction that hooks the reader
            - Clearly explains the key concepts
            - Highlights the main benefits and applications
            - Discusses important considerations
            - Includes practical insights
            - Ends with a strong conclusion
            
            Make the content accessible to a general audience while maintaining depth.
            """,
            expected_output="A well-written, engaging article that educates readers about the topic",
            agent=self.writer,
            context=[research_task]  # This task depends on the research task
        )
        
        # 🎯 CREATE THE CREW
        crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[research_task, write_task],
            verbose=True
        )
        
        print("✅ Workflow created!")
        print("📊 Execution order: Research Analysis → Content Writing")
        return crew
    
    def run_workflow(self, topic):
        """Execute the multi-agent workflow"""
        print(f"\n🚀 Starting multi-agent workflow for: '{topic}'")
        print("=" * 80)
        
        try:
            crew = self.create_content_workflow(topic)
            result = crew.kickoff()
            
            print("=" * 80)
            print("✅ Multi-agent workflow completed!")
            return result
            
        except Exception as e:
            print(f"❌ Error in workflow: {e}")
            return f"Workflow failed: {e}"
    
    def explain_collaboration(self):
        """Explain how the agents collaborate"""
        print("\n🎓 HOW AGENTS COLLABORATE:")
        print("=" * 60)
        print("1. 🔍 Researcher receives the topic")
        print("2. 🔍 Researcher analyzes and provides detailed insights")
        print("3. ✍️ Writer receives the research findings")
        print("4. ✍️ Writer crafts an article based on the research")
        print("5. 📄 Final article is delivered to user")
        print("\n🎯 BENEFITS:")
        print("   ✅ Specialization: Each agent focuses on their expertise")
        print("   ✅ Quality: Research-backed content creation")
        print("   ✅ Structure: Clear workflow and handoffs")
        print("   ✅ Consistency: Systematic approach to content creation")

# Demo script
if __name__ == "__main__":
    print("🎓 MULTI-AGENT SYSTEM TUTORIAL")
    print("This demonstrates AI agents working together as a team!")
    print("\n")
    
    # Create the system
    system = SimpleMultiAgentSystem()
    
    # Explain how it works
    system.explain_collaboration()
    
    # Example topics
    topics = [
        "Machine Learning for Beginners",
        "Benefits of Cloud Computing"
    ]
    
    for i, topic in enumerate(topics, 1):
        print(f"\n{'='*100}")
        print(f"EXAMPLE {i}: Creating content about '{topic}'")
        print('='*100)
        
        result = system.run_workflow(topic)
        
        print(f"\n📝 FINAL CONTENT:")
        print("-" * 70)
        print(result)
        print("-" * 70)
        
        if i < len(topics):
            print("\n⏳ Moving to next example...\n")
    
    print(f"\n🎉 Multi-Agent System tutorial completed!")
    print("🎓 You've learned how AI agents can collaborate to create amazing results!")