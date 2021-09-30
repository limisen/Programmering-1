import tkinter as tk
from tkinter.constants import END
from tkinter.scrolledtext import *
from tkinter.filedialog import *
from tkinter.messagebox import *

nuvarandefil='no file'

def new_file():
    """ "Creates" a new file """
    global nuvarandefil
    textruta.delete(1.0, tk.END)
    nuvarandefil = 'no file'

def open_file():
    """ körs när man klickar på open """
    global nuvarandefil

    filnamn = tk.filedialog.askopenfilename(
        filetypes =(
            ('Textfiler', '*.txt'),
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
            tk.massagebox.showerror('Filfel', 'Kunde inte öppna fil')
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
            tk.massagebox.showerror('Filfel', 'Kunde inte spata fil')
        else:
            fil.close()
    else:
        saveas()

def saveas():
    global nuvarandefil

    filnamn = tk.filedialog.asksaveasfilename(
        filetypes =(
            ('Textfiler', '*.txt'),
            ('html-filer', '*.html'),
            ('Alla filer', '*.*')
        ),
        defaultextension = ".txt",
    )
    if filnamn:
            nuvarandefil = filnamn
            savefile()

root = tk.Tk()
root.title('Nootepad')
root.geometry('800x500')
root.resizable(False, False)

textruta = ScrolledText(
    root,
    wrap = tk.WORD,
    font = ("Times New Roman", 15),
    undo = True
)

textruta.pack()

main_menu = tk.Menu()
root.config(menu=main_menu)
file_menu = tk.Menu(main_menu, tearoff = False)
main_menu.add_cascade(label='File', menu = file_menu)

file_menu.add_command(label='New',      command = new_file)
file_menu.add_command(label='Open',     command = open_file)
file_menu.add_command(label='Save',     command = savefile)
file_menu.add_command(label='Save As',  command = saveas)
file_menu.add_command(label='Exit',     command=root.destroy)

root.mainloop()