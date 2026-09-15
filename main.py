from tkinter import *


#Initial GUI setup
window = Tk()
window.title("Install your local friendly database")

#calculation of position for my GUI, making it central position
width = 400
height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
y = int(round(y*0.8,0))     #I do not want that height of window is 100% center, so this is placing it little more to top


window.geometry(f"{width}x{height}+{x}+{y}")
window.configure(background="#D3D3D3") #this is light gray color, optional: E0E0E0, EEEEEE

#-------------------------------------#






window.mainloop()