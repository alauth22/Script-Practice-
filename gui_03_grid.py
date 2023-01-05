from tkinter import * #import everything 
#everything in tk is considered a widget.
#FIRST THING: root widget = window

root = Tk()

#create your widget
mylabel_01 = Label(root, text = "Hello World!")
mylabel_02 = Label(root, text = "My name is Amelia Lauth")
mylabel_03 = Label(root, text = "hi")

#pack your widget into a grid 
#recall the space will always be relative to each other. 
#I'd rather do this to make code cleaner. Yes you can do Object-Oriented code. 
mylabel_01.grid(row=0, column=0)
mylabel_02.grid(row=1, column=2)
mylabel_03.grid(row=2, column=2)

#run your code 
root.mainloop()