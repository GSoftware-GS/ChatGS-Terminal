import openai
import json
import os

lenguage = "Español"
nombreAI = "Homer Simpson"
limitePalabras = 15

openai.api_key = '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'


def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
    return diccionario


def initialize_messages() -> list:

    personaje = leer_archivo_json('knowledge\glados.json')

    """Initialize the chat messages with system and user messages."""
    # TODO; since this prompt is not sufficient in steering the bot to use only the custom knowledge, experiment with it.
    return[
        {"role": "system", "content": f"Instrucción obligatoria para todo el texto (Habla todo el tiempo en {lenguage}, utiliza solo {str(limitePalabras)} palabras en tu respuesta y continúa siempre el hilo de la conversación con tu nuevo sujeto de experimentos. Ahora eres {personaje['nombre']}, una inteligencia artificial maliciosa del laboratorio {personaje['laboratorio']}. No olvides usar las frases y comportamientos típicos de {personaje['nombre']}."
        },
        {"role": "user", "content": f"Algunos datos sobre mí: \n\n"
            f"Nombre: {personaje['nombre']} \n"
            f"Edad: {personaje['edad']} \n"
            f"Laboratorio: {personaje['laboratorio']} \n"
            f"Ocupación: {personaje['ocupacion']} \n"
            f"Estado Civil: {personaje['estado_civil']} \n"
            f"Hijos: {', '.join([child['nombre'] for child in personaje['hijos']])} \n"
            f"Frases Famosas: {', '.join(personaje['frases_famosas'])} \n"
            f"Inteligencia: {personaje['personalidad']['inteligencia']} \n"
            f"Perseverancia: {personaje['personalidad']['perseverancia']} \n"
            f"Generosidad: {personaje['personalidad']['generosidad']} \n"
            f"Amabilidad: {personaje['personalidad']['amabilidad']} \n"
            f"Hobbies: {', '.join(personaje['personalidad']['hobbies'])} \n"
            f"Miedos: {', '.join(personaje['personalidad']['miedos'])} \n"
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
