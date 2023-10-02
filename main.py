import os
import importlib
import threading
from bots import chat_completion
from talk import talk
import user

# Store API key in environment variable
os.environ['OPENAI_API_KEY'] = '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'

personajes = ["glados","homer"]

def menu():
    for personaje in personajes:
        print(f"- {personaje} \n")
    personaje = input(f"Elije tu personaje: ")
    
    while personaje not in personajes:
        personaje = input(f"Esa no es una opcion valida: ")

    return personaje

def presentacion():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print("\n")
    print("-"*40)
    print("Para Terminar introduzca: Adios")
    print("-"*40)
    print("\n")
    
    print("\n")
    print("-"*40)
    personaje = menu()
    print("-"*40)
    print("\n")
    
    return personaje

if __name__ == "__main__":
    
    userMessage = ""
    messages = chat_completion.initialize_messages(personaje)
    
    personaje = presentacion()
    
    if personaje == "glados":
        talker = talk.FakeYouTalker(user.user, user.password, "GLaDOS (Portal, Castillian Spanish)")
    if personaje == "homer":
        talker = talk.FakeYouTalker(user.user, user.password, "GLaDOS (Portal, Castillian Spanish)")
    
    while userMessage != "Adios":
        
        userMessage = input("User Message: ")
        
        botMessage = chat_completion.main(userMessage, messages)
        
        print("\n")
        print("-"*40)
        print("\n")
        print(f"Bot Message: {botMessage}")
        print("\n")
        print("-"*40)
        print("\n")
        
        talker.talk(botMessage)
        
    
    