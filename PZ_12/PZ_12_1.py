from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Учебная форма')
root.geometry('313x385+350+350')
var = IntVar()
root.resizable(width=False, height=False)

frame1 = LabelFrame(bd=3, text='User Login Info')  # создаю рамку, в которую ставлю текста Username:, Email:,
# Password: и соответствующие им поля ввода
frame1.grid(sticky=N + S + E + W, padx=5)

Label(frame1, text='Username:', justify='left', height=2).grid(row=1, column=1, sticky=W)
Entry(frame1, width=33).grid(row=1, column=2, columnspan=2, padx=17, pady=5)

Label(frame1, text='Email:', height=2).grid(row=2, column=1, sticky=W)
Entry(frame1, width=33).grid(row=2, column=2, columnspan=2, padx=17, pady=5)

Label(frame1, text='Password:', height=2).grid(row=3, column=1, sticky=W)
Entry(frame1, width=33).grid(row=3, column=2, columnspan=2, padx=17, pady=5)

frame2 = LabelFrame(bd=3, text='Personal Data')
frame2.grid(sticky=N + S + E + W, padx=5,
            pady=2)  # создаю вторую рамку, в которую ставлю текста Address:, Date of Birth:,
# Age:, Gender: и соответствующие им поля ввода, а также виджет с единственным выбором из двух(RadioButton)

Label(frame2, text='Address:', height=2).grid(row=4, column=1, sticky=W)
Entry(frame2, width=33).grid(row=4, column=2, columnspan=2, padx=5, pady=5)

Label(frame2, text='Date of Birth:', height=2).grid(row=5, column=1, sticky=W)
Entry(frame2, width=33).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

Label(frame2, text='Age:', height=2).grid(row=6, column=1, sticky=W)
Entry(frame2, width=33).grid(row=6, column=2, columnspan=2, padx=5, pady=5)

Label(frame2, text='Gender:', height=2).grid(row=7, column=1, sticky=W)
ttk.Radiobutton(frame2, text='Male', variable=var, value='M').grid(row=7, column=2, sticky=W)
ttk.Radiobutton(frame2, text='Female', variable=var, value='F').grid(row=7, column=3, sticky=W)

frame3 = LabelFrame(bd=3)
frame3.grid(sticky=N + S + E + W,
            padx=5)  # создаю последнюю рамку, в которую ставлю текст "I accept forum's rules", поле
# для галки и две кнопки

Label(frame3, height=2, text='I accept forum\'s rules').grid(row=8, column=1, columnspan=2, pady=3)
Checkbutton(frame3).grid(row=8, column=3)

ttk.Button(frame3, text='Submit', width=7).grid(padx=5, pady=5, row=9, column=1, sticky=W)
ttk.Button(frame3, text='Reset', width=5).grid(padx=5, pady=5, row=9, column=2)

root.mainloop()
