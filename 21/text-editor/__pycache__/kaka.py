import tkinter as tk
from tkinter.scrolledtext import *

root = tk.Tk()
root.title('noootpad')
#root.geometry(800*400)
root.resizable(False, False)
textruta = ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Times New Roman", 15),
    undo=True
)
textruta.pack()

main_menu = tk.Menu()
root.config(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As')
file_menu.add_command(label='Exit', command=root.destroy)

root.mainloop()