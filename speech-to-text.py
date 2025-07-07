import speech_recognition as sr
import pyttsx3
import keyboard  # To listen for keyboard presses

# Initialize recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Flag to track listening state
listening = False

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands and convert to text
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        try:
            # Use Google's speech-to-text API to convert speech to text
            command = r.recognize_google(audio)
            print(f"You said: {command}")  # Print recognized command
            speak(f"Command recognized: {command}")  # Read it aloud
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak(f"Could not request results; {e}")
            return None

# Function to toggle listening with the keyboard shortcut
def toggle_listening(shortcut="ctrl+shift+l"):
    global listening

    print(f"Press {shortcut} to toggle listening.")
    
    while True:
        if keyboard.is_pressed(shortcut):  # Detect the shortcut key press
            if not listening:  # If not already listening, start listening
                print("Starting to listen...")
                speak("How can I assist you?")
                command = listen_for_command()  # Listen for the command
                if command:
                    # Just convert and display the command
                    print(f"Converted Command: {command}")
                    speak(f"Command recognized: {command}")
                listening = True
            else:  # If already listening, stop listening
                print("Stopped listening.")
                listening = False
                break  # Exit the loop after stopping
        else:
            continue

# Start the toggle listening process
toggle_listening()