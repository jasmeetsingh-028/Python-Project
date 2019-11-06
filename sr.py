import speech_recognition as sr
from gtts import gTTS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer
mixer.init()
while (True == True):
 r = sr.Recognizer()
 with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=5)
    try:
     response = r.recognize_google(audio)
     print("I think you said '" + response + "'")
     tts = gTTS(text="I think you said "+str(response), lang='en')
     tts.save("response.mp3")
     mixer.music.load('response.mp3')
     mixer.music.play()
    except sr.UnknownValueError:
     print("Sphinx could not understand audio")
    except sr.RequestError as e:
     print("Sphinx error; {0}".format(e))