from helper import D

from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter.ttk import Frame, Label, Style
from img import pic_chooser
import requests
from pprint import pprint
import datetime
from weather import weather_reporter

class GUI(Frame):

    def __init__(self):
        super().__init__()
        
        self.D = D
        self.pic_chooser = pic_chooser
        self.weather_reporter = weather_reporter
        
        self.initUI()

    def initUI(self):

        self.master.title("OIKIA TESTING")
        self.pack(fill=BOTH, expand=1)
        
        # general
        Style().configure("TFrame", background="#333")
        
        ### text
        canvas = Canvas(self)
        
        # main title
        canvas.create_text(
            250,
            10,
            anchor=W,
            font="Arial",
            text=datetime.datetime.now(),
            fill='#000000'
        )
           
        # weather table   
        weather_data = self.weather_reporter(D=self.D)
        weather_text = '\n'.join(' '.join(map(str,sl)) for sl in weather_data)
        
        canvas.create_text(
            200,
            300,
            anchor=W,
            font="Arial",
            text=weather_text,
            fill='#ff0000'
        )
        
        canvas.pack(fill=BOTH, expand=1)
        
        # img
        chosen_pic = Image.open(self.pic_chooser())
        display_pic = chosen_pic.resize((100, 100), Image.ANTIALIAS) 
        display_pic = ImageTk.PhotoImage(display_pic)
        label1 = Label(self, image=display_pic)
        label1.image = display_pic
        label1.place(x=20, y=20)

def main():

    root = Tk()
    root.geometry("500x500")
    app = GUI()
    root.mainloop()

if __name__ == '__main__':
    
    main()