import fakeyou
import os
import time
from pygame import mixer

fake_you = fakeyou.FakeYou()
# print(fake_you.list_voices(3000).title)
class FakeYouTalker:
    def __init__(self, username, password, model_name):
        self.username = username
        self.password = password
        self.model_name = model_name

    def __login_to_fakeyou(self):
        fake_you.login(self.username, self.password)

    def __get_tts_token(self, model_name):
        result = fake_you.search(model_name)
        return result.voices.modelTokens[0]

    def __generate_audio(self, text, filename):
        self.__login_to_fakeyou()
        tts_model_token = self.__get_tts_token(self.model_name)
        print(tts_model_token)
        fake_you.say(text=text, ttsModelToken=tts_model_token, filename=filename)


    def talk(self, text):
        mixer.init()
        print("test: 0")
        # Genera un nombre de archivo único basado en la hora actual
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = os.path.join(os.path.dirname(__file__), f"fakeyou_{timestamp}.wav")
        print("test: 1")
        
        self.__generate_audio(text, filename)  # Genera el nuevo archivo de audio

        # Cargamos el archivo de audio
        mixer.music.load(filename)
        
        # Reproducimos el audio
        mixer.music.play()

        # Esperamos hasta que termine la reproducción
        while mixer.music.get_busy():
            time.sleep(1)



