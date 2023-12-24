import sqlite3

class Sotrudnik:
    conn = sqlite3.connect("xz.db")
    cursor = conn.cursor()


    def prosmotr(self):
        conn = sqlite3.connect('xz.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

    def dobavlenie(self):
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        self.cursor.execute("INSERT INTO users(login,password) VALUES (?,?)",
                            (login, password))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
    def udalenie(self):
        value = self.cursor.fetchall()
        if not value:
            self.cursor.execute("SELECT * FROM users")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            idydal = input('Введите ID клиента для удаления: ')
            self.cursor.execute("DELETE FROM users WHERE id = ?", (idydal,))
            self.conn.commit()
            print(f"Клиент с ID {idydal} удален")
        else:
            print("Нечего удалять")

    def izmenenie(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        idyizmen = input('Введите ID для изменения: ')
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (idyizmen,))
        v = self.cursor.fetchone()
        print(v)
        login = input('Введите новый логин: ')
        password = input('Введите новый пароль: ')
        self.cursor.execute(
            "UPDATE users SET login = ?, password = ? WHERE id = ?",
            (login,password, idyizmen))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)