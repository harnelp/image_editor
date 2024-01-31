from tkinter import ttk, Tk, PhotoImage, Canvas, RIDGE, GROOVE, Scale, HORIZONTAL

# window
class FrontEnd:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('750x630+250+10')
        self.master.title('Image editor')
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
#""" #################################### Header ########################################### """

        
        
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
        
        # buttons menú
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
        
        # frame Buttons actios
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        
        # Buttons menú actions, down
        ttk.Button(self.apply_and_cancel, text="apply", command=self.apply_action).grid(row=0, column=0,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(row=0, column=1,padx=5,pady=5,sticky='sw')
        
        ttk.Button(self.apply_and_cancel, text="Revert Changes", command=self.revert_action).grid(row=0, column=2,padx=5,pady=5,sticky='sw')
        
        # Canvas for image
        self.canvas = Canvas(self.frame_menu, bg="black", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)
        
    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass
        
        #self.canvas.unbind("<BottonPress>")
        #self.canvas.unbind("<B1-Motion>")
        #self.canvas.unbind("<ButtonRelease>")
        #self.display_image(self.edited_image)
        
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE,padding=(50, 15))
        
    def upload_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Please upload image").grid(row=0, column=0)
        
    def crop_action(self):
        pass
    def text_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Enter a text").grid(row=0, column=0)
    
    def draw_action(self):
        pass
    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Negative", command=self.negative_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Black And white", command=self.bw_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Stylisation", command=self.stylisation_action).grid(row=2, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=3, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Emboss", command=self.emb_action).grid(row=4, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Sepia", command=self.sepia_action).grid(row=5, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Binary Thresholding", command=self.binary_threshold_action).grid(
            row=6, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Erosion", command=self.erosion_action).grid(
            row=7, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Dilation", command=self.dilation_action).grid(
            row=8, column=2, padx=5, pady=5, sticky='sw')
            
    def blur_action(self):
        self.refresh_side_frame()

        ttk.Label(
            self.side_frame, text="Averaging Blur").grid(row=0, column=2, padx=5, sticky='sw')

        self.average_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5,  sticky='sw')

        ttk.Label(
            self.side_frame, text="Gaussian Blur").grid(row=2, column=2, padx=5, sticky='sw')

        self.gaussian_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3, column=2, padx=5,  sticky='sw')

        ttk.Label(
            self.side_frame, text="Median Blur").grid(row=4, column=2, padx=5, sticky='sw')

        self.median_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5, column=2, padx=5,  sticky='sw')
    def levels_action(self):
        pass
    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Rotate Left", command=self.rotate_left_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Rotate Right", command=self.rotate_right_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')

    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(row=1, column=2, padx=5, pady=5, sticky='sw')
    
    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        self.brightness_slider = Scale(
            self.side_frame, from_=0, to_=2,  resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5,  sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(
            self.side_frame, text="Saturation").grid(row=2, column=2, padx=5, pady=5, sticky='sw')
        self.saturation_slider = Scale(
            self.side_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL, command=self.saturation_action)
        self.saturation_slider.grid(row=3, column=2, padx=5,  sticky='sw')
        self.saturation_slider.set(0)
        
    def save_action(self):
        pass
    
    # buttoms functions
    def apply_action():
        pass
    
    def cancel_action():
        pass
    
    def revert_action():
        pass
    
    def negative_action(self):
        pass

    def bw_action(self):
        pass

    def stylisation_action(self):
        pass

    def sketch_action(self):
        pass

    def emb_action(self):
        pass

    def sepia_action(self):
        pass

    def binary_threshold_action(self):
        pass

    def erosion_action(self):
        pass

    def dilation_action(self):
        pass
    
    def averaging_action(self):
        pass

    def gaussian_action(self):
        pass

    def median_action(self):
        pass
#"""**********************************End of triggers Menu Options********************************************"""


#"""**********************************Triggers for Adjust Menu Options********************************************"""
    def brightness_action(self):
        pass

    def saturation_action(self):
        pass
#"""**********************************End of triggers for Menu Options********************************************"""
#"""*********************************Triggers for Rotate and Flip*********************************************"""
    def rotate_left_action(self):
        pass

    def rotate_right_action(self):
        pass

    def vertical_action(self):
        pass

    def horizontal_action(self):
        pass
#""" #################################### Main menu ########################################### """
#""" #################################### Footer menu ########################################### """

#""" #################################### End Footer menu ########################################### """

root = Tk()
FrontEnd(root)
root.mainloop()