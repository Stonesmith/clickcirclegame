"""
Launcher for Circle Click Game

"""

from Tkinter import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
    
        Label(self, text = "Enter window width in pixels:").grid(row = 1, column = 0, sticky = W)
        
        self.widthEntry = Entry(self)
        self.widthEntry.grid(row = 1, column = 1)
        
        Label(self, text = "Enter window height in pixels:").grid(row = 3, column = 0, sticky = W)
        
        self.heightEntry = Entry(self)
        self.heightEntry.grid(row = 3, column = 1)
        
        Button(self, text = "Launch Game", command = self.launch).grid(row =5, column = 2, sticky = W)
        
    def launch(self):
    
        settings_file = open("settings.txt", "r+")
        settings_file.write(self.widthEntry.get())
        settings_file.write("\n")
        settings_file.write(self.heightEntry.get())

        import FinalProject
        FinalProject.game()
        
root = Tk()
root.title("Game Launcher")
root.geometry("400x400")
app = Application(root)
root.mainloop()


        
        
        