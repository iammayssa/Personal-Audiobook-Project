import speech_recognition as sr
# from google_trans_new import google_translator
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

r = sr.Recognizer()
# translator=google_translator()
translator = Translator()

while True:

    with sr.Microphone() as source:
        print("speak now")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:

            text = r.recognize_google(audio)
            print('Text: ' + text)
            if (text == "stop"):
                break

        except sr.UnknownValueError:
            print('Unknown Value')

        except sr.RequestError:
            print('Invalid Request')

        # try:
        # speech_text=r.recognizer_google(audio)
        # print(speech_text)
        # except sr.UnkownValueError:
        #   print("could not understand")
        # except sr.RequestError:
        #    print("could not request result from google")

        k = translator.translate(text, dest='french')

        translated = str(k.text)

        print(translated)

        voice = gTTS(translated, lang='fr')

        voice.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")