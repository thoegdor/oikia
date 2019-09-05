from PIL import Image, ImageTk
from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter.ttk import Frame, Label, Style
from img import pic_chooser

class GUI(Frame):

    def __init__(self):
        super().__init__()

        self.pic_chooser = pic_chooser
        self.initUI()

    def initUI(self):

        self.master.title("OIKIA TESTING")
        self.pack(fill=BOTH, expand=1)
        
        # general
        Style().configure("TFrame", background="#333")
        
        # text
        canvas = Canvas(self)
        canvas.create_text(
            200,
            300,
            anchor=W,
            font="Arial",
            text="TEST TEXT",
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