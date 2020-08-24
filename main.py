from generators import generate, setup
import tkinter as tk
import tkinter.font as tkFont

class App:

    def __init__(self, root):
        #setting title
        root.title("A Simple Plot Generator")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.configure(background='#22577a')
        root.resizable(width=False, height=False)

        self.GLabel_544=tk.Label(root)
        self.GLabel_544["bg"] = "#80ed99"
        ft = tkFont.Font(family='Times',size=30)
        self.GLabel_544["font"] = ft
        self.GLabel_544["fg"] = "#22577a"
        self.GLabel_544["justify"] = "center"
        self.GLabel_544["wraplength"] = 512
        self.GLabel_544["text"] = ""
        self.GLabel_544.place(x=20,y=20,width=550,height=300)

        GButton_483=tk.Button(root)
        GButton_483["bg"] = "#38a3a5"
        ft = tkFont.Font(family='Times',size=30)
        GButton_483["font"] = ft
        GButton_483["fg"] = "#22577a"
        GButton_483["justify"] = "center"
        GButton_483["text"] = "Generate Story"
        GButton_483.place(x=70,y=350,width=460,height=87)
        GButton_483["command"] = self.GButton_483_command

    def GButton_483_command(self):
        self.GLabel_544["text"] = generate()

if __name__ == "__main__":
    setup()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
