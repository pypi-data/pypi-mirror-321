# Based CLI

A powerful CLI tool for interacting with various AI models including OpenAI, Anthropic, Mistral, Groq, and Hugging Face.

## Features

- Multiple AI providers support
- Customizable system prompts
- Chat history management
- Interactive configuration
- Beautiful terminal UI

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd based-cli
```

2. Install the package:
```bash
pip install -e .
```

## Usage

1. Login and configure:
```bash
based login
```

2. Start chatting:
```bash
based
```

3. Other commands:
```bash
based config  # Edit configuration
based list    # List saved chats
based delete  # Delete a chat
based clear   # Clear all chats
```

## Available Models

- OpenAI: GPT-4, GPT-4 Turbo
- Anthropic: Claude 3 Sonnet, Claude 3 Opus
- Mistral: Mistral Large, CodeStraal
- Groq: Llama2 70B, Mixtral 8x7B
- Hugging Face: CodeRQween, StarCoder2, CodeLlama

## System Prompts

- Default: General software development assistant
- Code Assistant: Expert programming helper
- Terminal Expert: Command-line specialist
- Debugging Expert: Troubleshooting guide

## Requirements

- Python 3.9 or higher
- API keys for the providers you want to use 