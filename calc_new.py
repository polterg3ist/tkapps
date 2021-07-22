from tkinter import *
import tkinter as tk
from tkinter import messagebox

WIDTH = 240
HEIGHT = 280

window = Tk()

POS_X = window.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = window.winfo_screenheight() // 2 - HEIGHT // 2

window.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
window.resizable(width=False, height=False)
window['bg'] = 'gray'
window.title('Calculator')


def delete():
    value = calc.get()
    value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert('end', value)


def add(digit):
    calc.insert('end', digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert('end', value+operation)


def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    try:
        calc.insert('end', eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Ошибка!', 'Вводите цифры.')
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка!', 'Деление на ноль невозможно')


def make_digit_button(digit):
    return Button(text=digit, bd=5, command=lambda: add(digit))


def make_operation_button(operation):
    return Button(text=operation, bd=5, command=lambda: add_operation(operation), fg='red')


def make_calc_button(operation):
    return Button(text=operation, bd=5, command=calculate, fg='red')


def make_del_button(operation):
    return Button(text=operation, bd=5, command=delete, fg='red')


def press_key(event):
    if event.char == '\r':
        calculate()


window.bind('<Key>', press_key)

calc = Entry(window, bd=5, font=('Agency FB', 20))
calc.grid(column=0, row=0, columnspan=4)

make_digit_button('1').grid(column=0, row=1, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(column=1, row=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(column=2, row=1, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(column=0, row=2, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(column=1, row=2, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(column=2, row=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(column=0, row=3, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(column=1, row=3, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(column=2, row=3, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(column=0, row=4, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(column=3, row=1, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(column=3, row=2, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(column=3, row=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(column=3, row=4, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(column=1, row=4, stick='wens', padx=5, pady=5)

make_del_button('DEL').grid(column=2, row=4, stick='wens', padx=5, pady=5)

window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)

mainloop()
