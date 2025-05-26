import math
import tkinter as tk
from tkinter import StringVar


def press(key):
    current_expression = equation.get()
    equation.set(current_expression + str(key))


def clear():
    equation.set("")


def equal():
    try:
        expression = equation.get()
        expression = expression.replace("^", "**")
        result = eval(expression)
        if isinstance(result, float):
            result = "{:.2f}".format(result)
        equation.set(result)
    except (ZeroDivisionError, ValueError, SyntaxError) as e:
        equation.set(f"Error: {e}.")
    except Exception as e:
        equation.set(f"Error: {e}")


def square_root():
    try:
        expression = equation.get()
        value = float(expression)
        if value < 0:
            equation.set("Error: Negative number")
        else:
            result = math.sqrt(value)
            result = "{:.2f}".format(result)
            equation.set(str(result))
    except ValueError:
        equation.set("Error: Invalid input")


def backspace():
    current_expression = equation.get()
    equation.set(current_expression[:-1])


def toggle_theme():
    """Changes the color of the interface"""
    if window["bg"] == "#535753":
        window.configure(bg="#1d1f1d")
        for button in buttons_list:
            button.configure(bg="#2E2E2E", fg="#FFFFFF")
        expression_field.configure(bg="#1d1f1d", fg="#FFFFFF")
    else:
        window.configure(bg="#535753")
        for button in buttons_list:
            button.configure(bg="#4CAF50", fg="#000000")
        expression_field.configure(bg="white", fg="#000000")


window = tk.Tk()
window.configure(bg="#535753")
window.option_add("*font", "arial 18")
window.geometry("374x418")
window.title("Advanced Calculator")

equation = StringVar()
expression_field = tk.Entry(window, textvariable=equation, justify='right',
                            bd=10, font=("Arial", 20))
expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

buttons_config = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("0", 4, 0), ("=", 4, 1), (".", 4, 2), ("/", 4, 3),
    ("Clear", 5, 0), ("^", 5, 1), ("√", 5, 2), ("Theme", 6, 0), ("Exit", 7, 3),
    ("Back", 5, 3)
]

buttons_list = []

for (text, row, col) in buttons_config:
    if text == "Clear":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=clear, height=1, width=6)
    elif text == "=":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=equal, height=1, width=6)
    elif text == "Theme":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=toggle_theme, height=1, width=6)
    elif text == "√":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=square_root, height=1, width=6)
    elif text == "Exit":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=window.destroy, height=1, width=6)
    elif text == "Back":
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=backspace, height=1, width=6)
    else:
        button = tk.Button(window, text=text, fg="black", bg="#4CAF50",
                           command=lambda t=text: press(t), height=1, width=6)

    button.grid(row=row, column=col)
    buttons_list.append(button)


if __name__ == "__main__":
    window.mainloop()
