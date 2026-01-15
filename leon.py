#!/usr/bin/env python3
"""
Leon - Your Open-Source Personal Assistant
A minimal implementation of a modular personal assistant
"""

import sys
import json
from datetime import datetime
from typing import Dict, List, Optional


class Skill:
    """Base class for Leon skills"""
    
    def __init__(self, name: str):
        self.name = name
    
    def execute(self, command: str, params: Dict) -> str:
        """Execute the skill with given command and parameters"""
        raise NotImplementedError("Subclasses must implement execute()")
    
    def can_handle(self, command: str) -> bool:
        """Check if this skill can handle the given command"""
        raise NotImplementedError("Subclasses must implement can_handle()")


class GreetingSkill(Skill):
    """Handles greeting and introduction commands"""
    
    def __init__(self):
        super().__init__("Greeting")
        self.greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
    
    def can_handle(self, command: str) -> bool:
        return any(greeting in command.lower() for greeting in self.greetings)
    
    def execute(self, command: str, params: Dict) -> str:
        hour = datetime.now().hour
        if 5 <= hour < 12:
            time_greeting = "Good morning"
        elif 12 <= hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        return f"{time_greeting}! I'm Leon, your personal assistant. How can I help you today?"


class TimeSkill(Skill):
    """Handles time-related queries"""
    
    def __init__(self):
        super().__init__("Time")
        self.triggers = ["time", "what time", "current time", "clock"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"


class DateSkill(Skill):
    """Handles date-related queries"""
    
    def __init__(self):
        super().__init__("Date")
        self.triggers = ["date", "what date", "today", "what day"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        now = datetime.now()
        return f"Today is {now.strftime('%A, %B %d, %Y')}"


class WeatherSkill(Skill):
    """Handles weather queries (placeholder)"""
    
    def __init__(self):
        super().__init__("Weather")
        self.triggers = ["weather", "temperature", "forecast"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        return "Weather feature is not yet configured. Please add your weather API key to enable this feature."


class HelpSkill(Skill):
    """Provides help information"""
    
    def __init__(self):
        super().__init__("Help")
        self.triggers = ["help", "what can you do", "capabilities", "commands"]
    
    def can_handle(self, command: str) -> bool:
        return any(trigger in command.lower() for trigger in self.triggers)
    
    def execute(self, command: str, params: Dict) -> str:
        return """I'm Leon, your personal assistant. Here's what I can do:
        
• Greetings - Say hello and I'll greet you back
• Time - Ask "what time is it?" to get the current time
• Date - Ask "what's the date?" to get today's date
• Weather - Ask about weather (feature coming soon)
• Help - Ask for help to see this message

Just talk to me naturally, and I'll do my best to assist you!"""


class Leon:
    """Main Leon assistant class"""
    
    def __init__(self):
        self.skills: List[Skill] = []
        self.conversation_history = []
        self._load_skills()
    
    def _load_skills(self):
        """Load all available skills"""
        self.skills = [
            GreetingSkill(),
            TimeSkill(),
            DateSkill(),
            WeatherSkill(),
            HelpSkill(),
        ]
    
    def process_command(self, command: str) -> str:
        """Process a command and return the response"""
        if not command or not command.strip():
            return "I didn't catch that. Could you please repeat?"
        
        command = command.strip()
        self.conversation_history.append({"role": "user", "message": command})
        
        # Try to find a skill that can handle this command
        for skill in self.skills:
            if skill.can_handle(command):
                response = skill.execute(command, {})
                self.conversation_history.append({"role": "assistant", "message": response})
                return response
        
        # No skill found
        response = "I'm not sure how to help with that yet. Try asking for 'help' to see what I can do."
        self.conversation_history.append({"role": "assistant", "message": response})
        return response
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []


def interactive_mode():
    """Run Leon in interactive mode"""
    leon = Leon()
    
    print("=" * 60)
    print("Leon - Your Open-Source Personal Assistant")
    print("=" * 60)
    print("\nType 'exit' or 'quit' to end the session")
    print("Type 'clear' to clear conversation history")
    print("Type 'help' to see available commands\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nLeon: Goodbye! Have a great day!")
                break
            
            if user_input.lower() == 'clear':
                leon.clear_history()
                print("\nLeon: Conversation history cleared.\n")
                continue
            
            response = leon.process_command(user_input)
            print(f"\nLeon: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nLeon: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Process single command
        leon = Leon()
        command = ' '.join(sys.argv[1:])
        response = leon.process_command(command)
        print(response)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
