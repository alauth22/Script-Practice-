from tkinter import * #import everything 
#everything in tk is considered a widget.
#FIRST THING: root widget = window
root = Tk()

#create a function for the button to complete. 
def myClick():
    myLabel = Label(root, text = "Look! I clicked the Button!")
    myLabel.pack()

#create your widget; call the function to run it. NO (), you're only passing the function, NOT calling. 
mybutton = Button(root, text = "Click Me", padx=5, pady=5, command = myClick, fg="red")
#pack your widget into a grid 
mybutton.pack(padx=10, pady=10)

#run your code 
root.mainloop()