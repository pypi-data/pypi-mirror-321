import os
import typer
from rich.console import Console
from rich.markdown import Markdown
import questionary
from questionary import Style
from typing import Optional
import uuid

from .chat_manager import ChatManager
from .config import ConfigManager, custom_style

# Initialize components
app = typer.Typer(name="based", help="Your AI assistant in the terminal")
console = Console()
config_manager = ConfigManager()
chat_manager = ChatManager()

def check_login(func):
    """Decorator to check if user is logged in"""
    def wrapper(*args, **kwargs):
        if not config_manager.is_configured():
            console.print("[red]Please login first using 'based login'[/red]")
            raise typer.Exit()
        return func(*args, **kwargs)
    return wrapper

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Based CLI - Your AI assistant in the terminal"""
    if ctx.invoked_subcommand is None:
        # If no subcommand is provided, start chat
        chat()

@app.command()
def login():
    """Configure AI provider and login"""
    console.print("[bold]Welcome to Based CLI![/bold]")
    
    provider = questionary.select(
        "Choose your AI provider:",
        choices=["openai", "anthropic", "mistral", "groq", "huggingface"],
        style=custom_style
    ).ask()
    
    config_manager.setup_provider(provider)
    
    # Initialize the model
    provider_config = config_manager.get_active_provider()
    chat_manager.initialize_model(
        provider=provider,
        api_key=provider_config["api_key"],
        model_name=provider_config["model"],
        prompt_type=provider_config["prompt_type"]
    )
    
    console.print("\n[green]Login successful! Type 'based' to start chatting.[/green]")

@app.command()
def config():
    """Edit configuration"""
    config_manager.edit_config()
    
    # Reinitialize the model with new config
    provider_config = config_manager.get_active_provider()
    if provider_config:
        chat_manager.initialize_model(
            provider=config_manager.config["active_provider"],
            api_key=provider_config["api_key"],
            model_name=provider_config["model"],
            prompt_type=provider_config["prompt_type"]
        )

@app.command(hidden=True)
def chat(chat_id: Optional[str] = None):
    """Start or continue a chat session with the AI assistant"""
    if not config_manager.is_configured():
        console.print("[red]Please login first using 'based login'[/red]")
        raise typer.Exit()
        
    # Initialize model if not already initialized
    if not chat_manager.model:
        provider_config = config_manager.get_active_provider()
        chat_manager.initialize_model(
            provider=config_manager.config["active_provider"],
            api_key=provider_config["api_key"],
            model_name=provider_config["model"],
            prompt_type=provider_config["prompt_type"]
        )
        
    if chat_id:
        if not chat_manager.load_chat(chat_id):
            console.print(f"[red]Chat {chat_id} not found[/red]")
            return
        console.print(f"[green]Loaded chat {chat_id}[/green]")
    else:
        chat_manager.chat_id = str(uuid.uuid4())
        console.print(f"[green]Started new chat {chat_manager.chat_id}[/green]")
    
    console.print("\n[bold green]Chat session started (type 'exit' to quit, 'help' for commands)[/bold green]")
    
    while True:
        try:
            # Get user input
            user_input = questionary.text(
                "\nYou:",
                style=custom_style
            ).ask()
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit', ':q', ':quit', ':exit']:
                console.print("\nAI: Goodbye! Have a great day!")
                break
                
            # Check for help command
            if user_input.lower() in ['help', ':help', '?']:
                console.print("\n[bold]Available commands:[/bold]")
                console.print("exit - End the chat session")
                console.print("help - Show this help message")
                console.print("clear - Clear the screen")
                console.print("save - Save current chat")
                continue
                
            # Get response from AI
            response = chat_manager.get_response(user_input)
            
            # Print response
            console.print(f"\nAI: {response}")
            
        except KeyboardInterrupt:
            console.print("\nChat session ended by user")
            break
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")
            break

@app.command()
@check_login
def list():
    """List all saved chats"""
    chats = chat_manager.list_chats()
    if not chats:
        console.print("[yellow]No saved chats found[/yellow]")
        return
        
    console.print("\n[bold]Saved Chats:[/bold]")
    for chat in chats:
        console.print(f"\nChat ID: [bold cyan]{chat['id']}[/bold cyan]")
        console.print(f"Last updated: {chat['updated_at']}")
        if chat['messages']:
            last_msg = chat['messages'][-1]
            preview = last_msg['content'][:50] + "..." if len(last_msg['content']) > 50 else last_msg['content']
            console.print(f"Last message: {preview}")

@app.command()
@check_login
def delete(chat_id: str):
    """Delete a saved chat"""
    if questionary.confirm(f"Are you sure you want to delete chat {chat_id}?", style=custom_style).ask():
        chat_manager.delete_chat(chat_id)
        console.print(f"[green]Deleted chat {chat_id}[/green]")

@app.command()
@check_login
def clear():
    """Clear all saved chats"""
    if questionary.confirm("Are you sure you want to delete all saved chats?", style=custom_style).ask():
        chat_manager.clear_chats()
        console.print("[green]All chats cleared[/green]") 