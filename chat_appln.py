import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen to the microphone
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

# Get time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

# Get date
def get_date():
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y")

# Process command
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        speak(f"The current time is {get_time()}")
    elif "date" in command:
        speak(f"Today is {get_date()}")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to help with that.")

# Main loop
if __name__ == "__main__":
    speak("Voice assistant activated.")
    while True:
        command = listen()
        if command:
            process_command(command)
