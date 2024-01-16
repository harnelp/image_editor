from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog, RIDGE

# window
class FrontEnd:
    def __init__(self, master) -> None:
        self.master = master
        
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file='img/logo.png').subsample(5,5)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        
        ttk.Label(self.frame_header, text='Welcome to Image Editor app!').grid(
            row=0,column=1,columnspan=1
        )
        
        ttk.Label(self.frame_header, text='Upload, edit and save your images easy!').grid(
            row=1, column=1, columnspan=1
        )
        
#""" #################################### End Header ########################################### """

#""" #################################### Main menu ########################################### """
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50,15))
        
        ttk.Button(self.frame_menu, text="Upload Image", command=self.upload_action).grid(row=0, column=0, padx=5,pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Crop Image", command=self.crop_action).grid(row=1, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Add Text", command=self.text_action).grid(row=2, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Draw Over Image", command=self.draw_action).grid(row=3, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Apply Filters", command=self.filter_action).grid(row=4, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Blur/Smoothening", command=self.blur_action).grid(row=5, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Adjust Levels", command=self.levels_action).grid(row=6, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Rotate", command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Flip", command=self.flip_action).grid(row=8, column=0, padx=5, pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Save as", command=self.save_action).grid(row=9, column=0, padx=5, pady=5, sticky='sw')

    def upload_action(self):
        pass
    def crop_action(self):
        pass
    def text_action(self):
        pass
    def draw_action(self):
        pass
    def filter_action(self):
        pass
    def blur_action(self):
        pass
    def levels_action(self):
        pass
    def rotate_action(self):
        pass
    def flip_action(self):
        pass
    def save_action(self):
        pass
    
#""" #################################### Main menu ########################################### """
#""" #################################### Footer menu ########################################### """

#""" #################################### End Footer menu ########################################### """

root = Tk()
FrontEnd(root)
root.mainloop()