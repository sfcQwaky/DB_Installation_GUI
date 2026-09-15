from tkinter import *
from tkinter import ttk

#   Definition of global variables  #
FONT_1 = "Ariel"
FONT_2 = "Helvetica"
STEP_COUNT = 0

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

#-----------------------------#
#   Frame 1 setup   #

frame = Frame(window)
frame.place(relx=0.5,rely=0.4,anchor="center")
frame.configure(background="#D3D3D3")

#------     FUNCTIONS   ------#
def next_button():
    global STEP_COUNT

    if STEP_COUNT == 0:
        welcome_label.grid_remove()
        db_label.grid()
        db_select.grid()
        previous_btn.grid()
    elif STEP_COUNT == 1:
        print(db_select.get())
        db_label.config(text="Enter name of your database:")
        db_select.grid_remove()
        db_name.grid()

    STEP_COUNT += 1

def previous_button():
    global STEP_COUNT

    if STEP_COUNT == 2:
        pass

    STEP_COUNT -= 1

def db_creation():
    global STEP_COUNT

    print("Here is where we create db")

#-----------------------------#

#   GUI elements    #
#TODO: global grid should have 4 rows and 4 columns

    #welcome message
welcome_label = Label(frame, text="Welcome to \"Installation of test database\" !!!", font=(FONT_2,12,"italic"), bg="#D3D3D3")
welcome_label.grid(row=0, column=0, columnspan=4, pady=10)

    #button next
next_btn = Button(frame, text="Next", width=10, command=next_button)
next_btn.grid(row=1, column=3)

    #button previous
previous_btn = Button(frame, text="Previous", width=10, command=next_button)
previous_btn.grid(row=1, column=1, padx=10)
previous_btn.grid_remove()      #initial hidden

    #database label element that changes on every STEP
db_label = Label(frame, text="Select type of database", bg="#D3D3D3")
db_label.grid(row=0, column=0, columnspan=2, pady=10)
db_label.grid_remove()

    #database selection menu/combobox
db_select = ttk.Combobox(frame, values = ["SQLite","PostgreSQL","MongoDB"])
db_select.grid(row=0, column=3, pady=10)
db_select.grid_remove()

    #database name entry
db_name= Entry(frame, width=20)
db_name.grid(row=0, column=3, pady=10)
db_name.grid_remove()





window.mainloop()