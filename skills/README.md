# Leon Skills

This directory is where you can add custom skills to extend Leon's capabilities.

## Creating a Custom Skill

To create a new skill, follow these steps:

1. Create a new Python file in this directory (e.g., `my_skill.py`)
2. Import the base `Skill` class from `leon.py`
3. Create your skill class that inherits from `Skill`
4. Implement the required methods: `can_handle()` and `execute()`

## Example: Calculator Skill

Here's an example of a simple calculator skill:

```python
from leon import Skill
from typing import Dict
import re

class CalculatorSkill(Skill):
    """Handles basic arithmetic calculations"""
    
    def __init__(self):
        super().__init__("Calculator")
        self.triggers = ["calculate", "compute", "math", "plus", "minus", "times", "divided"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        # Extract numbers and operations from command
        # For example: "what is 5 plus 3?"
        try:
            # Simple pattern matching for basic operations
            if "plus" in command.lower() or "+" in command:
                numbers = re.findall(r'\d+', command)
                if len(numbers) >= 2:
                    result = int(numbers[0]) + int(numbers[1])
                    return f"The result is {result}"
            
            return "I can help with calculations, but I need the numbers and operation."
        except Exception as e:
            return f"Sorry, I couldn't perform that calculation: {str(e)}"
```

## Adding Your Skill to Leon

After creating your skill file, you need to:

1. Import it in `leon.py`
2. Add an instance of your skill to the `_load_skills()` method

Example modification to `leon.py`:

```python
from skills.my_skill import CalculatorSkill

def _load_skills(self):
    """Load all available skills"""
    self.skills = [
        GreetingSkill(),
        TimeSkill(),
        DateSkill(),
        WeatherSkill(),
        HelpSkill(),
        CalculatorSkill(),  # Add your new skill here
    ]
```

## Skill Guidelines

- Keep skills focused on a single purpose
- Use clear trigger words
- Provide helpful error messages
- Document your skill's capabilities
- Handle edge cases gracefully
