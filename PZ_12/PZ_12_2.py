from tkinter import *
from tkinter import messagebox, ttk


def button_clicked():
    return myEntry.get()


root = Tk()
root.title('Нахождение суммы по формуле.')
root.geometry("600x400")

frame = Frame()
frame.place(x=0, y=0)

N = IntVar()

Label(text='Нахождение суммы по формуле: 1 ** 1 + 2 ** 2 + ... N ** N.').place(in_=frame, x=5, y=2)
Label(text='Введите N:').place(in_=frame, x=5, y=25)
myEntry = Entry(width=15)
myEntry.place(in_=frame, x=80, y=25)


button = Button(text='Submit', command=button_clicked)
button.place(in_=frame, x=40, y=65)

N1 = button_clicked()
print(N1)

root.mainloop()
