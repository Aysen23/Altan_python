# *** Генератор паролей ***

# password_fb

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def generator():
    # чтение строки сырой пароли
    pwd_str = pwd.get() + salt.get()
    # кодирование в байт-строка
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest() # [:10] - короткий способ сократить строку вывода до 10 символов
    s = hex_str # [:10] - более короткий способ сократить строку вывода до 10 символов
    start = s[:12]  # - более длинный способ сократить строку вывода до 12 символов

    # вывод хеш-строки
    # print(hex_str)
    hash_pwd.set(start)
# generator("qwerty")

# объект окна
window = Tk()
window.title("Pwd generator v.0.1")

# объекты для хранения строк
pwd = StringVar()
salt = StringVar()
hash_pwd = StringVar()

# тестирование StringVar
#  pwd.set("qwerty")

#  print(pwd.get())

# виджет (компонент) текстовой метки
lbl = Label(text="Пароль:")
lbl.grid(row=0, column=0)

lbl_1 = Label(text="Соль:")
lbl_1.grid(row=1, column=0)

# виджет поля ввода
Entry(textvariable=pwd, show="*").grid(row=0, column=1)
Entry(textvariable=salt).grid(row=1, column=1)

# виджет кнопки
Button(text="СТАРТ", command=generator).grid(row=2, column=0)

# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=2, column=1)

# точка входа программы (место, где программа запускается)
window.mainloop()