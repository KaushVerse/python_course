# AI Chatbot

class AIChatbot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I am {self.name}, your AI chatbot. How can I assist you today?"

    def respond(self, user_input):
        # Simple response logic for demonstration purposes
        if "hello" in user_input.lower():
            return "Hi there! How can I help you?"
        elif "how are you" in user_input.lower():
            return "I'm just a chatbot, but I'm doing great! Thanks for asking."
        elif "bye" in user_input.lower():
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that. Can you please rephrase?"
        
# Example usage
if __name__ == "__main__":
    chatbot = AIChatbot("ChatGPT")
    print(chatbot.greet())
    
    user_input = input("You: ")
    while user_input.lower() != "bye":
        response = chatbot.respond(user_input)
        print(f"{chatbot.name}: {response}")
        user_input = input("You: ")
    
    print(f"{chatbot.name}: {chatbot.respond('bye')}")