import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything   : ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said : {text}")
       
    except:
        print("Sorry could not get you ")
        print("Say it again ")




























