import tkinter
from tkinter import *
from tkinter import ttk
from db_setup import sqlite_db_creation, postgresql_db_creation


#   Definition of global variables  #
FONT_1 = "Ariel"
FONT_2 = "Helvetica"
STEP_COUNT = 0
DB_TYPE = ""
CR_DB_NAME = ""  #Created database name
DB_USER_VL = ""
DB_PASS_VL = ""

#Initial GUI setup
window = Tk()
window.title("Install your local friendly database")
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=4)
window.grid_rowconfigure(0, weight=1)

#calculation of position for my GUI, making it central position
width = 500
height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
y = int(round(y*0.8,0))     #I do not want that height of window is 100% center, so this is placing it little more to top


window.geometry(f"{width}x{height}+{x}+{y}")
window.configure(background="#E0E0E0") #this is light gray color, optional: E0E0E0, EEEEEE

#------     FRAME DEFINITIONS AND SETUP   ------#

left_frame = tkinter.Frame(window, bg="#E0E0E0", width=100, height=300)
right_frame = tkinter.Frame(window, bg="#E0E0E0", width=400, height=300)
bottom_frame = tkinter.Frame(window, bg="#E0E0E0", width=500, height=100)

left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
bottom_frame.grid_columnconfigure(0, weight=1)

left_frame.grid_propagate(False)
right_frame.grid_propagate(False)
bottom_frame.grid_propagate(False)

content_frame = Frame(right_frame, bg="#E0E0E0")
content_frame.place(relx=0.5, rely=0.4, anchor="center")

#------     FUNCTIONS   ------#

def step_0():               # Welcome screen
    welcome_label.grid()
    db_label.grid_remove()
    db_select.grid_remove()
    previous_btn.grid_remove()


def step_1():               # Step for selecting type of database
    welcome_label.grid_remove()
    db_label.grid()
    db_select.grid()
    previous_btn.grid()
    db_name.grid_remove()
    db_user.grid_remove()
    db_password.grid_remove()
    db_user_label.grid_remove()
    db_password_label.grid_remove()

def step_2():               # Step for entering name of database
    db_label.config(text="Enter name of your database:")
    db_select.grid_remove()
    db_name.grid()
    if DB_TYPE == "PostgreSQL":
        db_user_label.grid()
        db_user.grid()
        db_password_label.grid()
        db_password.grid()


def step_3():               # Step which runs installation

    db_name.grid_remove()
    next_btn.grid_remove()
    previous_btn.grid_remove()
    db_user_label.grid_remove()
    db_user.grid_remove()
    db_password_label.grid_remove()
    db_password.grid_remove()
    db_label.config(text="Installation is running...")
    db_label.grid(row=0, column=0, columnspan=3, pady=10)

    window.after(2000, db_installation)     #delay of 2 seconds for running the query

def finish_button():               # Closing the installation window
    window.destroy()

#function for button Next
def next_button():
    global STEP_COUNT
    global DB_TYPE
    global CR_DB_NAME
    global DB_USER_VL
    global DB_PASS_VL

    if STEP_COUNT == 0:
        step_1()

    elif STEP_COUNT == 1:
        DB_TYPE = db_select.get()       #value which db was selected is stored in global variable
        step_2()

    elif STEP_COUNT == 2:
        CR_DB_NAME = db_name.get()
        if DB_TYPE == "PostgreSQL":
            DB_USER_VL = db_user.get()
            DB_PASS_VL = db_password.get()
        step_3()

    STEP_COUNT += 1         #after every click on NEXT button, STEP count goes up

#function for button Previous
def previous_button():          # only on steps 1 and 2 there is previous button
    global STEP_COUNT

    if STEP_COUNT == 1:
        step_0()
    elif STEP_COUNT == 2:
        step_1()

    STEP_COUNT -= 1

# DB installation function
def db_installation():
    global DB_TYPE
    global CR_DB_NAME
    message = ""
    if DB_TYPE == "SQLite":
        message = sqlite_db_creation(CR_DB_NAME)
    elif DB_TYPE == "PostgreSQL":
        message = postgresql_db_creation(db_name=CR_DB_NAME,db_user=DB_USER_VL,db_pass=DB_PASS_VL)

    db_label.config(text=f"{message}")
    finish_btn.grid()

#---------------------------------#

#------     GUI elements    ------#

    #welcome message
welcome_label = Label(content_frame, text="Welcome to \n \"Installation of test database\" !!!",
                      wraplength=350,
                      justify="center",
                      font=(FONT_2,12,"italic"),
                      bg="#E0E0E0")
welcome_label.grid(row=0, column=1, pady=10)

    #button next
next_btn = Button(bottom_frame, text="Next", width=10, command=next_button)
next_btn.grid(row=0, column=2, padx=5, pady=30)

    #button previous
previous_btn = Button(bottom_frame, text="Previous", width=10, command=previous_button)
previous_btn.grid(row=0, column=1, padx=5, pady=30)
previous_btn.grid_remove()      #initial hidden

    #button finish
finish_btn = Button(bottom_frame, text="Finish", width=10, command=finish_button)
finish_btn.grid(row=0, column=2, padx=5, pady=30)
finish_btn.grid_remove()        #initial hidden

    #database label element that changes on almost every STEP
db_label = Label(content_frame, text="Select type of database", bg="#E0E0E0")
db_label.grid(row=0, column=0, columnspan=2, pady=10)
db_label.grid_remove()

    #database selection menu/combobox
db_select = ttk.Combobox(content_frame, values = ["SQLite","PostgreSQL"])
db_select.grid(row=0, column=2, pady=10)
db_select.grid_remove()

    #database name entry
db_name= Entry(content_frame, width=20)
db_name.grid(row=0, column=2, pady=10)
db_name.grid_remove()

    #database user
db_user = Entry(content_frame, width=20)
db_user.grid(row=1, column=2, pady=10)
db_user.grid_remove()

    #database password
db_password = Entry(content_frame, width=20)
db_password.grid(row=2, column=2, pady=10)
db_password.grid_remove()

    #database user label
db_user_label = Label(content_frame, text="Enter username:", bg="#E0E0E0")
db_user_label.grid(row=1, column=0, columnspan=2, pady=10)
db_user_label.grid_remove()

    #database password
db_password_label = Label(content_frame, text="Enter password:", bg="#E0E0E0")
db_password_label.grid(row=2, column=0, columnspan=2, pady=10)
db_password_label.grid_remove()


#------     END OF GUI    ------#

window.mainloop()