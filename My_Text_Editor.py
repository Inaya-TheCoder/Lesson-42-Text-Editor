from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

Window = Tk()
Window.title("Text Editor")
Window.geometry("400x300")
Window.rowconfigure(0, minsize = 800,weight = 1)
Window.columnconfigure(1, minsize = 800, weight= 1)

def open_file():
    '''Open a file for editing'''
    filepath = askopenfilename(
        filetypes = [('Text Files','*.txt'),('All files','*.*')]
    )
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    with open(filepath, 'r')as input_file:
        text = input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    Window.title(f"Codingal's Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [('Text Files','*.txt'),('All files','*.*')]
    )
    if not filepath:
        return
    with open(filepath, 'w')as output_file:
        text = txt_edit.get(1.0,END)
        output_file.write(text)
    Window.title(f"Codingal's Text Editor - {filepath}")

txt_edit = Text(Window)
fr_buttons = Frame(Window,relief = RAISED, bd=2)
btn_open = Button(fr_buttons, text = "Open",command = open_file)
btn_save = Button(fr_buttons, text = "Save",command = save_file)

btn_open.grid (row = 0, column = 0, sticky = 'ew', padx = 5,pady = 5)
btn_save.grid (row = 1, column = 0, sticky = 'ew', padx = 5)

fr_buttons.grid (row = 0, column = 0, sticky = 'ns')
txt_edit.grid (row = 0, column = 1, sticky = 'nsew')
Window.mainloop()