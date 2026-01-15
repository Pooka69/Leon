#!/usr/bin/env python3
"""
Example: Extending Leon with a custom skill
"""

import sys
import os
import re

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leon import Leon, Skill
from typing import Dict

class CalculatorSkill(Skill):
    """Handles basic arithmetic calculations"""
    
    def __init__(self):
        super().__init__("Calculator")
        self.triggers = ["calculate", "compute", "math", "plus", "minus", "times", "divided"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        try:
            # Extract numbers from command (matches integers and decimals like 5, 5.0, 5.25)
            numbers = re.findall(r'\d+(?:\.\d+)?', command)
            
            if len(numbers) < 2:
                return "Please provide at least two numbers for calculation."
            
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            
            # Determine operation
            command_lower = command.lower()
            if any(word in command_lower for word in ["plus", "+", "add"]):
                result = num1 + num2
                operation = "plus"
            elif any(word in command_lower for word in ["minus", "-", "subtract"]):
                result = num1 - num2
                operation = "minus"
            elif any(word in command_lower for word in ["times", "*", "multiply", "multiplied"]):
                result = num1 * num2
                operation = "times"
            elif any(word in command_lower for word in ["divided", "/", "divide"]):
                if num2 == 0:
                    return "I cannot divide by zero!"
                result = num1 / num2
                operation = "divided by"
            else:
                return "I can help with addition, subtraction, multiplication, and division."
            
            return f"{num1} {operation} {num2} equals {result}"
            
        except ValueError:
            return "Sorry, I couldn't extract valid numbers from your request."
        except Exception:
            return "Sorry, I couldn't perform that calculation. Please try again."


def main():
    # Create a Leon instance
    assistant = Leon()
    
    # Add the custom calculator skill
    calculator = CalculatorSkill()
    assistant.skills.append(calculator)
    
    print("=" * 60)
    print("Leon - Custom Skill Example (Calculator)")
    print("=" * 60)
    print()
    
    # Test the calculator skill
    test_commands = [
        "what is 5 plus 3?",
        "calculate 10 minus 4",
        "what's 7 times 6?",
        "compute 20 divided by 4",
    ]
    
    for command in test_commands:
        print(f"You: {command}")
        response = assistant.process_command(command)
        print(f"Leon: {response}")
        print()

if __name__ == "__main__":
    main()
