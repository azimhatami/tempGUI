import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.title('temprature app')

fahrenheit_val = tk.StringVar()

lbl_result = ttk.Label(
    master=window,
    text='Enter your number...',
)


def convert_fahrenheit_to_celsius(*args):
    # user input value
    fahrenheit_input = fahrenheit_val.get()
    try:
        fahrenheit_value = float(fahrenheit_input)
        # convert to celsius
        lbl_result['text'] = (fahrenheit_value - 32) * 5 / 9
    except ValueError:
        if fahrenheit_input != '':
            # if user input is not valid
            lbl_result['text'] = 'You should enter a number.'
        else:
            # if user input is empty
            lbl_result['text'] = 'Your input is empty.'

window.bind('<Return>', convert_fahrenheit_to_celsius)

lbl_fahrenheit = ttk.Label(
    master=window,
    text='Fahrenheit:',
)

ent_fahrenheit = ttk.Entry(
    master=window,
    width=50,
    textvariable=fahrenheit_val,
)

btn_calc = ttk.Button(
    master=window,
    text='Calc',
    command=convert_fahrenheit_to_celsius,
)


lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2)

lbl_celsius = ttk.Label(
    master=window,
    text='Celsius:',
)

lbl_result = ttk.Label(
    master=window,
    text='Enter your number...',
)

lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))

window.mainloop()
