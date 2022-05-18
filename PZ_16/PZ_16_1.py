# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).
# БД должна обеспечивать получение информации по сумме сделки.
import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#FFCB73', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="images/plus.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить запись', command=self.open_dialog, bg='#FFB840', bd=0,
                                         compound=tk.TOP, image=self.add_img, padx=10)
        self.btn_open_dialog.pack(side=tk.LEFT, padx=10)

        self.update_img = tk.PhotoImage(file="images/edit.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#FFB840', bd=0,
                                    compound=tk.TOP, image=self.update_img, padx=10)
        btn_edit_dialog.pack(side=tk.LEFT, padx=10)

        self.delete_img = tk.PhotoImage(file="images/delete.png")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#FFB840', bd=0,
                               compound=tk.TOP, image=self.delete_img, padx=10)
        btn_delete.pack(side=tk.LEFT, padx=10)

        self.search_img = tk.PhotoImage(file="images/search.png")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#FFB840', bd=0,
                               compound=tk.TOP, image=self.search_img, padx=10)
        btn_search.pack(side=tk.LEFT, padx=10)

        self.refresh_img = tk.PhotoImage(file="images/refresh.png")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#FFB840', bd=0,
                                compound=tk.TOP, image=self.refresh_img, padx=10)
        btn_refresh.pack(side=tk.LEFT, padx=10)

        self.tree = ttk.Treeview(self, columns=('user_id', 'full_name', 'service', 'price', 'commission'), height=15,
                                 show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('full_name', width=180, anchor=tk.CENTER)
        self.tree.column('service', width=140, anchor=tk.CENTER)
        self.tree.column('price', width=140, anchor=tk.CENTER)
        self.tree.column('commission', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('full_name', text='ФИО')
        self.tree.heading('service', text='Услуга')
        self.tree.heading('price', text='Сумма Сделки')
        self.tree.heading('commission', text='Комиссионные')
        self.tree.pack()

    def records(self, user_id, full_name, service, price, comis):
        self.db.insert_data(user_id, full_name, service, price, comis)
        self.view_records()

    def update_record(self, user_id, full_name, service, price, comis):
        self.db.cur.execute("""UPDATE not_serv SET user_id=?, full_name=?, service=?, price=?, commission=? WHERE 
        user_id=?""", (user_id, full_name, service, price, comis, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("SELECT * FROM not_serv")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("DELETE FROM not_serv WHERE user_id=?", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, price):
        price = (price,)
        self.db.cur.execute("SELECT * FROM not_serv WHERE price>?", price)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search(self)


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить запись')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self, width=27)
        self.entry_description.place(x=150, y=25)

        label_name = tk.Label(self, text='ФИО')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self, width=27)
        self.entry_name.place(x=150, y=50)

        label_serv = tk.Label(self, text='Услуга')
        label_serv.place(x=50, y=75)
        self.entry_serv = ttk.Entry(self, width=27)
        self.entry_serv.place(x=150, y=75)

        label_old = tk.Label(self, text='Сумма')
        label_old.place(x=50, y=100)
        self.entry_price = ttk.Entry(self, width=27)
        self.entry_price.place(x=150, y=100)

        label_score = tk.Label(self, text='Комиссионные')
        label_score.place(x=50, y=125)
        self.entry_comis = ttk.Entry(self, width=27)
        self.entry_comis.place(x=150, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=200, y=160)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=120, y=160)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_serv.get(),
                                                                       self.entry_price.get(),
                                                                       self.entry_comis.get()))

        self.grab_set()
        self.focus_set()


class Search(tk.Toplevel):
    """Класс для дочернего окна поиска"""

    def __init__(self, root):
        super().__init__(root)
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('360x130+400+370')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск по сумме сделки выше указанного вами числа:')
        label_search.place(x=20, y=20)
        self.entry_search = ttk.Entry(self, width=25)
        self.entry_search.place(x=100, y=50)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=180, y=80)

        btn_ok = ttk.Button(self, text='Поиск')
        btn_ok.place(x=100, y=80)
        btn_ok.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_ok.bind('<Button-1>', lambda event: self.destroy(), add='+')


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=105, y=160)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_name.get(),
                                                                          self.entry_serv.get(),
                                                                          self.entry_price.get(),
                                                                          self.entry_comis.get()))
        self.btn_ok.destroy()


class DB:
    def __init__(self):
        with sq.connect('Notary_Services.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS not_serv (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                service text NOT NULL,
                price INTEGER,
                commission INTEGER
                )""")

    def insert_data(self, user_id, full_name, service, price, comis):
        self.cur.execute("INSERT INTO not_serv(user_id, full_name, service, price, commission) VALUES (?, ?, ?, ?, ?)",
                         (user_id, full_name, service, price, comis))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Нотариальные услуги")
    root.geometry("650x450+300+200")
    root.iconphoto(True, tk.PhotoImage(file='images/doc.png'))
    root.resizable(False, False)
    root.mainloop()
