import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class CacheManager:
    def __init__(self):
        self.cache_dir = os.path.expanduser("~/.based/cache")
        self.ensure_cache_dir()
        
    def ensure_cache_dir(self):
        """Create cache directory if it doesn't exist"""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            
    def save_chat_history(self, chat_id: str, messages: List[Dict]):
        """Save chat history to cache"""
        cache_file = os.path.join(self.cache_dir, f"chat_{chat_id}.json")
        with open(cache_file, "w") as f:
            json.dump({
                "updated_at": datetime.now().isoformat(),
                "messages": messages
            }, f)
            
    def load_chat_history(self, chat_id: str) -> Optional[List[Dict]]:
        """Load chat history from cache"""
        cache_file = os.path.join(self.cache_dir, f"chat_{chat_id}.json")
        if os.path.exists(cache_file):
            with open(cache_file) as f:
                data = json.load(f)
                return data["messages"]
        return None
        
    def list_chats(self) -> List[Dict]:
        """List all cached chats"""
        chats = []
        for file in os.listdir(self.cache_dir):
            if file.startswith("chat_") and file.endswith(".json"):
                chat_id = file[5:-5]  # Remove 'chat_' prefix and '.json' suffix
                cache_file = os.path.join(self.cache_dir, file)
                with open(cache_file) as f:
                    data = json.load(f)
                    chats.append({
                        "id": chat_id,
                        "updated_at": data["updated_at"],
                        "messages": data["messages"]
                    })
        return sorted(chats, key=lambda x: x["updated_at"], reverse=True)
        
    def delete_chat(self, chat_id: str):
        """Delete a chat from cache"""
        cache_file = os.path.join(self.cache_dir, f"chat_{chat_id}.json")
        if os.path.exists(cache_file):
            os.remove(cache_file)
            
    def clear_cache(self):
        """Clear all cached data"""
        for file in os.listdir(self.cache_dir):
            if file.endswith(".json"):
                os.remove(os.path.join(self.cache_dir, file)) 