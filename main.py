from tkinter import *
from tkinter import ttk

#   Definition of global variables  #
FONT_1 = "Ariel"
FONT_2 = "Helvetica"
STEP_COUNT = 0
DB_TYPE = ""
CR_DB_NAME = ""  #Created database name

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

#Frame setup, used to center elements
frame = Frame(window)
frame.place(relx=0.5,rely=0.4,anchor="center")
frame.configure(background="#D3D3D3")

#------     FUNCTIONS   ------#

def step_0():
    welcome_label.grid()
    db_label.grid_remove()
    db_select.grid_remove()
    previous_btn.grid_remove()


def step_1():
    welcome_label.grid_remove()
    db_label.grid()
    db_select.grid()
    previous_btn.grid()
    db_name.grid_remove()

def step_2():
    db_label.config(text="Enter name of your database:")
    db_select.grid_remove()
    db_name.grid()

def step_3():
    db_name.grid_remove()
    next_btn.grid_remove()
    previous_btn.grid_remove()
    db_label.config(text="Installation is running...")
    db_label.grid(row=0, column=0, columnspan=3, pady=10)

#function for button Next
def next_button():
    global STEP_COUNT
    global DB_TYPE
    global CR_DB_NAME

    if STEP_COUNT == 0:
        step_1()

    elif STEP_COUNT == 1:
        DB_TYPE = db_select.get()       #value which db was selected is stored in global variable
        step_2()

    elif STEP_COUNT == 2:
        DB_NAME = db_name.get()
        step_3()

    STEP_COUNT += 1         #after every click on NEXT button, STEP count goes up

#function for button Previous
def previous_button():
    global STEP_COUNT

    if STEP_COUNT == 1:
        step_0()
    elif STEP_COUNT == 2:
        step_1()

    STEP_COUNT -= 1

def db_creation():
    global STEP_COUNT

    print("Here is where we create db")

#---------------------------------#

#------     GUI elements    ------#

    #welcome message
welcome_label = Label(frame, text="Welcome to \"Installation of test database\" !!!", font=(FONT_2,12,"italic"), bg="#D3D3D3")
welcome_label.grid(row=0, column=0, columnspan=4, pady=10)

    #button next
next_btn = Button(frame, text="Next", width=10, command=next_button)
next_btn.grid(row=1, column=3)

    #button previous
previous_btn = Button(frame, text="Previous", width=10, command=previous_button)
previous_btn.grid(row=1, column=1, padx=10)
previous_btn.grid_remove()      #initial hidden

    #database label element that changes on almost every STEP
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

#---------------------------------#


window.mainloop()