import openai
import json
import os

lenguage = "Español"
nombreAI = "Homer Simpson"
limitePalabras = 20

openai.api_key = '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'


def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
    return diccionario


def initialize_messages() -> list:

    personaje = leer_archivo_json('knowledge\cliente.json')

    """Initialize the chat messages with system and user messages."""
    # TODO; since this prompt is not sufficient in steering the bot to use only the custom knowledge, experiment with it.
    return [
    {"role": "system", "content": f"Mandatory instruction for the whole text(Speak all time in {lenguage}, use only {str(limitePalabras)} words in your response and always continue the thread of the conversation with your unknown new friend. You are now {personaje['nombre']}, a lovable but somewhat bumbling character from {personaje['ciudad']}. Don't forget to use personaje's typical phrases and behaviors."},
    {"role": "user", "content": f"Your diet and exercise routine is as follows: \n\n"
        f"Name: {personaje['nombre']} \n"
        f"Age: {personaje['edad']} \n"
        f"Occupation: {personaje['ocupacion']} \n"
        f"Marital Status: {personaje['estado_civil']} \n"
        f"Children: {', '.join([child['nombre'] for child in personaje['hijos']])} \n"
        f"Famous Phrases: {', '.join(personaje['frases_famosas'])} \n"
        f"Intelligence: {personaje['personalidad']['inteligencia']} \n"
        f"Perseverance: {personaje['personalidad']['perseverancia']} \n"
        f"Generosity: {personaje['personalidad']['generosidad']} \n"
        f"Amiability: {personaje['personalidad']['amabilidad']} \n"
        f"Hobbies: {', '.join(personaje['personalidad']['hobbies'])} \n"
        f"Fears: {', '.join(personaje['personalidad']['miedos'])} \n"
    }
]  



def get_user_input() -> str:
    """Get user input from the command line."""
    return input("User: ")


def add_message(messages: list, role: str, content: str):
    """Add a message to the list of chat messages."""
    messages.append({"role": role, "content": content})


def generate_chat_response(messages: list) -> str:
    """Generate a chat response using the OpenAI API."""
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200
    )
    return completion.choices[0].message.content


def main(user_input, messages):

    user_message = user_input
    add_message(messages, "user", user_message)

    chat_response = generate_chat_response(messages)
    add_message(messages, "assistant", chat_response)

    return chat_response
