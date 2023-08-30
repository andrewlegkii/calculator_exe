import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Ошибка")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Калькулятор")

screen = tk.StringVar()
screen.set("")

entry = tk.Entry(root, textvar=screen, font="Helvetica 24 bold")
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, font="Helvetica 20", relief="ridge", borderwidth=3)
    button.grid(row=row, column=col, padx=10, pady=10)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
