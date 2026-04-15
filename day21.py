import pyttsx3

engine = pyttsx3.init()

def speak_tex(speak_to_text):
    print(speak_to_text)
    engine.say(speak_to_text)
speak_tex("hello, iam your assistant")
engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()

def speak_text(siri):
    engine.say(siri)
client = input("Enter you message: ").lower()
name = "clien"
if "my name is" in client:
     name = client.split("my name is")[-1].strip()
elif "name is" in client:
    name = client.split("name is")[-1].strip()
if client in ["hi", "hello", "hey"]:
    respond = "Hello! how can i help you ?"
elif "name" in client:
    respond = f"Hello {name}, how can i help you ?"
else:
    respond = "sorry , i didn't understand that"
print(respond)
speak_text(respond)
engine.runAndWait()
