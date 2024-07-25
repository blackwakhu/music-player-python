import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

def fun(name):
  print("Hello", name)

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!", command=lambda: fun("derrick"))
button.pack()

tk.mainloop()