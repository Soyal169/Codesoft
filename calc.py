import tkinter as tk

# Function to update the input field when a button is pressed
def button_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

# Function to clear the input field
def button_clear():
    input_text.set("")

# Function to delete the last character from the input field
def button_backspace():
    current = input_text.get()
    input_text.set(current[:-1])

# Function to evaluate the expression in the input field
def button_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except Exception as e:
        input_text.set("Error")

# Setting up the main application window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("500x500")
root.resizable(0, 0)
root.config(bg="#e0f7fa")

# Input field to display the current expression and result
input_text = tk.StringVar()
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=("Arial", 18, "bold"), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for the buttons
buttons_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
buttons_frame.pack()

# Button layout
button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#00796b",
    "fg": "#ffffff",
    "bd": 0,
    "width": 10,
    "height": 3
}

# First row
clear_button = tk.Button(buttons_frame, text="C", command=button_clear, **button_style)
clear_button.grid(row=0, column=0, padx=1, pady=1)
backspace_button = tk.Button(buttons_frame, text="⌫", command=button_backspace, **button_style)
backspace_button.grid(row=0, column=1, padx=1, pady=1)
divide_button = tk.Button(buttons_frame, text="/", command=lambda: button_click("/"), **button_style)
divide_button.grid(row=0, column=2, padx=1, pady=1)
multiply_button = tk.Button(buttons_frame, text="*", command=lambda: button_click("*"), **button_style)
multiply_button.grid(row=0, column=3, padx=1, pady=1)

# Second row
seven_button = tk.Button(buttons_frame, text="7", command=lambda: button_click("7"), **button_style)
seven_button.grid(row=1, column=0, padx=1, pady=1)
eight_button = tk.Button(buttons_frame, text="8", command=lambda: button_click("8"), **button_style)
eight_button.grid(row=1, column=1, padx=1, pady=1)
nine_button = tk.Button(buttons_frame, text="9", command=lambda: button_click("9"), **button_style)
nine_button.grid(row=1, column=2, padx=1, pady=1)
subtract_button = tk.Button(buttons_frame, text="-", command=lambda: button_click("-"), **button_style)
subtract_button.grid(row=1, column=3, padx=1, pady=1)

# Third row
four_button = tk.Button(buttons_frame, text="4", command=lambda: button_click("4"), **button_style)
four_button.grid(row=2, column=0, padx=1, pady=1)
five_button = tk.Button(buttons_frame, text="5", command=lambda: button_click("5"), **button_style)
five_button.grid(row=2, column=1, padx=1, pady=1)
six_button = tk.Button(buttons_frame, text="6", command=lambda: button_click("6"), **button_style)
six_button.grid(row=2, column=2, padx=1, pady=1)
add_button = tk.Button(buttons_frame, text="+", command=lambda: button_click("+"), **button_style)
add_button.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
one_button = tk.Button(buttons_frame, text="1", command=lambda: button_click("1"), **button_style)
one_button.grid(row=3, column=0, padx=1, pady=1)
two_button = tk.Button(buttons_frame, text="2", command=lambda: button_click("2"), **button_style)
two_button.grid(row=3, column=1, padx=1, pady=1)
three_button = tk.Button(buttons_frame, text="3", command=lambda: button_click("3"), **button_style)
three_button.grid(row=3, column=2, padx=1, pady=1)
equal_button = tk.Button(buttons_frame, text="=", command=button_equal, **button_style)
equal_button.grid(row=3, column=3, rowspan=2, padx=1, pady=1)

# Fifth row
zero_button = tk.Button(buttons_frame, text="0", command=lambda: button_click("0"), **button_style)
zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
decimal_button = tk.Button(buttons_frame, text=".", command=lambda: button_click("."), **button_style)
decimal_button.grid(row=4, column=2, padx=1, pady=1)

# Start the Tkinter event loop
root.mainloop()
