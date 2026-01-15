# Leon - Your Open-Source Personal Assistant

Leon is a modular, open-source personal assistant that can help you with various tasks through natural language interaction.

## Features

- **Modular Skills System**: Easy to extend with new capabilities
- **Natural Language Processing**: Understands natural language commands
- **Interactive Mode**: Chat with Leon in real-time
- **Command Line Interface**: Execute single commands quickly
- **Privacy-Focused**: Runs locally on your machine

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone this repository:
```bash
git clone https://github.com/Pooka69/Leon.git
cd Leon
```

2. Make the script executable (Linux/Mac):
```bash
chmod +x leon.py
```

## Usage

### Interactive Mode

Run Leon in interactive mode for a conversation:

```bash
python leon.py
```

Or if made executable:
```bash
./leon.py
```

### Single Command Mode

Execute a single command:

```bash
python leon.py "what time is it?"
python leon.py "hello"
python leon.py "what's the date?"
```

## Available Skills

Leon currently supports the following skills:

### 1. Greeting
- Say hello and Leon will greet you back
- Examples: "hello", "hi", "good morning"

### 2. Time
- Get the current time
- Examples: "what time is it?", "current time"

### 3. Date
- Get today's date
- Examples: "what's the date?", "what day is it?"

### 4. Weather
- Weather information (feature coming soon)
- Examples: "what's the weather?"

### 5. Help
- Get information about available commands
- Examples: "help", "what can you do?"

## Example Interaction

```
You: hello
Leon: Good morning! I'm Leon, your personal assistant. How can I help you today?

You: what time is it?
Leon: The current time is 02:30 PM

You: what's the date?
Leon: Today is Monday, January 15, 2026

You: help
Leon: I'm Leon, your personal assistant. Here's what I can do:
        
• Greetings - Say hello and I'll greet you back
• Time - Ask "what time is it?" to get the current time
• Date - Ask "what's the date?" to get today's date
• Weather - Ask about weather (feature coming soon)
• Help - Ask for help to see this message

Just talk to me naturally, and I'll do my best to assist you!
```

## Extending Leon

Leon is designed to be easily extensible. To add a new skill:

1. Create a new class that inherits from the `Skill` base class
2. Implement the `can_handle()` method to determine if the skill can process a command
3. Implement the `execute()` method to perform the skill's action
4. Add your skill to the `_load_skills()` method in the `Leon` class

Example:

```python
class CalculatorSkill(Skill):
    """Handles calculation queries"""
    
    def __init__(self):
        super().__init__("Calculator")
        self.triggers = ["calculate", "compute", "what is"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        # Implement calculation logic here
        return "Calculation result"
```

## Architecture

Leon follows a modular architecture:

- **Leon Core**: Main assistant logic and command routing
- **Skills**: Modular components that handle specific tasks
- **Conversation History**: Tracks interactions for context

## Contributing

Contributions are welcome! Feel free to:

- Add new skills
- Improve existing functionality
- Fix bugs
- Enhance documentation

## License

This project is open source and available under the MIT License.

## Roadmap

- [ ] Add more built-in skills
- [ ] Implement weather API integration
- [ ] Add reminder and note-taking capabilities
- [ ] Implement voice interaction (STT/TTS)
- [ ] Add configuration file support
- [ ] Create skill marketplace
- [ ] Add LLM integration for more natural conversations

## Credits

Inspired by the [Leon AI project](https://github.com/leon-ai/leon) - an open-source personal assistant.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
