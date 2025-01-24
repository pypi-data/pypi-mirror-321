import os
import json
from typing import Dict, Optional
from rich.console import Console
from rich.table import Table
import questionary
from questionary import Style

from .chat_manager import AVAILABLE_MODELS, ChatManager

console = Console()

# Custom style for questionary
custom_style = Style([
    ('qmark', 'fg:#673ab7 bold'),     # token in front of the question
    ('question', 'bold'),             # question text
    ('answer', 'fg:#f44336 bold'),    # submitted answer text
    ('pointer', 'fg:#673ab7 bold'),   # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#673ab7 bold'),  # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#cc5454'),       # style for a selected item of a checkbox
    ('separator', 'fg:#673ab7'),      # separator in lists
    ('instruction', 'fg:#f44336')    # user instructions for select, rawselect, checkbox
])

class ConfigManager:
    def __init__(self):
        self.config_dir = os.path.expanduser("~/.based")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.ensure_config_dir()
        self.config = self.load_config()
        self.chat_manager = ChatManager()
        
    def ensure_config_dir(self):
        """Create config directory if it doesn't exist"""
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
            
    def load_config(self) -> Dict:
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            with open(self.config_file) as f:
                return json.load(f)
        return {
            "providers": {
                "openai": {
                    "api_key": None,
                    "model": "gpt-4-turbo",
                    "prompt_type": "default"
                },
                "anthropic": {
                    "api_key": None,
                    "model": "claude-3-sonnet",
                    "prompt_type": "default"
                },
                "mistral": {
                    "api_key": None,
                    "model": "mistral-large",
                    "prompt_type": "default"
                },
                "groq": {
                    "api_key": None,
                    "model": "llama2-70b",
                    "prompt_type": "default"
                },
                "huggingface": {
                    "api_key": None,
                    "model": "coderqween",
                    "prompt_type": "default"
                }
            },
            "active_provider": None
        }
        
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=2)
            
    def get_active_provider(self) -> Optional[Dict]:
        """Get active provider configuration"""
        if not self.config["active_provider"]:
            return None
        return self.config["providers"][self.config["active_provider"]]
        
    def setup_provider(self, provider: str):
        """Setup a provider configuration"""
        if provider not in self.config["providers"]:
            console.print(f"[red]Invalid provider: {provider}[/red]")
            return
            
        console.print(f"\n[bold]Setting up {provider.upper()}[/bold]")
        
        # Get API key
        api_key = questionary.password(
            f"Enter your {provider} API key",
            style=custom_style
        ).ask()
        
        if not api_key:
            console.print("[red]API key is required[/red]")
            return
            
        # Select model
        available_models = AVAILABLE_MODELS[provider]
        model = questionary.select(
            "Choose a model:",
            choices=list(available_models.keys()),
            style=custom_style
        ).ask()
        
        # Select prompt type
        prompt_type = questionary.select(
            "Choose a system prompt type:",
            choices=self.chat_manager.get_available_prompts(),
            style=custom_style
        ).ask()
        
        # Update config
        self.config["providers"][provider]["api_key"] = api_key
        self.config["providers"][provider]["model"] = available_models[model]
        self.config["providers"][provider]["prompt_type"] = prompt_type
        self.config["active_provider"] = provider
        
        self.save_config()
        
    def edit_config(self):
        """Edit configuration interactively"""
        # Show current config
        self.show_config()
        
        # Select action
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Change active provider",
                "Configure provider",
                "Change system prompt",
                "Show configuration",
                "Back"
            ],
            style=custom_style
        ).ask()
        
        if action == "Change active provider":
            provider = questionary.select(
                "Choose provider:",
                choices=list(self.config["providers"].keys()),
                style=custom_style
            ).ask()
            
            if self.config["providers"][provider]["api_key"]:
                self.config["active_provider"] = provider
                self.save_config()
            else:
                console.print(f"[yellow]Provider {provider} is not configured yet[/yellow]")
                self.setup_provider(provider)
                
        elif action == "Configure provider":
            provider = questionary.select(
                "Choose provider to configure:",
                choices=list(self.config["providers"].keys()),
                style=custom_style
            ).ask()
            
            self.setup_provider(provider)
            
        elif action == "Change system prompt":
            if not self.config["active_provider"]:
                console.print("[red]No active provider selected[/red]")
                return
                
            prompt_type = questionary.select(
                "Choose a system prompt type:",
                choices=self.chat_manager.get_available_prompts(),
                style=custom_style
            ).ask()
            
            self.config["providers"][self.config["active_provider"]]["prompt_type"] = prompt_type
            self.save_config()
            
        elif action == "Show configuration":
            self.show_config()
            
    def show_config(self):
        """Display current configuration"""
        console.print("\n[bold]Current Configuration:[/bold]")
        
        table = Table(show_header=True)
        table.add_column("Provider")
        table.add_column("Status")
        table.add_column("Model")
        table.add_column("Prompt Type")
        
        for provider, config in self.config["providers"].items():
            status = "[green]Configured[/green]" if config["api_key"] else "[red]Not Configured[/red]"
            active = " [yellow](Active)[/yellow]" if provider == self.config["active_provider"] else ""
            table.add_row(
                provider,
                status + active,
                config["model"] if config["api_key"] else "-",
                config["prompt_type"]
            )
            
        console.print(table)
        
    def is_configured(self) -> bool:
        """Check if any provider is configured and active"""
        return (
            self.config["active_provider"] is not None
            and self.config["providers"][self.config["active_provider"]]["api_key"] is not None
        ) 