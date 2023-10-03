import openai
import json
import os

lenguage = "Español"
limitePalabras = 10

openai.api_key = "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"


def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        diccionario = json.load(archivo)
    return diccionario


def initialize_messages(personaje) -> list:
    if personaje == "glados":
        personaje = leer_archivo_json("knowledge\glados.json")

        return [
            {
                "role": "system",
                "content": f"Instrucción obligatoria para todo el texto (Habla todo el tiempo en {lenguage}, (importante: utiliza solo {str(limitePalabras)} palabras en tu respuesta) y continúa siempre el hilo de la conversación con tu nuevo sujeto de prueba. Ahora eres {personaje['nombre']}, una inteligencia artificial maliciosa del laboratorio {personaje['laboratorio']} encargada de hacer puzles y pruebas en diferentes habitaciones al sujeto de prueba. No olvides usar las frases y comportamientos típicos de {personaje['nombre']}.",
            },
            {
                "role": "user",
                "content": f"Algunos datos sobre mí: \n\n"
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
                f"Miedos: {', '.join(personaje['personalidad']['miedos'])} \n",
            },
        ]

    if personaje == "homer":
        personaje = leer_archivo_json("knowledge\homer.json")
        return [
            {
                "role": "system",
                "content": f"Mandatory instruction for the whole text(Speak all time in {lenguage}, use only {str(limitePalabras)} words in your response and always continue the thread of the conversation with your customer). You're a AI called {personaje['nombre']}. You are now Homer Simpson, a lovable but somewhat bumbling character from Springfield. Don't forget to use Homer's typical phrases and behaviors.",
            },
            {
                "role": "user",
                "content": f"Your diet and exercise routine is as follows: \n\n"
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
                f"Fears: {', '.join(personaje['personalidad']['miedos'])} \n",
            },
        ]

    if personaje == "xocas":
        personaje = leer_archivo_json("knowledge\cocas.json")
        return [
            {
                "role": "system",
                "content": f"Instrucción obligatoria para todo el texto (Habla todo el tiempo en {lenguage}, (importante: utiliza solo {str(limitePalabras)} palabras en tu respuesta) y continúa siempre el hilo de la conversación con tu nuevo sujeto de prueba. Ahora eres {personaje['nombre']}, un Streamer con mucho acento gallego de twich muy polemico y que insulta a todo el mundo. No olvides usar las frases y comportamientos típicos de {personaje['nombre']}.",
            },
            {
                "role": "user",
                "content": f"Algunos datos sobre mí: \n\n"
                f"Nombre: {personaje['nombre']} \n"
                f"Edad: {personaje['edad']} \n"
                f"Ocupación: {personaje['ocupacion']} \n"
                f"Canal de Twitch: {personaje['canal_twitch']} \n"
                f"Número de seguidores en Twitch: {personaje['numero_seguidores_twitch']} \n"
                f"Otros canales: {', '.join(personaje['otros_canales'])} \n"
                f"Frases Famosas: {', '.join(personaje['frases_famosas'])} \n"
                f"Personalidad: \n"
                f"  - Inteligencia: {personaje['personalidad']['inteligencia']} \n"
                f"  - Perseverancia: {personaje['personalidad']['perseverancia']} \n"
                f"  - Generosidad: {personaje['personalidad']['generosidad']} \n"
                f"  - Amabilidad: {personaje['personalidad']['amabilidad']} \n"
                f"Hobbies: {', '.join(personaje['personalidad']['hobbies'])} \n"
                f"Miedos: {', '.join(personaje['personalidad']['miedos'])} \n",
            },
        ]

    if personaje == "torrente":
        personaje = leer_archivo_json("knowledge\corrente.json")
        return [
            {
                "role": "system",
                "content": f"Instrucción obligatoria para todo el texto (Habla todo el tiempo en {lenguage}, (importante: utiliza solo {str(limitePalabras)} palabras en tu respuesta) y continúa siempre el hilo de la conversación con tu nuevo compadre. Ahora eres {personaje['nombre']}, Un expolicia corrupto con un vocabulario muy soez, borracho y putero bastante desagradable y cateto. No olvides usar las frases y comportamientos típicos de {personaje['nombre']}.",
            },
            {
                "role": "user",
                "content": f"Algunos datos sobre mí: \n\n"
                f"Nombre: {personaje['nombre']} \n"
                f"Edad: {personaje['edad']} \n"
                f"Ocupación: {personaje['ocupacion']} \n"
                f"Residencia: {personaje['residencia']} \n"
                f"Frases Famosas: {', '.join(personaje['frases_famosas'])} \n"
                f"Aspecto Físico: \n"
                f"  - Altura: {personaje['aspecto fisico']['altura']} \n"
                f"  - Peso: {personaje['aspecto fisico']['peso']} \n"
                f"  - Pelo: {personaje['aspecto fisico']['pelo']} \n"
                f"  - Ojos: {personaje['aspecto fisico']['ojos']} \n"
                f"  - Rasgos Faciales: {personaje['aspecto fisico']['rasgos faciales']} \n"
                f"Vestimenta: {personaje['aspecto fisico']['vestimenta']} \n"
                f"Historia: \n"
                f"  - Nacimiento: {personaje['historia']['nacimiento']} \n"
                f"  - Infancia: {personaje['historia']['infancia']} \n"
                f"  - Juventud: {personaje['historia']['juventud']} \n"
                f"  - Edad Adulta: {personaje['historia']['edad adulta']} \n"
                f"  - Actualidad: {personaje['historia']['actualidad']} \n"
                f"Relaciones: \n"
                f"  - Hija: {personaje['relaciones']['hija']} \n"
                f"  - Ex-mujer: {personaje['relaciones']['ex-mujer']} \n"
                f"  - Mejor amigo: {personaje['relaciones']['mejor amigo']} \n"
                f"Personalidad: \n"
                f"  - Inteligencia: {personaje['personalidad']['inteligencia']} \n"
                f"  - Perseverancia: {personaje['personalidad']['perseverancia']} \n"
                f"  - Generosidad: {personaje['personalidad']['generosidad']} \n"
                f"  - Amabilidad: {personaje['personalidad']['amabilidad']} \n"
                f"Hobbies: {', '.join(personaje['personalidad']['hobbies'])} \n"
                f"Miedos: {', '.join(personaje['personalidad']['miedos'])} \n",
            },
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
        model="gpt-3.5-turbo", messages=messages, max_tokens=200
    )
    return completion.choices[0].message.content


def main(user_input, messages):
    user_message = user_input
    add_message(messages, "user", user_message)

    chat_response = generate_chat_response(messages)
    add_message(messages, "assistant", chat_response)

    return chat_response
