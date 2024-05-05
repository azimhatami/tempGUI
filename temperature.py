# Import the tkinter library for creating graphical user interfaces
import tkinter as tk
# Import ttk widgets from tkinter for a more consistent look and feel (optional)
from tkinter import ttk


# Create the main window of the temperature converter application
window = tk.Tk()

# Set the title displayed on the window's title bar
window.title('temprature app')

# Create a string variable to store the user's Fahrenheit input
fahrenheit_val = tk.StringVar()

# Create a label to display instructions or conversion results
lbl_result = ttk.Label(
    master=window, # Specify the label belongs to the main window
    text='Enter your number...', # Initial display text
)


def convert_fahrenheit_to_celsius(*args):
    """
    This function handles conversion and displays the Celsius equivalent.

    *args allows for handling potential future event arguments.
    """
    # Get the user's input value from the StringVar
    fahrenheit_input = fahrenheit_val.get()
    try:
        # Convert the input to a float for numerical operations
        fahrenheit_value = float(fahrenheit_input)

        # Calculate Celsius using the conversion formula
        lbl_result['text'] = (fahrenheit_value - 32) * 5 / 9

    except ValueError:
        if fahrenheit_input != '':
            # Handle invalid input (non-numeric characters)
            lbl_result['text'] = 'You should enter a number.'
        else:
            # Handle empty input
            lbl_result['text'] = 'Your input is empty.'

# Bind the Enter key press to the conversion function
window.bind('<Return>', convert_fahrenheit_to_celsius)

# Create a label for the Fahrenheit temperature (using ttk.Label)
lbl_fahrenheit = ttk.Label(
    master=window,
    text='Fahrenheit:',
)

# Create an entry widget for the user to input the Fahrenheit value
ent_fahrenheit = ttk.Entry(
    master=window,
    width=50,
    textvariable=fahrenheit_val,
)

# Create a button to trigger the conversion function
btn_calc = ttk.Button(
    master=window,
    text='Calc',
    command=convert_fahrenheit_to_celsius,
)

# Arrange the widgets on a grid layout manager
# Label for Fahrenheit
lbl_fahrenheit.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
) # Padded positioning

# Entry field and button for Fahrenheit input and conversion
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2)

# Label for Celsius
lbl_celsius = ttk.Label(
    master=window,
    text='Celsius:',
)

# Label for result
lbl_result = ttk.Label(
    master=window,
    text='Enter your number...',
)

lbl_celsius.grid(row=1, column=0, pady=(10, 20))
# Label for displaying the conversion result
lbl_result.grid(row=1, column=1, pady=(10, 20))

# Start the main event loop to keep the application running
window.mainloop()
