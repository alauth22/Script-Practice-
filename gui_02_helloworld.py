from tkinter import * #import everything 
#everything in tk is considered a widget.
#FIRST THING: root widget = window

root = Tk()
#created our label widget 
mylabel = Label(root, text = "Hello World!")
#packing your label widget into your root widget or main window 
mylabel.pack(padx=10, pady=10)

#tells python to run the Tkinter loop over and over again. 
root.mainloop()