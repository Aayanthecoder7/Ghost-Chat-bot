import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import openai
import pyttsx3

api_key = "Your api key here idk why it should be private i just did it for fun"

openai.api_key = api_key

engine = pyttsx3.init()

root = tk.Tk()
root.geometry("500x500")
root.config(bg="White")
root.title("GHO$T_AK")
icon_image = Image.open("hacker_logo.png")
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

title_label = Label(root, text="GHO$T_AK", font=("Cascadia Code", 37), bg="White")
title_label.pack()

img = tk.PhotoImage(file="hacker_logo.png")
label = tk.Label(root, image=img)
label.pack()

l_label = Label(root, text="", font=("Arial", 15), bg="White", fg="Black")
l_label.pack()


def talk_buttonn():
    l_label.config(text="Listening...", font=("Old English Text MT", 15), bg="White", fg="Black")
    l_label.update_idletasks()

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
      
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            
            audio = recognizer.listen(source)
            l_label.config(text="Processing your input...", font=("Old English Text MT", 15), bg="White", fg="Black")

            user_input = recognizer.recognize_google(audio)
            l_label.config(text=f"You said: {user_input}", font=("Old English Text MT", 15), bg="White", fg="Black")

            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=user_input,
                max_tokens=150
            )
            
            chatgpt_response = response.choices[0].text.strip()

            engine.say(chatgpt_response)
            engine.runAndWait()

            engine.say(user_input)
            engine.runAndWait()
            
        except sr.UnknownValueError:
            l_label.config(text="Sorry, I could not understand what you said.", font=("Old English Text MT", 15), bg="White", fg="Black")
        except sr.RequestError as e:
            l_label.config(text=f"Could not request results; {e}", font=("Old English Text MT", 15), bg="White", fg="Black")

talk_button = Button(root, text="Talk", font=("Arial", 15), bg="White", fg="Black", command=talk_buttonn)
talk_button.pack()

root.mainloop()