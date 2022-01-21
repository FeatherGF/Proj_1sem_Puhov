from tkinter import *
# from tkinter import ttk

root = Tk()
root.title('Учебная форма')
root.geometry('400x400')
var = IntVar()

frame1 = LabelFrame(bd=3, text='User Login Info')
frame1.grid(sticky=N+S+E+W)


Label(frame1, text='Username:', justify='left', height=2).grid(row=1, column=1, sticky=W)
Entry(frame1, width=33).grid(row=1, column=2, columnspan=2)

Label(frame1, text='Email:', height=2).grid(row=2, column=1, sticky=W)
Entry(frame1, width=33).grid(row=2, column=2, columnspan=2)

Label(frame1, text='Password:', height=2).grid(row=3, column=1, sticky=W)
Entry(frame1, width=33).grid(row=3, column=2, columnspan=2)

frame2 = LabelFrame(bd=3, text='Personal Data')
frame2.grid(sticky=N+S+E+W)

Label(frame2, text='Address:', height=2).grid(row=4, column=1, sticky=W)
Entry(frame2, width=33).grid(row=4, column=2, columnspan=2)

Label(frame2, text='Date of Birth:', height=2).grid(row=5, column=1, sticky=W)
Entry(frame2, width=33).grid(row=5, column=2, columnspan=2)

Label(frame2, text='Age:', height=2).grid(row=6, column=1, sticky=W)
Entry(frame2, width=33).grid(row=6, column=2, columnspan=2)

Label(frame2, text='Gender:', height=2).grid(row=7, column=1, sticky=W)
Radiobutton(frame2, text='Male', variable=var, value='M').grid(row=7, column=2)
Radiobutton(frame2, text='Female', variable=var, value='F').grid(row=7, column=3)

frame3 = LabelFrame(bd=3)
frame3.grid(sticky=N+S+E+W)

Label(frame3, height=2, text='I accept forum\'s rules').grid(row=8, column=1, columnspan=2)
Checkbutton(frame3).grid(row=8, column=3)

Button(frame3, text='Submit', width=5, height=1).grid(row=9, column=1, sticky=W)
Button(frame3, text='Reset', width=5, height=1).grid(row=9, column=2)

root.mainloop()
