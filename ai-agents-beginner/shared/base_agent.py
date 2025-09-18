"""
Base Agent Implementation - Universal Agentic Loop
Perception → Plan → Act → Reflect pattern for all AI agents
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

class BaseAgent(ABC):
    """
    Abstract base class for all AI agents implementing the universal agentic loop
    """
    
    def __init__(self, role: str = "Assistant"):
        self.role = role
        self.execution_history = []
        self.stats = {
            "total_runs": 0,
            "successful_runs": 0,
            "average_quality_score": 0.0
        }
    
    @abstractmethod
    def perceive(self, input_data: Any, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        PERCEPTION: Analyze input and understand the current situation
        Args:
            input_data: The input to process (text, data, etc.)
            context: Optional context information
        Returns:
            Dict containing perception results
        """
        pass
    
    @abstractmethod  
    def plan(self, perception: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        PLAN: Create a plan of action based on perception
        Args:
            perception: Results from the perceive step
        Returns:
            List of planned actions to execute
        """
        pass
    
    @abstractmethod
    def act(self, plan: List[Dict[str, Any]], perception: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        ACT: Execute the planned actions
        Args:
            plan: List of actions to execute
            perception: Original perception for context
        Returns:
            List of execution results
        """
        pass
    
    @abstractmethod
    def reflect(self, results: List[Dict[str, Any]], expected_outcome: Optional[str] = None) -> Dict[str, Any]:
        """
        REFLECT: Evaluate results and learn for improvement
        Args:
            results: Results from the act step
            expected_outcome: Optional expected outcome for comparison
        Returns:
            Dict containing reflection and quality metrics
        """
        pass
    
    def run_loop(self, input_data: Any, expected_outcome: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute the complete agentic loop: Perceive → Plan → Act → Reflect
        Args:
            input_data: Input to process
            expected_outcome: Optional expected outcome
        Returns:
            Dict containing complete execution results
        """
        
        print(f"🤖 Starting agentic loop - {self.role}")
        print("=" * 50)
        
        try:
            # 1. PERCEIVE
            perception = self.perceive(input_data)
            
            # 2. PLAN  
            plan = self.plan(perception)
            
            # 3. ACT
            results = self.act(plan, perception)
            
            # 4. REFLECT
            reflection = self.reflect(results, expected_outcome)
            
            # Store execution
            execution = {
                "timestamp": datetime.now().isoformat(),
                "input": input_data,
                "perception": perception,
                "plan": plan, 
                "results": results,
                "reflection": reflection,
                "success": reflection.get("quality_score", 0) >= 3.0
            }
            
            self.execution_history.append(execution)
            self._update_stats(reflection)
            
            print("=" * 50)
            print(f"✅ Loop completed - Quality: {reflection.get('quality_score', 0)}/5")
            
            return execution
            
        except Exception as e:
            print(f"❌ Error in agentic loop: {e}")
            error_execution = {
                "timestamp": datetime.now().isoformat(),
                "input": input_data,
                "error": str(e),
                "success": False
            }
            self.execution_history.append(error_execution)
            return error_execution
    
    def _update_stats(self, reflection: Dict[str, Any]):
        """Update performance statistics"""
        self.stats["total_runs"] += 1
        
        quality_score = reflection.get("quality_score", 0)
        if quality_score >= 3.0:
            self.stats["successful_runs"] += 1
        
        # Update average quality score
        current_avg = self.stats["average_quality_score"]
        n = self.stats["total_runs"]
        self.stats["average_quality_score"] = (current_avg * (n-1) + quality_score) / n
    
    def get_stats(self) -> Dict[str, Any]:
        """Get performance statistics"""
        return self.stats.copy()
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """Get execution history"""
        return self.execution_history.copy()