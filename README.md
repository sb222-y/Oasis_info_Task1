# Oasis_info_Task1

## 🗣️ Voice Assistant in Python
A simple voice-activated assistant built using Python that can recognize your voice, respond with speech, tell the time and date, perform Google searches, and more.

## 🚀 Features
🔊 Text-to-Speech (TTS) using pyttsx3
🎤 Speech Recognition using Google Web Speech API
⏰ Tell the Current Time and Date
🌐 Google Search Support
🛑 Exit the Assistant via Voice Command

## 📁 Project Structure
voice_assistant/
│
├── assistant.py         # Main Python script
├── README.md            # This file
└── requirements.txt     # Python dependencies

## 🛠️ Installation

1. Clone the repository:
git clone https://github.com/sb222-y/voice_assistant.git
cd voice_assistant

2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Scripts\activate          # On Windows

3.Install dependencies:
pip install -r requirements.txt

# 📦 If you get errors with pyaudio, install it via pipwin:
pip install pipwin
pipwin install pyaudio

## ▶️ Usage
python assistant.py

## Speak commands like:

1. "hello"
2. "what time is it"
3. "what's the date"
4. "search OpenAI"
5. "exit"

## 📋 Dependencies
1. SpeechRecognition
2. pyttsx3
3. pyaudio
4. datetime
5. webbrowser

## Add to requirements.txt:
SpeechRecognition
pyttsx3
pyaudio

## 🧠 Future Enhancements
1. Add weather info using OpenWeather API
2. Launch local applications (e.g., Chrome, Notepad)
3. Play music or open files/folders
4. Add voice authentication

## 📜 License
MIT License

## 🙋‍♀️ Author
Sanskruti Yewale
https://github.com/sb222-y

