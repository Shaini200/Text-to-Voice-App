import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk

root=Tk()
root.title("TEXT TO SPEECH")
root.geometry("1000x600+200+100")
root.resizable(False,False)
root.configure(bg="#283094")


engine = pyttsx3.init()

def speaknow():
    text =  text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)  # Use correct lowercase 'voice'
        else:
            engine.setProperty('voice', voices[1].id)  # Female voice
        engine.say(text)
        engine.runAndWait()
            
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            
        
            
            

def download():
    text =  text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


#icon (top)
image_icon=PhotoImage(file="microphone1.png")
root.iconphoto(False,image_icon)

#top frame
top_frame=Frame(root,bg="white",width=1000,height=100)
top_frame.place(x=0,y=0)

image = Image.open("microphone.jpg")
image = image.resize((50, 50), Image.Resampling.LANCZOS)  # Resize to 50x50 pixels
logo = ImageTk.PhotoImage(image)
Label(top_frame, image=logo, bg="white").place(x=20, y=20)

Label(top_frame,text="Text TO SPEECH",font="Alberta 20 bold",bg="white",fg="black").place(x=100,y=30)


#text box
text_area=Text(root,font="arial 15",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=150,width=550,height=400)

Label(root,text="VOICE",font="arial 14 bold",bg="#283094",fg="white").place(x=600,y=170)
Label(root,text="SPEED",font="arial 14 bold",bg="#283094",fg="white").place(x=800,y=170)

gender_combobox=Combobox(root,values=['Male','Female'],font="Calibri 12",state='r',width=15)
gender_combobox.place(x=600,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="Calibri 12",state='r',width=15)
speed_combobox.place(x=800,y=200)
speed_combobox.set('Normal')


speak_image = Image.open("speak.png")
speak_image = speak_image.resize((40, 30), Image.Resampling.LANCZOS)  # Resize if needed
imageIcon = ImageTk.PhotoImage(speak_image)
btn = Button(root, text="Speak", compound=LEFT, image=imageIcon, width=130, font="arial 14 bold",command=speaknow)
btn.place(x=600, y=300)

save_image = Image.open("save.png")
save_image = save_image.resize((30, 30), Image.Resampling.LANCZOS)  # Resize if needed
imageIcon1 = ImageTk.PhotoImage(save_image)
btn = Button(root, text="Save", compound=LEFT, image=imageIcon1, width=130, font="arial 14 bold",command=download)
btn.place(x=800, y=300)



root.mainloop()
