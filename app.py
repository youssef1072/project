import tkinter as tk

print("Starting Calculator App...")

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")  # Increased window size

entry = tk.Entry(root, font="Arial 20", borderwidth=2, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for r, row in enumerate(buttons):
    for c, btn_text in enumerate(row):
        btn = tk.Button(btns_frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.grid(row=r, column=c, padx=5, pady=5)
        btn.bind("<Button-1>", click)
print("Buttons created and bound to click event.")
def on_closing():
    print("Calculator App closed.")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()