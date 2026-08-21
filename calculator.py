import tkinter as tk

def press(num):
    entry.insert(tk.END, str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# main window
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text,r,c) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        b = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t))
    b.grid(row=r, column=c)

clear_btn = tk.Button(root, text="C", width=5, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
