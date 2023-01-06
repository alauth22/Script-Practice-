#01.05.23_AQL
#tkinter_simple_calculator 

from tkinter import * #import everything 
#everything in tk is considered a widget.

root = Tk()
root.title("Simple Calculator") #want the calculator labeled

#entry widget 
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #delete what's already in the box 0 = beginning, END = go to very end. 
    # entry.delete(0, END)
    current_num = entry.get() #this just creates the variable!!
    #aka clear the textbox 
    entry.delete(0, END) #needs to delete what's already in there first before adding new number. 
    entry.insert(0, str(current_num) + str(number))

def button_clear_f():
    entry.delete(0, END)

def button_equal_f():
    #declaring variable to grab the variable sitting in the textbox. 
    second_num = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, global_num + int(second_num))
    elif math == "subtraction":
        entry.insert(0, global_num - int(second_num))
    elif math == "multiplication":
        entry.insert(0, global_num * int(second_num))
    else:
        entry.insert(0, global_num / int(second_num))
   

def button_add():
    first_num = entry.get() #grab the first 
    #need to make it global 
    global global_num 
    global math 
    math = "addition"
    global_num = int(first_num) #ensure global num is int 
    #clear textbox 
    entry.delete(0, END)

def button_subtract_f():
    first_num = entry.get() #grab the first 
    #need to make it global 
    global global_num 
    global math 
    math = "subtraction"
    global_num = int(first_num) #ensure global num is int 
    #clear textbox 
    entry.delete(0, END)

def button_multiply_f():
    first_num = entry.get() #grab the first 
    #need to make it global 
    global global_num 
    global math 
    math = "multiplication"
    global_num = int(first_num) #ensure global num is int 
    #clear textbox 
    entry.delete(0, END)

def button_divide_f():
    first_num = entry.get() #grab the first 
    #need to make it global 
    global global_num 
    global math 
    math = "division"
    global_num = int(first_num) #ensure global num is int 
    #clear textbox 
    entry.delete(0, END)


#define button variables, only use lambda if you need to pass variables. 
button_1 = Button(root, text = "1",padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(root, text = "2",padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root, text = "3",padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root, text = "4",padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root, text = "5",padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root, text = "6",padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root, text = "7",padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root, text = "8",padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root, text = "9",padx=40, pady=20, command = lambda: button_click(9))
button_0 = Button(root, text = "0",padx=40, pady=20, command = lambda: button_click(0))

#don't need to use lambda since I'm not passing any variable. I grab variable in function 
button_addition = Button(root, text = "+",padx=39, pady=20, command = button_add)
button_equal = Button(root, text = "=",padx=101, pady=20, command = button_equal_f)
button_clear = Button(root, text = "CLEAR",padx=79, pady=20, command = button_clear_f)

button_subtract = Button(root, text = "-",padx=41, pady=20, command = button_subtract_f)
button_multiply = Button(root, text = "*",padx=40, pady=20, command = button_multiply_f)
button_divide = Button(root, text = "/",padx=41, pady=20, command = button_divide_f)

#display buttons on screen 
#goes from top to bottom with highest starting 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0) 
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

#the odd buttons 
button_0.grid(row=4, column=0)
button_addition.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()  