from tkinter import *
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


WIDTH = 640
HEIGHT = 400

window = Tk()

POS_X = window.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = window.winfo_screenheight() // 2 - HEIGHT // 2

window["bg"] = "yellow3"

window.resizable(width=False, height=False)

window.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

window.title('Pogoda')


def owm():
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('8e524655deb30fa1ccd858539dfd3268', config_dict)
    cityp = f'{city.get()}'
    place = f'{city.get()}'
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    poster.configure(text=f'Температура в городе {cityp}: {temp}', bg='Green')


poster = Label(text=' ', font=('Arial', 20), bg="yellow3")
poster.place(x=50, y=150)

invite = Label(text='Впишите город', font=('Arial', 20), bg='forest green')
invite.place(x=50, y=90)

city = Entry(width=15, bg='olive drab', font=('Times New Roman', 14))
city.place(x=250, y=100)

enter = Button(text='Enter', font=('Arial', 10), command=owm, bg='olive drab')
enter.place(x=391, y=96)

window.mainloop()
