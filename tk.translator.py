from translate import Translator
from tkinter import *
from tkinter.ttk import Combobox


WIDTH = 640
HEIGHT = 400

window = Tk()

POS_X = window.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = window.winfo_screenheight() // 2 - HEIGHT // 2

window["bg"] = 'steelblue4'

window.resizable(width=False, height=False)

window.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

window.title('Переводчик!')


def get_trans():
    text_lang = set_lang.get()
    trans_lang = set_trans.get()
    text = text_trans.get(1.0, END)
    poster.delete(1.0, END)
    translator = Translator(from_lang=text_lang, to_lang=trans_lang)
    translation = translator.translate(text)
    poster.insert(1.0, f'Перевод: {translation}')


def press_key(event):
    if event.char == '\r':
        get_trans()


window.bind('<Key>', press_key)


poster = Text(font=('Arial', 15), bg="light steel blue", width=55, height=8, fg='Gray5', wrap=WORD)
poster.place(x=15, y=150)

invite = Label(text='<<= С какого языка на какой =>>', font=('Arial', 13), bg='lavender', bd=5, fg='gray15')
invite.place(x=180, y=0)

text_trans = Text(width=60, height=3, bg='olive drab', font=('Times New Roman', 15), wrap=WORD)
text_trans.place(x=15, y=50)

sl_font = ('Arial', 10)
set_lang = Combobox(window, values=[
    'russian', 'english', 'FR', 'PL'], font=sl_font, state="readonly")
set_lang.current(0)
set_lang.place(x=5, y=10)

st_font = ('Arial', 10)
set_trans = Combobox(window, values=[
    'russian', 'english', 'FR', 'PL'], font=st_font, state="readonly")
set_trans.current(1)
set_trans.place(x=458, y=10)

window.mainloop()
