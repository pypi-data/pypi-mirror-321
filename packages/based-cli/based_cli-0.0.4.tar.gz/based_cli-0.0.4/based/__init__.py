"""Based CLI - Your AI assistant in the terminal"""

from .cli import app

__version__ = "0.0.1"
__author__ = "nonom"
__email__ = "nounsplayground@gmail.com"

# Make sure all modules are properly imported
from . import cli
from . import config
from . import chat_manager 