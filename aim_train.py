from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
import random
import time

WIDTH = 800 
HEIGHT = 600

colors = ['royal blue', 'orange', 'green', 'blue']

points = 0

window = Tk()

POS_X = window.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = window.winfo_screenheight() // 2 - HEIGHT // 2

window.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')
window.resizable(width=False, height=False)
window.title('Aim Train!')


canvas = Canvas(bg='lavender')
canvas.pack(fill=BOTH, expand=1)


def oval():
    """
    Функция для создания круга на полотне. Размер круга 
    задается случайно, для этого импортирован модуль random.
    Также здесь начинается отсчет для таймера, модуль time
    """
    global start
    canvas.delete(ALL)
    strt.destroy()
    combo.destroy()
    set.destroy()
    start = time.perf_counter()
    rx = random.randint(0, 755)
    ry = random.randint(35, 555)
    rr = random.randint(20, 50)
    circle = canvas.create_oval(rx, ry, rx+rr, ry+rr, outline="#f11", fill=random.choice(colors), width=2)
    canvas.tag_bind(circle, '<Button-1>', click)   # При нажатии на фигуру вызвется функция click()
    

def click(event):
    """
    При вызове проверяет сколько времени прошло с начала отсчета
    Если прошло больше секунды то работа остановится и вызовется функция lose().
    Иначе прибавляет 1 очко и сново вызывает функцию oval()
    """
    global points
    stop = time.perf_counter()
    lost = stop - start
    if lost > dif:
        lose()
        return
    canvas.delete(ALL)  # Полотно очищается от предыдущей фигуры
    points += 1
    oval()


def lose():
    """
    Вызывается при поражении
    Сообщает пользователю о достигнутом результате
    """
    global alert, score, restart, change
    canvas.delete(ALL)
    alert = tk.Label(text='Поражение!', font=('Arial Bold', 30), fg='brown4', bg='gray')
    score = tk.Label(text=f'Очков набрано: {points}', font=('Arial Bold', 15), bg='gray')
    restart = tk.Button(text='Рестарт', font=('Arial Bold', 30), bg='Green', command=play_again)
    change = tk.Button(text='Изменить сложность', font=('Arial Bold', 12), bg='yellow3', command=change_dif)
    alert.place(x=285, y=190)
    score.place(x=310, y=250)
    restart.place(x=307, y=290)
    change.place(x=315, y=375)
    rect = canvas.create_rectangle(275, 175, 518, 425, width=2, fill='gray')


def launch():
    global strt, combo, set
    combo = Combobox(window)
    combo['values'] = ('Easy', 'Normal', 'Hard')
    combo.current(1)
    combo.place(x=295, y=285)
    set_dif()
    set = tk.Button(text='ok', font=('Arial Bold', 10), command=set_dif)
    set.place(x=440, y=280)
    strt = tk.Button(text='START', font=('Arial Bold', 30), bg='Green', command=oval)
    strt.place(x=295, y=200)


def set_dif():
    global dif
    dif = combo.get()
    if dif == 'Easy':
        dif = 1.45
    elif dif == 'Hard':
        dif = 0.7
    else:
        dif = 0.9


def play_again():
    global points
    points = 0
    alert.destroy()
    restart.destroy()
    score.destroy()
    change.destroy()
    oval()


def change_dif():
    global points
    points = 0
    points = 0
    alert.destroy()
    restart.destroy()
    score.destroy()
    change.destroy()
    canvas.delete(ALL)
    launch()


launch()
mainloop()





