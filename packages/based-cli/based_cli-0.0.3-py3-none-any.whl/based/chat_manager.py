from typing import Dict, List, Optional
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_mistralai import ChatMistralAI
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from rich.console import Console
import json
import os
from datetime import datetime
from pathlib import Path

console = Console()

# Load available models
AVAILABLE_MODELS = {
    "openai": {
        "gpt-4": "gpt-4",
        "gpt-4-turbo": "gpt-4-0125-preview",
        "gpt-3.5-turbo": "gpt-3.5-turbo"
    },
    "anthropic": {
        "claude-3-sonnet": "claude-3-sonnet-20240229",
        "claude-3-opus": "claude-3-opus-20240229",
        "claude-2.1": "claude-2.1"
    },
    "mistral": {
        "mistral-large": "mistral-large-latest",
        "mistral-medium": "mistral-medium-latest",
        "mistral-small": "mistral-small-latest",
        "mistral-codestraal": "mistral-codestraal-latest"
    },
    "groq": {
        "llama2-70b": "llama2-70b-4096",
        "mixtral-8x7b": "mixtral-8x7b-32768",
        "gemma-7b": "gemma-7b-it"
    },
    "huggingface": {
        "coderqween": "bigcode/coderqween",
        "starcoder2": "bigcode/starcoder2-15b",
        "codellama": "codellama/CodeLlama-34b-Instruct-hf"
    }
}

class ChatManager:
    def __init__(self):
        self.chat_dir = os.path.expanduser("~/.based/chats")
        self.ensure_chat_dir()
        self.messages: List[Dict] = []
        self.chat_id: Optional[str] = None
        self.model = None
        self.load_prompts()
        
    def ensure_chat_dir(self):
        """Create chat directory if it doesn't exist"""
        if not os.path.exists(self.chat_dir):
            os.makedirs(self.chat_dir)
            
    def load_prompts(self):
        """Load system prompts from JSON file"""
        prompts_file = Path(__file__).parent / "prompts.json"
        try:
            with open(prompts_file) as f:
                self.prompts = json.load(f)
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load prompts.json: {str(e)}[/yellow]")
            self.prompts = {
                "default": {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                }
            }
            
    def initialize_model(self, provider: str, api_key: str, model_name: str, prompt_type: str = "default"):
        """Initialize the language model"""
        if provider == "openai":
            self.model = ChatOpenAI(
                model_name=model_name,
                openai_api_key=api_key,
                temperature=0.7
            )
        elif provider == "anthropic":
            self.model = ChatAnthropic(
                model=model_name,
                anthropic_api_key=api_key,
                temperature=0.7
            )
        elif provider == "mistral":
            self.model = ChatMistralAI(
                model=model_name,
                mistral_api_key=api_key,
                temperature=0.7
            )
        elif provider == "groq":
            self.model = ChatGroq(
                model=model_name,
                groq_api_key=api_key,
                temperature=0.7
            )
        elif provider == "huggingface":
            self.model = HuggingFaceEndpoint(
                endpoint_url=f"https://api-inference.huggingface.co/models/{model_name}",
                huggingfacehub_api_token=api_key,
                task="text-generation",
                model_kwargs={"temperature": 0.7}
            )
            
        # Get system prompt
        system_prompt = self.prompts.get(prompt_type, self.prompts["default"])
        
        # Create a chain with system message
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt["content"]),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
        
        self.chain = prompt | self.model | StrOutputParser()
            
    def get_response(self, user_input: str) -> str:
        """Get response from the model"""
        try:
            # Convert stored messages to LangChain format
            history = []
            for msg in self.messages:
                if msg["role"] == "user":
                    history.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "assistant":
                    history.append(AIMessage(content=msg["content"]))
                elif msg["role"] == "system":
                    history.append(SystemMessage(content=msg["content"]))
            
            # Get response
            response = self.chain.invoke({
                "history": history,
                "input": user_input
            })
            
            return response
            
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")
            return "Sorry, there was an error generating the response."
            
    def add_message(self, role: str, content: str):
        """Add a message to the conversation"""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
        if self.chat_id:
            self.save_chat()
            
    def save_chat(self):
        """Save chat to file"""
        if not self.chat_id:
            return
            
        chat_file = os.path.join(self.chat_dir, f"{self.chat_id}.json")
        with open(chat_file, "w") as f:
            json.dump({
                "updated_at": datetime.now().isoformat(),
                "messages": self.messages
            }, f, indent=2)
            
    def load_chat(self, chat_id: str) -> bool:
        """Load chat from file"""
        chat_file = os.path.join(self.chat_dir, f"{chat_id}.json")
        if os.path.exists(chat_file):
            with open(chat_file) as f:
                data = json.load(f)
                self.messages = data["messages"]
                self.chat_id = chat_id
                return True
        return False
        
    def list_chats(self) -> List[Dict]:
        """List all saved chats"""
        chats = []
        for file in os.listdir(self.chat_dir):
            if file.endswith(".json"):
                chat_id = file[:-5]  # Remove .json extension
                chat_file = os.path.join(self.chat_dir, file)
                with open(chat_file) as f:
                    data = json.load(f)
                    chats.append({
                        "id": chat_id,
                        "updated_at": data["updated_at"],
                        "messages": data["messages"]
                    })
        return sorted(chats, key=lambda x: x["updated_at"], reverse=True)
        
    def delete_chat(self, chat_id: str):
        """Delete a chat"""
        chat_file = os.path.join(self.chat_dir, f"{chat_id}.json")
        if os.path.exists(chat_file):
            os.remove(chat_file)
            
    def clear_chats(self):
        """Delete all chats"""
        for file in os.listdir(self.chat_dir):
            if file.endswith(".json"):
                os.remove(os.path.join(self.chat_dir, file))
                
    @staticmethod
    def get_available_models(provider: str = None) -> Dict:
        """Get available models for a provider or all providers"""
        if provider:
            return AVAILABLE_MODELS.get(provider, {})
        return AVAILABLE_MODELS
        
    def get_available_prompts(self) -> List[str]:
        """Get list of available prompt types"""
        return list(self.prompts.keys()) 