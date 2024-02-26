import speech_recognition as speech
from pygame import mixer
import os
from pynput.keyboard import Key, Controller
from gtts import gTTS
from  time import  sleep

def speak(text):
    gtts = gTTS(text = text,lang="en")
    gtts.save("temp.mp3")
    sound = mixer.Sound(file="temp.mp3")
    sound.play()
# загрузить файл , озвучить


# подключаем клавиотуру
printing = False
keyboard = Controller()
# создаем узнователь
rec = speech.Recognizer()
mixer.init()
while True:
    with speech.Microphone() as micro:
        #  наченаем слушать
        speak("I'm starting to listen")
        sleep(1.5)
        print("I'm starting to listen")
        audio_data = rec.listen(micro,phrase_time_limit= 5)
        speak("I'm done listening")
        sleep(1.5)
        print("I'm done listening")
    # пробуем распознать текст из аудио
    try:
        text = rec.recognize_google(audio_data, language="en-US").lower()
        print(text)
        if not printing:

            if "stop" in text:
                break
            if "open" in text:
                speak("im opening")
                sleep(1.5)
                if "google" in text:
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
                if "раст" in text or "rust" in text:
                    os.startfile("C:\\Users\\goldi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Rust.url")
                if "roblox" in text:
                    os.startfile("C:\\Users\\goldi\\Desktop\\Roblox Player.lnk")
                if "discord" in text:
                    os.startfile("C:\\Users\\goldi\\Desktop\\Discord.lnk")
                if "steam" in text:
                    os.startfile("C:\\Users\\Public\\Desktop\\Steam.lnk")
            if "print" in text:
                printing = True
                print("start printing")
                speak("im starting printing")
                sleep(1.5)
        else:
            # for letter in text:
            #     keyboard.press(letter)
            #     keyboard.release(letter)
            if "stop" in text:
                printing = False
            else:
                keyboard.type(text)


    except speech.exceptions.UnknownValueError:
        print("couldnt hear")