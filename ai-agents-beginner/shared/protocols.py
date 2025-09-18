"""
Communication Protocols for Multi-Agent Systems
MCP (Message Communication Protocol) and A2A (Agent-to-Agent) patterns
"""

from enum import Enum
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import json

class MessageType(Enum):
    """Types of messages between agents"""
    REQUEST = "request"
    RESPONSE = "response" 
    NOTIFICATION = "notification"
    ERROR = "error"
    HANDSHAKE = "handshake"

class Priority(Enum):
    """Message priority levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

@dataclass
class AgentMessage:
    """Standard message format for agent communication"""
    id: str
    sender_id: str
    receiver_id: str
    message_type: MessageType
    priority: Priority
    content: Dict[str, Any]
    timestamp: str
    conversation_id: Optional[str] = None
    reply_to: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AgentMessage':
        """Create from dictionary"""
        return cls(
            id=data['id'],
            sender_id=data['sender_id'],
            receiver_id=data['receiver_id'],
            message_type=MessageType(data['message_type']),
            priority=Priority(data['priority']),
            content=data['content'],
            timestamp=data['timestamp'],
            conversation_id=data.get('conversation_id'),
            reply_to=data.get('reply_to'),
            metadata=data.get('metadata')
        )

class MessageProtocol:
    """Message Communication Protocol implementation"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.message_counter = 0
        self.conversations: Dict[str, List[AgentMessage]] = {}
    
    def create_message(
        self,
        receiver_id: str,
        content: Dict[str, Any],
        message_type: MessageType = MessageType.REQUEST,
        priority: Priority = Priority.MEDIUM,
        conversation_id: Optional[str] = None,
        reply_to: Optional[str] = None
    ) -> AgentMessage:
        """Create a new message"""
        
        self.message_counter += 1
        message_id = f"{self.agent_id}_{self.message_counter}_{int(datetime.now().timestamp())}"
        
        message = AgentMessage(
            id=message_id,
            sender_id=self.agent_id,
            receiver_id=receiver_id,
            message_type=message_type,
            priority=priority,
            content=content,
            timestamp=datetime.now().isoformat(),
            conversation_id=conversation_id,
            reply_to=reply_to
        )
        
        # Track conversation
        if conversation_id:
            if conversation_id not in self.conversations:
                self.conversations[conversation_id] = []
            self.conversations[conversation_id].append(message)
        
        return message
    
    def create_request(
        self,
        receiver_id: str,
        action: str,
        parameters: Dict[str, Any],
        conversation_id: Optional[str] = None
    ) -> AgentMessage:
        """Create a request message"""
        return self.create_message(
            receiver_id=receiver_id,
            content={"action": action, "parameters": parameters},
            message_type=MessageType.REQUEST,
            conversation_id=conversation_id
        )
    
    def create_response(
        self,
        receiver_id: str,
        result: Dict[str, Any],
        reply_to: str,
        success: bool = True,
        conversation_id: Optional[str] = None
    ) -> AgentMessage:
        """Create a response message"""
        return self.create_message(
            receiver_id=receiver_id,
            content={"result": result, "success": success},
            message_type=MessageType.RESPONSE,
            reply_to=reply_to,
            conversation_id=conversation_id
        )
    
    def create_error(
        self,
        receiver_id: str,
        error: str,
        reply_to: Optional[str] = None,
        conversation_id: Optional[str] = None
    ) -> AgentMessage:
        """Create an error message"""
        return self.create_message(
            receiver_id=receiver_id,
            content={"error": error},
            message_type=MessageType.ERROR,
            priority=Priority.HIGH,
            reply_to=reply_to,
            conversation_id=conversation_id
        )
    
    def get_conversation(self, conversation_id: str) -> List[AgentMessage]:
        """Get all messages in a conversation"""
        return self.conversations.get(conversation_id, [])

class AgentCoordinator:
    """Coordinates communication between multiple agents"""
    
    def __init__(self):
        self.agents: Dict[str, Any] = {}
        self.message_queue: List[AgentMessage] = []
        self.message_history: List[AgentMessage] = []
    
    def register_agent(self, agent_id: str, agent_instance: Any):
        """Register an agent for coordination"""
        self.agents[agent_id] = agent_instance
    
    def send_message(self, message: AgentMessage) -> bool:
        """Send message to target agent"""
        if message.receiver_id not in self.agents:
            print(f"Agent {message.receiver_id} not found")
            return False
        
        self.message_queue.append(message)
        self.message_history.append(message)
        
        # Simulate message delivery
        target_agent = self.agents[message.receiver_id]
        if hasattr(target_agent, 'receive_message'):
            target_agent.receive_message(message)
        
        return True
    
    def broadcast_message(
        self,
        sender_id: str,
        content: Dict[str, Any],
        exclude_agents: Optional[List[str]] = None
    ) -> List[AgentMessage]:
        """Broadcast message to all agents"""
        exclude_agents = exclude_agents or []
        messages = []
        
        protocol = MessageProtocol(sender_id)
        
        for agent_id in self.agents:
            if agent_id != sender_id and agent_id not in exclude_agents:
                message = protocol.create_message(
                    receiver_id=agent_id,
                    content=content,
                    message_type=MessageType.NOTIFICATION
                )
                if self.send_message(message):
                    messages.append(message)
        
        return messages
    
    def get_agent_stats(self) -> Dict[str, Any]:
        """Get communication statistics"""
        total_messages = len(self.message_history)
        
        by_type = {}
        by_agent = {}
        
        for msg in self.message_history:
            # By type
            msg_type = msg.message_type.value
            by_type[msg_type] = by_type.get(msg_type, 0) + 1
            
            # By agent
            sender = msg.sender_id
            by_agent[sender] = by_agent.get(sender, 0) + 1
        
        return {
            "total_messages": total_messages,
            "registered_agents": len(self.agents),
            "messages_by_type": by_type,
            "messages_by_agent": by_agent,
            "queue_size": len(self.message_queue)
        }