import tkinter as tk
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkinter.messagebox import *

nuvarandefil = 'no file'

root = tk.Tk()
root.title('noootpad')
root.geometry(800*400)
root.resizable(False, False)

textruta = ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Times New Roman", 15),
    undo=True
)
textruta.pack()

def new_file():
    """ Creates" a new file """
    global nuvarandefil

    textruta.delete(1.0, tk.END)
    nuvarandefil = 'no file'


def open_file():
    global nuvarandefil

    filnamn = tk.filedialog.askopenfilename(
        filetype=(
            ('Textfile', '*.txt'),
            ('html-filer', '*.html'),
            ('Alla filer', '*.*')
        )
    )
    if filnamn:
        try:
            fil = open(filnamn, 'r', encoding='utf-8')
            rader = fil.read()
            nuvarandefil = filnamn
        except:
            tk.messagebox.showerror('Filfel', 'kunde inte öppna filen')
        else:
            textruta.delete(1.0, tk.END)
            textruta.insert(1.0, rader)
        finally:
            try:
                fil.close()
            except:
                pass

def savefile():
    global nuvarandefil
    filnamn = nuvarandefil
    rader = textruta.get(1.0, tk.END)

    if filnamn != 'no file':
        try:
            fil = open(filnamn, 'w', encoding='utf-8')
            fil.write(rader)
        except:
            tk.messagebox.showerror('Filefel', 'kunde inte öppna filen')
        else:
            file.close()
    else:
        saveas()

def saveas():
    global nuvarandefil

    filnamn = tk.filedialog.asksaveasfilename(
        filetypes=(
            ('Textfile', '*.txt'),
            ('html-filer', '*.html'),
            ('Alla filer', '*.*')
        ),
        defaultextension=".txt",
    )
    if filnamn:
        nuvarandefil = filnamn
        savefile()

main_menu = tk.Menu()
root.config(menu=main_menu, tearoff=False)
main_menu.add_cascade(lable='File', menu=filen_menu)

file_menu.add_command(lable='New')
file_menu.add_command(lable='Open')
file_menu.add_command(lable='Save')
file_menu.add_command(lable='Save As')
file_menu.add_command(lable='Exit', command=root.destroy)

root.mainloop()