import sqlite3


class Admin:
    conn = sqlite3.connect("xz.db")
    cursor = conn.cursor()


    def prosmotr(self):
        conn = sqlite3.connect("xz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sotrudniki")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

    def dobavlenie(self):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        surname = input('Введите фамилию: ')
        namee = input('Введите имя: ')
        middlename = input('Введите отчество(если есть): ')
        self.cursor.execute("INSERT INTO sotrudniki(login,password, surname, firstname, middlename) VALUES (?,?,?,?,?)",
                            (login, password, surname, namee, middlename))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM sotrudniki")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def udalenie(self):
        value = self.cursor.fetchall()
        if not value:
            self.cursor.execute("SELECT * FROM sotrudniki")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            idydal = input('Введите ID сотрудника для удаления: ')
            self.cursor.execute("DELETE FROM sotrudniki WHERE id = ?", (idydal,))
            self.conn.commit()
            print(f"Сотрудник с ID {idydal} делитнут")
        else:
            print("Нечего удалять")

    def izmenenie(self):
        self.cursor.execute("SELECT * FROM sotrudniki")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        idyizmen = input('Введите ID для изменения: ')
        self.cursor.execute("SELECT * FROM sotrudniki WHERE id = ?", (idyizmen,))
        v = self.cursor.fetchone()
        print(v)
        login = input('Введите новый логин: ')
        password = input('Введите новый пароль: ')
        surname = input('Введите новую фамилию: ')
        namee = input('Введите новое имя: ')
        middlename = input('Введите новое отчество(если есть): ')
        self.cursor.execute(
            "UPDATE sotrudniki SET login = ?, password = ?, surname = ?, firstname = ?, middlename = ? WHERE id = ?",
            (login, password, surname, namee, middlename, idyizmen))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM sotrudniki")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
