from tkinter import *

from numpy import longdouble

root = Tk()
root.title("Calculator")
root.configure(bg="black")

e = Entry(root, font=("Segoe UI Black",15, "bold"), width=35, borderwidth=15, bg="black", fg="white")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky=W + E + N + S)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_remove():
    e.delete(len(e.get())-1, END)

def button_revers():
    current_text = e.get()
    if current_text:
        if current_text[0] == "-":
            e.delete(0, 1)
        else:
            e.insert(0, "-")


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = longdouble(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = longdouble(first_number)
    e.delete(0, END)
    e.insert(0, f_num ** (0.5))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = longdouble(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = longdouble(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = longdouble(first_number)
    e.delete(0, END)


def button_pow():
    first_number = e.get()
    global f_num
    global math
    math = "pow"
    f_num = longdouble(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + longdouble(second_number))
    if math == "subtraction":
        e.insert(0, f_num - longdouble(second_number))
    if math == "multiplication":
        e.insert(0, f_num * longdouble(second_number))
    if math == "division":
        e.insert(0, f_num / longdouble(second_number))
    if math == "pow":
        e.insert(0, f_num ** longdouble(second_number))

# Define the buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click(0))
button_dot = Button(root, text=".", padx=40, pady=20, bg="grey", fg="black", font=("Segoe UI Black",15, "bold"), command=lambda: button_click("."))
button_add = Button(root, text="+", padx=40, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_divide)
button_pow = Button(root, text="^", padx=40, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_pow)
button_clear = Button(root, text="Clear", padx=20, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_clear)
button_remove= Button(root, text="<🅇", padx=30, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_remove)
button_revers= Button(root, text="+/-", padx=30, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_revers)
button_sqrt= Button(root, text="√", padx=30, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_sqrt)
button_equal = Button(root, text="=", padx=91, pady=20, bg = "grey", fg = "black", font = ("Segoe UI Black",15, "bold"), command=button_equal)

# Put the buttons on the screen
button_pow.grid(row=5, column=0, sticky = W+E+N+S)
button_revers.grid(row=1, column=0, sticky = W+E+N+S)
button_clear.grid(row=1, column=2, columnspan=1, sticky = W+E+N+S)
button_remove.grid(row=1, column=3, sticky = W+E+N+S)

button_1.grid(row=2, column=0, sticky = W+E+N+S)
button_2.grid(row=2, column=1, sticky = W+E+N+S)
button_3.grid(row=2, column=2, sticky = W+E+N+S)

button_4.grid(row=3, column=0, sticky = W+E+N+S)
button_5.grid(row=3, column=1, sticky = W+E+N+S)
button_6.grid(row=3, column=2, sticky = W+E+N+S)

button_7.grid(row=4, column=0, sticky = W+E+N+S)
button_8.grid(row=4, column=1, sticky = W+E+N+S)
button_9.grid(row=4, column=2, sticky = W+E+N+S)

button_0.grid(row=5, column=1, sticky = W+E+N+S)
button_dot.grid(row=5, column=2, sticky = W+E+N+S)

button_add.grid(row=2, column=3, sticky = W+E+N+S)
button_subtract.grid(row=3, column=3, sticky = W+E+N+S)
button_multiply.grid(row=4, column=3, sticky = W+E+N+S)
button_divide.grid(row=5, column=3, sticky = W+E+N+S)
button_sqrt.grid(row=1, column=1, sticky = W+E+N+S)

button_equal.grid(row=6, column=0, columnspan=4, sticky = W+E+N+S)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=1)
root.rowconfigure(6,weight=1)

root.mainloop()
