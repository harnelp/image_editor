from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog

# window
class FrontEnd:
    def __init__(self, master) -> None:
        self.master = master
        
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text='Welcome to Image Editor app!').grid(
            row=0,column=1,columnspan=1
        )
        
        ttk.Label(self.frame_header, text='Upload, edit and save your images easy!').grid(
            row=1, column=1, columnspan=1
        )

root = Tk()
FrontEnd(root)
root.mainloop()