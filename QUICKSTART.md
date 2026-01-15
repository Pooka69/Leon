# Quick Start Guide for Leon Personal Assistant

Welcome to Leon! This guide will help you get started quickly.

## Installation

No dependencies required - just Python 3.7+!

```bash
git clone https://github.com/Pooka69/Leon.git
cd Leon
```

## Usage

### Interactive Mode (Recommended for first-time users)

```bash
python leon.py
```

Example session:
```
You: hello
Leon: Good afternoon! I'm Leon, your personal assistant. How can I help you today?

You: what time is it?
Leon: The current time is 02:30 PM

You: help
Leon: I'm Leon, your personal assistant. Here's what I can do...
```

### Single Command Mode

```bash
python leon.py "what time is it?"
python leon.py "hello"
```

## What Can Leon Do?

1. **Greet you** - Try: "hello", "hi", "good morning"
2. **Tell time** - Try: "what time is it?"
3. **Tell date** - Try: "what's the date?"
4. **Show help** - Try: "help"
5. **Weather** (coming soon)

## Running Examples

```bash
# Basic usage example
python examples/single_command.py

# Custom skill example (calculator)
python examples/custom_skill.py
```

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Check [skills/README.md](skills/README.md) to learn how to create custom skills
3. Look at [examples/custom_skill.py](examples/custom_skill.py) for a working example

## Customization

Create `config/config.json` to customize Leon:

```json
{
  "assistant_name": "Leon",
  "language": "en",
  "voice_enabled": false,
  "weather_api_key": "",
  "timezone": "UTC"
}
```

## Getting Help

- Type `help` when interacting with Leon
- Check the [README.md](README.md) for full documentation
- Open an issue on GitHub if you encounter problems

Enjoy using Leon!
