#!/usr/bin/env python3
"""
Example: Using Leon with a single command
"""

import sys
sys.path.insert(0, '..')

from leon import Leon

def main():
    # Create a Leon instance
    assistant = Leon()
    
    # Process various commands
    commands = [
        "hello",
        "what time is it?",
        "what's the date?",
        "help"
    ]
    
    print("=" * 60)
    print("Leon - Single Command Example")
    print("=" * 60)
    print()
    
    for command in commands:
        print(f"You: {command}")
        response = assistant.process_command(command)
        print(f"Leon: {response}")
        print()

if __name__ == "__main__":
    main()
