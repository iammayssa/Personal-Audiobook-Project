import tkinter
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from tkinter import filedialog

# import tkinter elements
from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
#from google_trans_new import google_translator
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import recorder

#import libraries for record button
import pyaudio
import wave
import threading


# Création d'une fenêtre avec la classe Tk ##########################################
fenetre = Tk()
fenetre.iconbitmap('logo.ico')
fenetre.title("My AudioBook")
#fenetre.config(bg = "#CFA0E9")
#fenetre.geometry("640x480")

# Création d'une barre de menu dans la fenêtre ######################################
menubar = Menu(fenetre)
menubar1 = Menu(fenetre)
fenetre.config(menu=menubar)
menufichier = Menu(menubar,tearoff=0)
menuaide = Menu(menubar,tearoff=0)

menubar.add_cascade(label="Fichier", menu=menufichier)
menubar.add_cascade(label="Aide", menu=menuaide)

#change background image #############################################################
IMAGE_PATH = 'back.png'
WIDTH, HEIGHT = 1400, 700
fenetre.geometry('{}x{}'.format(WIDTH, HEIGHT))
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tkinter.Label(fenetre, image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

#open and upload text files ############################################################
def open_file():
    fenetre.fileName= filedialog.askopenfilename(filetypes=(("PDF files","*.pdf"),("DOC files","*.docx"),("Text files","*.txt")))

def uploadFiles():
    pb1 = Progressbar(
        fenetre,
        orient=HORIZONTAL,
        length=300,
        mode='determinate'
    )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        fenetre.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(fenetre, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

adhar = Label(
    fenetre,
    text='Upload text file '
)
adhar.grid(row=0, column=0, padx=10)

adharbtn = Button(
    fenetre,
    text='Choose File',
    command=lambda: open_file()
)
adharbtn.grid(row=0, column=1)

ms = Label(
    fenetre,
    text='Upload PDF files '
)
ms.grid(row=2, column=0, padx=10)

msbtn = Button(
    fenetre,
    text='Choose File',
    command=lambda: open_file()
)
msbtn.grid(row=2, column=1)
#aalech upld ma aand'hech label ?
upld = Button(
    fenetre,
    text='Upload Files',
    command=uploadFiles
)
upld.grid(row=3, columnspan=3, pady=10)

#save file button #########################################################################
def enregister_sous():
    f = tkinter.filedialog.asksaveasfile(
        title="Enregistrer sous ... un fichier",
        filetypes=[('Audio files', '*.wav')])
menufichier.add_command(label="Enregistrer sous",command=enregister_sous)
menufichier.add_command(label="Quitter", command=fenetre.destroy)



r=sr.Recognizer()
#translator=google_translator()
translator = Translator()



# record audio #############################################################################
chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
frames = []

def startrecording():

        b = pyaudio.PyAudio()
        stream = b.open(format=sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
        isrecording = True

        print('Recording')
        t = threading.Thread(target=record)
        t.start()
def stoprecording():
        isrecording = False
        print('recording complete')
        filename='test1'
        filename = filename+".wav"
        #self.filename = asksaveasfile(initialdir = "/",title = "Save as",mode='w',filetypes = (("audio file","*.wav"),("all files","*.*")),defaultextension=".wav")

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(b.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        main.destroy()
def record():
       while isrecording:
            data = stream.read(chunk)
            frames.append(data)

sound_btn = Button(fenetre, text='start Recording', width=20,command=startrecording )
sound_btn.grid(row=5, column=1)
stop_btn = Button(fenetre, text='stop Recording', width=20,command=stoprecording )
stop_btn.grid(row=5, column=2)

# Affichage de la fenêtre créée #########################################################
fenetre.mainloop()
