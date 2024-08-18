from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


class BasicMenu(ttk.Frame):
    def __init__(self, root):
        self.filename = ''
        
        root.title('Guest JSON File Generator')
        root.tk.call('tk', 'windowingsystem')     # returns x11, win32 or aqua
        root.option_add('*tearOff', False)

        # create a menubar
        menubar = Menu(root)
        root.config(menu=menubar)

        # create a menu
        file_menu = Menu(menubar)

        # creat an about menu
        help_menu = Menu(menubar)

        # Add menu items to the file menu
        file_menu.add_command(
            label='Open',
            command=self.select_file
        )

        file_menu.add_command(
            label='Save',
            command=self.destroy
        )

        file_menu.add_command(
            label='Exit',
            command=root.destroy
        )

        # add the File menu to the menubar
        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        # Add a menu item to the help menu        
        help_menu.add_command(
            label='About',
            command=root.destroy
        )

        # add the Help menu to the menubar
        menubar.add_cascade(
            label="Help",
            menu=help_menu
        )
        

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.filename = StringVar()
        fileName = ttk.Entry(mainframe, width=100, textvariable=self.filename)
        fileName.grid(column=2, row=1, sticky=(W, E))
        
        self.sheetName = StringVar()
        sheetName = ttk.Entry(mainframe, width=100, textvariable=self.sheetName)
        sheetName.grid(column=2, row=2, sticky=(W, E))
        
        self.userName = StringVar()    
        userName = ttk.Entry(mainframe, width=20, textvariable=self.userName)
        userName.grid(column=2, row=3, sticky=(W, E))
        
        self.password = StringVar()
        password = ttk.Entry(mainframe, width=20, textvariable=self.password)
        password.grid(column=2, row=4, sticky=(W, E))
                
        self.meters = StringVar()
        ttk.Label(mainframe, text="Guest Spreadsheet URL or File Name:").grid(column=1, row=1, sticky=S)
        ttk.Label(mainframe, text="Sheet name:").grid(column=1, row=2, sticky=S)
        ttk.Label(mainframe, text="Username for URL:").grid(column=1, row=3, sticky=S)        
        ttk.Label(mainframe, text="Password URL:").grid(column=1, row=4, sticky=S)        
        ttk.Button(mainframe, text="Update", command=self.update).grid(column=5, row=10, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        fileName.focus()
        root.bind("<Return>", self.update)
        
    def update(self, *args,):
        try:
            value = self.filename.get()
            self.sheetName.set(value)
            self.userName.set(value)
            self.password.set(value)
            self.sheetName.set(value)
            
        except ValueError:
            pass

    # import tkinter as tk
    # from tkinter import filedialog as fd 

    # def callback():
    #     name= fd.askopenfilename() 
    #     print(name)
        
    # errmsg = 'Error!'
    # tk.Button(text='File Open', 
    #     command=callback).pack(fill=tk.X)
    # tk.mainloop()

    
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('All files', '*.*')
        )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        print(self.filename)

        # showinfo(
        #     title='Selected File',
        #     message=filename
        # )

    
    
if __name__ == "__main__":
    # root = Tk()
    # myApp = Calculator(root)    
    # root.mainloop()
    pass    
    root = Tk()
    myApp = BasicMenu(root)
    root.mainloop()    



# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo

# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')


# def select_file():
#     filetypes = (
#         ('Excel files', '*.xlsx'),
#         ('All files', '*.*')
#     )

#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)

#     showinfo(
#         title='Selected File',
#         message=filename
#     )


# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )

# open_button.pack(expand=True)

# # run the application
# root.mainloop()