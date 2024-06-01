import threading

from tkinter import Tk, Button, Label, BOTTOM
from PIL import Image, ImageTk
from WAVE_Process import CreateWave
from WAVE_Process import AudioFile
from ChatGPT import GPT
from Voicevox import Voice
class menu:
    def __init__(self, Whisper, GPT):
        self.Whisper_API = Whisper
        self.GPT_API = GPT
        return None

    def Button_Talk(self):

        x = CreateWave(self.Whisper_API)
        x.Record()
        x.SaveWaveFile()
        Text = x.SendToWhisper()

        y = GPT(Text, self.GPT_API)
        Text = y.Input()

        z = Voice(Text[1])
        z.POST()

        a = AudioFile("output.wav")
        a.play()


    def start(self):
        root = Tk()
        root.title('AI Maid')
        root.geometry('256x300')
        root.iconbitmap('superaxin.ico')
        root.resizable(False, False)

        button = Button(root, text="Hold To Talk")
        button.pack(side=BOTTOM)
        button.bind('<ButtonPress-1>', lambda x: threading.Thread(target=self.Button_Talk).start())

        img = ImageTk.PhotoImage(Image.open('Girl_opa.png'))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        root.mainloop()
