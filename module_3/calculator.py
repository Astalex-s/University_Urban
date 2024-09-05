import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, str(value))


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()
window.title('Calculator')
window.geometry('250x280')
window.resizable(width=False, height=False)
button_add = tk.Button(window, text='+', width=5, height=2, command=add)
button_add.place(x=10, y=200)
button_sub = tk.Button(window, text='-', width=5, height=2, command=sub)
button_sub.place(x=70, y=200)
button_mul = tk.Button(window, text='*', width=5, height=2, command=mul)
button_mul.place(x=130, y=200)
button_div = tk.Button(window, text='/', width=5, height=2, command=div)
button_div.place(x=190, y=200)
number1_entry = tk.Entry(window, width=36)
number1_entry.place(x=10, y=50)
number2_entry = tk.Entry(window, width=36)
number2_entry.place(x=10, y=100)
answer_entry = tk.Entry(window, width=36)
answer_entry.place(x=10, y=150)
number1 = tk.Label(window, text="Enter number one:")
number1.place(x=10, y=25)
number2 = tk.Label(window, text="Enter number two:")
number2.place(x=10, y=75)
answer = tk.Label(window, text="Answer: ")
answer.place(x=10, y=125)
window.mainloop()
