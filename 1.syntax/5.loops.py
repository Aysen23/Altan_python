#  *** Циклы (операторы циклов) ***

# Оператор while

# бесконечный цикл (условие всегда True)
# while True:
#     print("Hello!")

# while c прерывающийся по условии
num = 0

# while num < 10:
#     # print(num)
#     #  инкремент
#     # num = num + 1 # длинная запись
#     num += 1 # короткая запись
#     print(num)

# прерывание цикла по дополнительному условию
num = 10

# while num > 0:
#     print(num)
#     if num == 5:
#         # инструкция прерывания цикла
#         break
#     # декремент
#     num -= 1

num = 80
# while num < 100:
#     s = input("Введите команду: ")
#     if s == "stop":
#         print("Bye bye!")
#         break
#     print(f"Вы ввели: {s}")
#     num += 10

# пропуск куска кода в теле цикла
# while  True:
#     s = input("Введите слово ДА: ")
#     if s == "ДА":
#         print("Цикл продолжается! :)")
#         continue
#     print("Циклу конец :(")
#     break


# Оператор for

# 1. читает значение элемента итерируемого объекта по порядку
# 2. значение присваивается в свою переменную
# 3. выполняет блок кода своего тела

# for n in [1,2,3,4,5]:
#     print(n)

# for m in (10,20,30,40):
#     print(m)

# for _ in (1,2,3,4,):
#     print("hello!")

# for char in "python":
#     print(char)

my_tuple = (100, 400, 200, 700, 2021)

# for i in my_tuple:
#     res = i * 2
#     print(res)

# for i in my_tuple[::-1]:
#     print(i)


# Класс range()

r = range(2, 10)
# print(r)

# for n in range(2, 10):
#     print(n)

# for n in range(10):
#     print(n)

# for n in range(10, 100, 10)[::-1]:
#     print(n)


# *** генератор списка ***

my_list = [num for num in range(50, 100, 10)]

my_list = [num + 100 for num in range(10)]

my_list = [num  for num in range(10) if num % 2 == 0]

# print(my_list)

# *** генератор словарей ***

# ключ значения

# a = {word: len(word) for word in ['hello', 'hi', 'www']}

# изменяемые списки ключами быть не могут
# a = {word: len[word] for word in ['hello', 'hi', 'www']} 

# print(a) 

# data = {
#     'Джефф Безос': "177",
#     "ИлоН МаСк": "126",
#     "бернар АрнО": "150",
#     "БиЛл ГейтС": "124",
# }
# new_data = {key.title():int(value)for key, value in data.items()}
# то же самое без генератора словарей
# new_data = {} 
# for key, value in data.items():
#     new_data[key.title()] = int(value)
# print(data)
# print(new_data)

users = [
    [0, "Bob", "password"],
    [1, "code", "python"],
    [2, "Stack", "overflow"],
    [3, "username", "1234"],
    [51, "qwerty", "1234"],
]
new_users = {user[0]: user for user in users}
print(new_users[51])