#tutorial of GUI 
#tkinter is a library built within python to create GUI

import tkinter as tk 
from tkinter import messagebox

class myGUI:
    #in the constructor, going to have entire GUI process 
    def __init__(self):

        self.root = tk.Tk()

        #label portion here 
        self.label = tk.Label(self.root, text = "Your Message", font = ("Arial", 18))
        self.label.pack(padx=10, pady=10)

        #textbox portion here 
        self.textbox = tk.Text(self.root, height = 5, font = ("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady= 10)

        #checkbutton needs a variable to hold the checkbutton value. 
        self.check_state = tk.IntVar()
        #check portion here 
        self.check = tk.Checkbutton(self.root, text = "Show Messagebox", font = ("Arial", 16), variable = self.check_state)
        self.check.pack(padx=10, pady=10)

        #need to add the button portion
        self.button = tk.Button(self.root, text = "Show Message", font = ("Arial", 18), command = self.show_message)
        #we don't want to call the function with show_message() because we're ONLY passing show_message as a parameter. 
        self.button.pack(padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        #is the checkbox checked or not? 
        # print("Hello World!")
        # print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END)) #get funciton need to provide a start and an end. index 1 and index 2. "1.0" is to start
            #at the beginning. To go all the way at the end = tk.End
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        if event.state == 0 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        #the askyesno will be triggered if it is yes or no. 
        #if statement only triggered if we press yes. 
        if messagebox.askyesno(title="Quit?", message = "Do you really want to quit?"):
            self.root.destroy()
        
#create an object here. 
myGUI()