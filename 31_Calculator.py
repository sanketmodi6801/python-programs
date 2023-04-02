import tkinter as tk

base = tk.Tk()
base.title("Simple Calculator")

# Taking number input
num = tk.Entry(base, width=30, borderwidth=10)
num.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

global number1
global math
math = ""


# functions foe operations
def button_click(number):
    current_number = num.get()
    num.delete(0, tk.END)
    num.insert(0, str(current_number) + str(number))


def clear_button():
    num.delete(0, tk.END)


def add_button():
    global number1
    global math
    number1 = int(num.get())
    num.delete(0, tk.END)
    math = 1


def sub_button():
    global number1, math
    number1 = int(num.get())
    num.delete(0, tk.END)
    math = 2


def mul_button():
    global number1, math
    number1 = int(num.get())
    num.delete(0, tk.END)
    math = 3


def div_button():
    global number1, math
    number1 = int(num.get())
    num.delete(0, tk.END)
    math = 4


def equal_button():
    global number1
    number2 = int(num.get())
    num.delete(0, tk.END)

    if math == 1:
        num.insert(0, number1 + number2)

    if math == 2:
        num.insert(0, number1 - number2)

    if math == 3:
        num.insert(0, number1 * number2)

    if math == 4:
        num.insert(0, number1 / number2)


# Defining widgets
button_1 = tk.Button(base, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(base, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(base, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(base, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(base, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(base, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(base, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(base, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(base, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(base, text="0", padx=30, pady=20, command=lambda: button_click(0))
add_button = tk.Button(base, text="+", padx=30, pady=20, command=add_button)
sub_button = tk.Button(base, text="-", padx=30, pady=20, command=sub_button)
mul_button = tk.Button(base, text="*", padx=30, pady=20, command=mul_button)
div_button = tk.Button(base, text="/", padx=30, pady=20, command=div_button)
button_decimal = tk.Button(base, text=".", padx=30, pady=20, command=lambda: button_click("."))
button_clear = tk.Button(base, text="clear", padx=20, pady=20, command=clear_button)
button_equal = tk.Button(base, text="=", padx=30, pady=20, command=equal_button)
# Creating widgets

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_decimal.grid(row=4, column=1)
add_button.grid(row=5, column=1)
sub_button.grid(row=5, column=2)
mul_button.grid(row=5, column=3)
div_button.grid(row=5, column=4)

# main loop
base.mainloop()
