import os
import importlib
import threading
from bots import chat_completion


# Store API key in environment variable
os.environ['OPENAI_API_KEY'] = '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'


if __name__ == "__main__":
    
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("\n")
    print("-"*20)
    print("Para Terminar introduzca: Adios")
    print("-"*20)
    print("\n")
    
    userMessage = ""
    messages = chat_completion.initialize_messages()
    
    while userMessage != "Adios":
        userMessage = input("User Message: ")
        
        botMessage = chat_completion.main(userMessage, messages)
        
        print("\n")
        print("-"*20)
        print("\n")
        print(f"Bot Message: {botMessage}")
        print("\n")
        print("-"*20)
        print("\n")
        
    
    