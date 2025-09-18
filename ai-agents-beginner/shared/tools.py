"""
Tool System for AI Agents - Modular tools that agents can use
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
import time
from datetime import datetime

class BaseTool(ABC):
    """Base class for all agent tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute the tool with given arguments"""
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """Get JSON schema for this tool's parameters"""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.get_parameters()
            }
        }
    
    @abstractmethod
    def get_parameters(self) -> Dict[str, Any]:
        """Get parameters schema for this tool"""
        pass

class CalculatorTool(BaseTool):
    """Calculator tool for basic math operations"""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Perform basic math calculations"
        )
    
    def execute(self, expression: str) -> Dict[str, Any]:
        """Execute a math expression safely"""
        try:
            # Simple safety check
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                return {"error": "Invalid characters", "success": False}
            
            result = eval(expression)
            return {"expression": expression, "result": result, "success": True}
            
        except Exception as e:
            return {"expression": expression, "error": str(e), "success": False}
    
    def get_parameters(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression (e.g., '2 + 2')"
                }
            },
            "required": ["expression"]
        }

class TimeTool(BaseTool):
    """Tool for getting current time and date"""
    
    def __init__(self):
        super().__init__(
            name="get_time", 
            description="Get current date and time"
        )
    
    def execute(self, format_type: str = "datetime") -> Dict[str, Any]:
        """Get current time in various formats"""
        now = datetime.now()
        
        formats = {
            "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "timestamp": int(time.time())
        }
        
        if format_type not in formats:
            return {"error": "Invalid format", "success": False}
        
        return {
            "format_type": format_type,
            "value": formats[format_type],
            "success": True
        }
    
    def get_parameters(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "format_type": {
                    "type": "string",
                    "enum": ["datetime", "date", "time", "timestamp"],
                    "default": "datetime"
                }
            }
        }

class ToolRegistry:
    """Registry to manage and execute tools"""
    
    def __init__(self):
        self.tools: Dict[str, BaseTool] = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default tools"""
        self.register(CalculatorTool())
        self.register(TimeTool())
    
    def register(self, tool: BaseTool):
        """Register a new tool"""
        self.tools[tool.name] = tool
        return self
    
    def get_tool(self, name: str) -> Optional[BaseTool]:
        """Get tool by name"""
        return self.tools.get(name)
    
    def list_tools(self) -> List[str]:
        """List all registered tools"""
        return list(self.tools.keys())
    
    def execute_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """Execute a tool by name"""
        tool = self.get_tool(tool_name)
        if not tool:
            return {"error": f"Tool '{tool_name}' not found", "success": False}
        
        try:
            return tool.execute(**kwargs)
        except Exception as e:
            return {"error": str(e), "success": False}
    
    def get_all_schemas(self) -> List[Dict[str, Any]]:
        """Get schemas for all tools"""
        return [tool.get_schema() for tool in self.tools.values()]