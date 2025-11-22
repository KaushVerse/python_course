import random
from datetime import datetime

class SimpleChatBot:
    """Basic chatbot with predefined responses."""
    
    def __init__(self, name: str = "PyBot"):
        self.name = name
        self.responses = {
            "hello": ["Hi there! 👋", "Hey! How are you?", "Hello! Nice to meet you!"],
            "how are you": ["I'm doing great! 😊", "Feeling awesome!", "All systems operational! 🤖"],
            "what is your name": [f"I'm {self.name}! 🤖", f"My name is {self.name}"],
            "bye": ["Goodbye! 👋", "See you later!", "Take care!"],
            "time": [f"Current time is {datetime.now().strftime('%H:%M:%S')}"],
            "date": [f"Today is {datetime.now().strftime('%Y-%m-%d')}"],
            "help": ["I can respond to: hello, how are you, what is your name, bye, time, date, help"],
        }
    
    def get_response(self, user_input: str) -> str:
        """Generate response based on user input."""
        user_input = user_input.lower().strip()
        
        # Check for keyword matches
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)
        
        # Default response
        return "I didn't understand that. Type 'help' for available commands. 🤔"
    
    def chat(self) -> None:
        """Start interactive chat session."""
        print(f"\n🤖 {self.name} started! Type 'bye' to exit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}\n")
            
            if "bye" in user_input.lower():
                break


if __name__ == "__main__":
    bot = SimpleChatBot("PyBot")
    bot.chat()