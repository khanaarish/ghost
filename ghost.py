import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as pwt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Ghost. Please tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendwhatsmsg():
    pwt.senwhatmsg("+919021599825",query,"here time")

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wkipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'open maps' in query:
            webbrowser.open("maps.google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            codePath = "E:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            os.startfile(webbrowser.Chrome)
            # i have dought in in above chrome opening code

        elif 'open notepad ' in query:
            notepadPath = "%windir%\system32\notepad.exe"
            os.startfile(notepadPath)
        
        elif 'open paint ' in query:
            paintPath = "%windir%\system32\mspaint.exe"
            os.startfile(paintPath)
        
        elif 'open snipping tool' in query:
            snippingPath = "%windir%\system32\SnippingTool.exe"
            os.startfile(snippingPath)

        elif 'open wordpad' in query:
            wordPath = "%ProgramFiles%\Windows NT\Accessories\wordpad.exe"
            os.startfile(wordPath)

        












