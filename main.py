import sqlite3
import sys
from Admin import Admin
from Sotrudnik import Sotrudnik
from Clients import Clients
conn = sqlite3.connect('xz.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id_users INTEGER PRIMARY KEY,
                    login TEXT,
                    password TEXT   
                    )
                """)

cursor.execute('''
            CREATE TABLE IF NOT EXISTS sotrudniki(
            id INTEGER PRIMARY KEY,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            surname TEXT NOT NULL,
            firstname TEXT NOT NULL,
            middlename TEXT
            )
        ''')


cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins(
            id INTEGER PRIMARY KEY,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            surname TEXT NOT NULL,
            firstname TEXT NOT NULL,
            middlename TEXT NOT NULL
            )
        ''')

def regadm():
    conn = sqlite3.connect('xz.db')
    cursor = conn.cursor()
    login_adm = input('Введите логин админа: ')
    password_adm = input('Введите пароль админа:')
    surname_adm = input('Введите фамилию админа:')
    firstname_adm = input('Введите имя админа: ')
    middlename_adm = input('Введите отчество админа: ')
    cursor.execute("INSERT INTO admins (login, password,surname, firstname, middlename) VALUES (?,?,?,?,?)", (login_adm,password_adm, surname_adm, firstname_adm, middlename_adm))
    conn.commit()

def regsotr():
    conn = sqlite3.connect('xz.db')
    cursor = conn.cursor()
    login_sotr = input('Введите логин сотрудника: ')
    password_sotr = input('Введите пароль сотрудника:')
    surname_sotr = input('Введите фамилию сотрудника:')
    firstname_sotr = input('Введите имя сотрудника: ')
    middlename_sotr = input('Введите отчество сотрудника: ')
    cursor.execute("INSERT INTO sotrudniki (login, password,surname, firstname, middlename) VALUES (?,?,?,?,?)", (login_sotr, password_sotr, surname_sotr, firstname_sotr, middlename_sotr))
    conn.commit()

def regcl():
    login = input('Введите логин клиента: ')
    password = input('Введите пароль клиента:')
    cursor.execute("INSERT INTO users (login, password) VALUES (?,?)", (login, password))
    conn.commit()

def main():
    while True:
        try:
            vybor_menu = int(input('Выберите опцию в меню\n1. Зарегистрироваться\n2. Войти\n3. Выйти\n'))
        except ValueError:
            continue
        if vybor_menu == 1:
            while True:
                try:
                    vybor = int(input('Как вы хотите зарегистрироваться?\n1. Как клиент\n2. Как сотрудник\n3. Как админ\n4. Выйти\n'))
                except ValueError:
                    continue
                if vybor == 1:
                    regcl()
                    print('Регистрация прашла успешна, брад')
                    main()
                if vybor == 2:
                    regsotr()
                    print('Регистрация прашла успешна, брад')
                    main()
                if vybor == 3:
                    regadm()
                    print('Регистрация прашла успешна, брад')
                    main()
                if vybor == 4:
                    sys.exit()
        if vybor_menu == 2:
            while True:
                try:
                    vybor = int(input('Выберите за кого хатите войти\n1. За админа\n2. За сотрудника\n3. За клиента\n4. Выйти\n'))
                except ValueError:
                    continue
                if vybor == 1:

                    regadm()
                    print('Вы зашли как админ')
                    while True:
                        try:
                            vybor = int(input('1. Просмотр всех сотрудников\n'
                                            '2. Добавить сотрудника\n'
                                            '3. Удалить сотрудника\n'
                                            '4. Изменить сотрудника\n'
                                            '5. Выйти\n'
                                            ))
                        except ValueError:
                            continue
                        if vybor == 1:
                            lol = Admin()
                            lol.prosmotr()
                        if vybor == 2:
                            lol = Admin()
                            lol.dobavlenie()
                        if vybor == 3:
                            lol = Admin()
                            lol.udalenie()
                        if vybor == 4:
                            lol = Admin()
                            lol.izmenenie()
                        if vybor == 5:
                            sys.exit()
                if vybor == 2:
                    regsotr()
                    print('Вы зашли как сотрудник')
                    while True:
                        try:
                            vybor = int(input('1. Просмотр всех клиентов\n'
                                        '2. Добавить клиента\n'
                                        '3. Удалить клиента\n'
                                        '4. Изменить клиента\n'
                                        '5. Выйти\n'))
                        except ValueError:
                            continue
                        if vybor == 1:
                            lol = Sotrudnik()
                            lol.prosmotr()
                        if vybor == 2:
                            lol = Sotrudnik()
                            lol.dobavlenie()
                        if vybor == 3:
                            lol = Sotrudnik()
                            lol.udalenie()
                        if vybor == 4:
                            lol = Sotrudnik()
                            lol.izmenenie()
                        if vybor == 5:
                            sys.exit()
                if vybor == 3:
                    regcl()
                    print('Вы зашли как клиент')
                    while True:
                        try:
                            vybor = int(input('Выберите действие\n1. Просмотр товаров\n2. Выбор товаров\n3. Выйти\n'))
                        except ValueError:
                            continue
                        if vybor == 1:
                            lol = Clients()
                            lol.tovary()
                            lol.prosmotr()
                        if vybor == 2:
                            lol = Clients()
                            lol.tovary()
                            lol.vybortovara()
                        if vybor == 3:
                            sys.exit()
                if vybor == 4:
                    sys.exit()
main()
