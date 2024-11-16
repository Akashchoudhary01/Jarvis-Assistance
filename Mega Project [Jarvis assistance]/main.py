import speech_recognition as sr
import webbrowser
import pyttsx3


recoginizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
            
        # Listain For The Wake Word "Jarvis"
        # obtain audio from the microphones
        r = sr.Recognizer()
        # command = r.recognize_sphinx(audio)    

        # recognize speech using Sphinx
        print("Recoginizing...")
        try:
            with sr.Microphone(device_index=0) as source:
                print("Listning...!")
                audio = r.listen(source)
            word = r.recognize_google_cloud(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
         
        except Exception as e:
            print("Error; {0}".format(e))

