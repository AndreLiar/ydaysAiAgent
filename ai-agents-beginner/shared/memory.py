"""
Memory Systems for AI Agents - Short-term and long-term memory
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

class BaseMemory(ABC):
    """Base class for memory systems"""
    
    @abstractmethod
    def add(self, key: str, value: Any, metadata: Optional[Dict] = None) -> None:
        """Add item to memory"""
        pass
    
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """Get item from memory"""
        pass
    
    @abstractmethod
    def search(self, query: str, limit: int = 10) -> List[Tuple[str, Any]]:
        """Search memory"""
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clear all memory"""
        pass

class SimpleMemory(BaseMemory):
    """Simple in-memory storage with LRU eviction"""
    
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.data: Dict[str, Any] = {}
        self.metadata: Dict[str, Dict] = {}
        self.access_order: List[str] = []
    
    def add(self, key: str, value: Any, metadata: Optional[Dict] = None) -> None:
        """Add item with optional metadata"""
        if key in self.data:
            self.access_order.remove(key)
        
        self.data[key] = value
        self.metadata[key] = metadata or {}
        self.metadata[key]['timestamp'] = datetime.now().isoformat()
        self.access_order.append(key)
        
        # LRU eviction
        while len(self.data) > self.max_size:
            oldest = self.access_order.pop(0)
            del self.data[oldest]
            del self.metadata[oldest]
    
    def get(self, key: str) -> Optional[Any]:
        """Get item and update access"""
        if key in self.data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.data[key]
        return None
    
    def search(self, query: str, limit: int = 10) -> List[Tuple[str, Any]]:
        """Simple text search"""
        query_lower = query.lower()
        results = []
        
        for key, value in self.data.items():
            if query_lower in key.lower():
                results.append((key, value))
            elif isinstance(value, str) and query_lower in value.lower():
                results.append((key, value))
        
        return results[:limit]
    
    def clear(self) -> None:
        """Clear all memory"""
        self.data.clear()
        self.metadata.clear()
        self.access_order.clear()
    
    def size(self) -> int:
        """Get current size"""
        return len(self.data)

class VectorMemory(BaseMemory):
    """Vector-based memory for semantic search (simplified)"""
    
    def __init__(self, persist_path: Optional[str] = None):
        self.persist_path = persist_path or "memory.json"
        self.data: Dict[str, Any] = {}
        self.metadata: Dict[str, Dict] = {}
        self._load_from_disk()
    
    def add(self, key: str, value: Any, metadata: Optional[Dict] = None) -> None:
        """Add item to persistent memory"""
        self.data[key] = value
        self.metadata[key] = {
            **(metadata or {}),
            'timestamp': datetime.now().isoformat()
        }
        self._save_to_disk()
    
    def get(self, key: str) -> Optional[Any]:
        """Get item from memory"""
        return self.data.get(key)
    
    def search(self, query: str, limit: int = 10) -> List[Tuple[str, Any]]:
        """Search with basic text matching"""
        query_lower = query.lower()
        results = []
        
        for key, value in self.data.items():
            score = 0
            if query_lower in key.lower():
                score += 1
            if isinstance(value, str) and query_lower in value.lower():
                score += 1
            
            if score > 0:
                results.append((key, value))
        
        return results[:limit]
    
    def clear(self) -> None:
        """Clear all memory"""
        self.data.clear()
        self.metadata.clear()
        self._save_to_disk()
    
    def _save_to_disk(self):
        """Save to disk"""
        import json
        try:
            with open(self.persist_path, 'w') as f:
                json.dump({
                    'data': self.data,
                    'metadata': self.metadata
                }, f, indent=2)
        except Exception:
            pass  # Silent fail for demo
    
    def _load_from_disk(self):
        """Load from disk"""
        import json
        try:
            with open(self.persist_path, 'r') as f:
                saved = json.load(f)
                self.data = saved.get('data', {})
                self.metadata = saved.get('metadata', {})
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Start fresh