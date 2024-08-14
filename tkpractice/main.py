from tkinter import *
from tkinter import ttk
import tkinter as tk





def sample1():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    # frm.
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


def main():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()




class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

        from tkinter import tix
        root = tix.Tk()
        print(root.tix_configure())
        pass

    
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())





if __name__ == "__main__":
    main()