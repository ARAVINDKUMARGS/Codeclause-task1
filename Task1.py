import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("command.wav") as source:
    audio_data = recognizer.record(source)

text = recognizer.recognize_google(audio_data)
print("Recognized text:", text)

with open("task1_output.txt", "w") as f:
    f.write(text)
