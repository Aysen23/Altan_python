# *** Исключения (исключительные события, ситуации, ошибки) ***

# Пример исключения при делении на ноль
a = 100
b = 0

# отлов исключения
# try:
#     # потенциально аварийный код
#     c = a / b
#     print("Всё нормально! :)")
# except:
#     # код который должен сработать при исключении
#     print("Что-то пошло не так :(")
#     c = 0

# print(c)


# Обработка множества исключений
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
# # конкретные типы исключений
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Нужно ввести число!")
# # общее исключение
# except Exception as err:
#     print(err)

# Конструкция "try-except-finally"
# try:
#     a = int(input("Введите число: "))
#     result = 100 / a
#     print("Полёт нормальный! :)")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
#     result = 0
# finally:
#     print("Сработала finally")
#     result = 10

# print(result)


# Кастомизированные исключения
# try:
#     a = input("Введите символ: ")
#     if a == 'A':
#         raise Exception("Ошибка А")
#     elif a == 'B':
#         raise Exception("Ошибка В")
#     elif a == 'C':
#         raise Exception("Ошибка C")
# except Exception as err:
#     print(err)

# Пример приближенный к реальности
# while True:
#     try:
#         a = int(input("Введите число: "))
#         c = 100 / a
#     except ZeroDivisionError:
#         print("Деление на ноль невозможно!")
#         continue
#     except ValueError:
#         print("Вы ввели не число!")
#         continue
#     print(f"Result: {c}")
#     break

# Пример калькулятор
def calculate(n1, n2, op):
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return d[op](n1, n2)

while True:
    # ввод данных
    cmd = input("Командуйте, сэр: ")
    if cmd == "stop":
        print("Buy buy!")
        break

    try:
        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))  
        op = input("Введите символ операции: ")

        # обработка данных
        result = calculate(num_1, num_2, op)
    except ZeroDivisionError:
        result = "На ноль делить нельзя!"
        continue
    except ValueError:
        result = "Вы ввели не число!"
        continue
    finally:
        # вывод данных
        print(f"Результат: {result}")
