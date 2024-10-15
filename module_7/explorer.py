import tkinter
from tkinter import filedialog
import os


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] += filename
    os.startfile(filename)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл: ', height=5, width=50, background='white')
text.grid(columns=1, row=1)
button_select = tkinter.Button(window, height=3, width=20, text='Выберите файл', foreground='yellow',
                               background='blue', command=file_select)
button_select.grid(columns=1, row=2, pady=5)

window.mainloop()
