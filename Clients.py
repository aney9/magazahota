import sqlite3


class Clients:
    def tovary(self):
        conn = sqlite3.connect('xz.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tovary(
        id_tovary INTEGER PRIMARY KEY NOT NULL,
        model TEXT NOT NULL,
        price TEXT NOT NULL,
        id_users INTEGER,
        FOREIGN KEY (id_users) REFERENCES users(id_users)
        )
        ''')
        cursor.executemany("INSERT INTO tovary(model, price) VALUES (?,?)",
                           [("HONDA CB750-2","154000"),
                           ("HONDA STEED 400","108000"),
                           ("KAWASAKI ZR-7S","376000"),
                           ("YAMAHA VMAX","186000"),
                           ("YAMAHA YZF-R1","131000")]
                           )
        conn.commit()
    def prosmotr(self):
        conn = sqlite3.connect('xz.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tovary")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    def vybortovara(self):
        conn = sqlite3.connect('xz.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tovary")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        while True:
            try:
                id_users = int(input("Введите ваш ID: "))
                id_tovary = int(input("Введите ID товара: "))
            except ValueError:
                continue
            cursor.execute("UPDATE tovary SET id_users = ? WHERE id_tovary = ?", (id_users,id_tovary))
            conn.commit()
            break
