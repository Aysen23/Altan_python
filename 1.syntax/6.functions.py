# *** Функции ***

# Создание (определение) функции

# 1 вариант.
# Функция которая не принимает данные (нет аргументов)
# и ничего не возвращает

def func_1():
    var_1 = 100
    var_2 = 20
    res = var_1 + var_2
    print(res)

# вызов функции
# func_1()

# 2 вариант.
# Функция, принимающая параметры (значения,данные) (обладает аргументами)
# и ничего не возвращающая

def func_2(arg_1):
    res = arg_1 ** 2
    print(res)

# func_2(10)

def func_3(a, b, c):
    res = a + b % c
    print(res)

# позиционная передача параметров
# func_3(5, 10, 4)

# аргументы могут иметь значения по умолчанию
def func_4(arg_1, arg_2 = 5):
    print(arg_1 * arg_2)

# передача одного параметра
# func_4(20)

# передача двух параметров
# передаваемый параметр имеет приоритет
# func_4(20, 2)

def func_5(a = 10, b = 20, c = 5):
    print(a + b + c)

# Позиционная передача параметров
# func_5(100, 2)

# Именованная передача параметров
# func_5(c = 10)

# Смешанная передача параметров
# func_5(100, c = 2)

# Передача произвольного кол-ва параметров
# - позиционных
def func_6(*args):
    print(args)
    res = args[0] + args[1]
    print(res)

# func_6(10, 20)

# - именованных
def func_7(**kwargs):
    print(kwargs)
    res = kwargs["a"] + kwargs["b"] + kwargs["c"]
    print(res)

# func_7(a=10, b=20, c=30)

# 3 вариант.
# Функция, принимающая параметры 
# и возвращающая значения

def func_8(arg_1, arg_2):
    res = arg_1 > arg_2
    return res

res = func_8(10, 20)
# print(res)

# возврат двух значений
def func_9(x, y):
    a = x * y
    b = x ** y
    return a, b

# print(func_9(2, 8))
var_1, var_2 = func_9(2, 8)
# print(var_1, var_2)


# *** Безымянные функции (лямбда-функции, лямбда-выражения) ***

# Особенности:
# - однострочная конструкция
# - всегда имеют аргументы
# - всегда возвращает объект

my_lambda = lambda arg_1: arg_1 ** 3

# print(my_lambda(10))

# Пример 1. Словарь лямбда-выражений
# my_lambdas = {
#     "key_1": lambda a, b: (a + b)**2,
#     "key_2": lambda a, b, c: (a + b)**c
# }

# # print(my_lambdas["key_1"](2, 3))

# # Пример 2. Передача объекта лямбды в функцию в качестве параметра
# def func_10(f, n):
#     res = f(n)
#     print(res)

# func_10(lambda x: x * x, 10)

# Упорядочивание множества функций 
# с помощью специальной функции "main"
def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate, money)
    print("К выдаче", result, "долларов")
 
 
def say_hello(name):
    print("Hello,", name)
     
     
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result
 
# Вызов функции main
main()