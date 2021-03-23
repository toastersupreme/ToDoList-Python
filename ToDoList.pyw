# Author: Willem Vidler
# Date: December 7th, 2020
# Program Name: To Do List
# Program Description: Program that displays a list of tasks, the user can add/remove tasks

from tkinter import *   # Imports the tkinter module
from tkinter.ttk import *   # Replace the tk widgets with ttk ones
from tkinter import messagebox  # Used for the pop-ups

def removeSelectedClick():
    """
    Removes the selected task from the to do list
    """
    # Nothing Selected
    if not listbox.curselection(): # No index selected
        messagebox.showwarning("Warning!", "No task selected!") # Pop up
        return # Stop the function here

    # Get the selected task's text
    selection = listbox.selection_get()
    taskList.remove(selection) # Removes the 1st occurance of the string from the list
    listboxItems.set(taskList) # update the GUI

def addTaskClick():
    """
    Adds a new task to the to do list
    """
    # Get the entry's text
    newTask = addTaskText.get()

    # Nothing to add
    if newTask == "":
        messagebox.showwarning("Warning!", "Please enter a task!") # Pop-up
        return # Stop the function here

    # Update the list
    taskList.append(newTask) # Add the new task to the list
    listboxItems.set(taskList) # Update the GUI
    addTaskText.set("") # Reset the entry's text

def keyHandler(event:Event):
    """
    Handles key presses
    - [Enter] to add
    - [Del] to remove
    """
    if event.keysym ==  "Return": # Enter key
        addTaskClick()
    elif event.keysym == "Delete": # Delete Key
        removeSelectedClick()

# Window properties
tk = Tk() # tk object
tk.title ("To Do List - Willem Vidler")
tk.minsize(width=400, height=400)
tk.bind("<Key>", keyHandler) # Binds key presses to the keyHandler 


# Frames
listFrame = Frame() # 
buttonsFrame = Frame()

# Banner Label
bannerLabel = Label(listFrame, text="Task List", font="44") 

# Listbox
taskList = ["Task 1", "Task 2"] # The list hold all the tasks
listboxItems = StringVar() # The tkinter string variable
listboxItems.set(taskList)  # Initial value
listbox = Listbox(listFrame, listvariable=listboxItems)

# New task entry
addTaskText = StringVar()
addTaskEntry = Entry(buttonsFrame, textvariable=addTaskText)

# Buttons
addButton = Button(buttonsFrame, text="Add New Task", command=addTaskClick)
removeButton = Button(buttonsFrame, text="Remove Selected Task", command=removeSelectedClick)

# Position the widgets in the window
# List Frame
listFrame.pack(padx=10, pady=(10,5), expand=True, fill="both") # Grow hori and verti
bannerLabel.pack()
listbox.pack(expand=True, fill="both") # Grow hori and verti
# Buttons Frame
buttonsFrame.pack(padx=10, pady=(5,10), side="bottom", fill="x") # Grow along x axis
addTaskEntry.pack(side="left", expand=True, fill="x" ) # Grow along x axis
addButton.pack(side="left")
removeButton.pack(side="left")

# Start the GUI
tk.mainloop() # Don't forget the ()