# *** Полиморфизм ***

# поли + морф - разные формы чего-то

# Полиморфизм операторов
res = 100 + 20 # сложение
res = "100" + "20" # конкатенация

# Полиморфизм функций
res = len("python")
res = len([10, 20, 30])

# print(res)

# Полиморфизм методов
class A:
    # атрибут (свойство) определённое без конструктора
    attr_1 = 100
    def m1(self, arg):
        print(arg + self.attr_1)

class B:
    def m1(self, arg):
        print(arg * 5)

obj_a = A()
obj_b = B()

# obj_a.m1(10)
# obj_b.m1(10)

class C(A):
    pass

class D(A):
    def m1(self):
        print("hello", self.attr_1)

obj_c = C()
obj_d = D()

# obj_c.m1(10)
# obj_d.m1()

# Полиморфизм с "магическими" методами (методами перегрузки операторов)

class Sum:
    # def compute(self, a, b):
    #     print(a + b)
    def __call__(self, a, b):
        print(a + b)
    
    def __str__(self):
        return "Sum object"

s = Sum()
# s.compute(10, 20)
# s(10, 20)
# print(s)

# *** Инкапсуляция ***

# инкапсуляция - скрытие атрибутов или методов
# чтобы они не были доступны из экземпляров класса


# не строгая инкапсуляция
class X:
    def __init__(self, arg):
        self._attr = arg

    def _m1(self, arg):
        return self._attr ** arg

    def m2(self, arg):
        print(self._m1(arg))

x = X(5)
# x.m2(10)
# print(x._m1(5))

# строгая инкапсуляция
class Y:
    def __init__(self, arg):
        self.__attr = arg

    def __m1(self):
        return self.__attr ** 2

    def m2(self, arg):
        print(self.__m1() + arg)

y = Y(5)
# y.m2(2)
# y.__m1()
# y.__attr

# обходной путь
# print(y._Y__attr)
# print(y._Y__m1())


# *** Композиция (Агрегация) ***

class Neuron:
    def __init__(self, w):
        self.weights = w
    def __call__(self, data):
        return self.weights[0] * data[0] + self.weights[1] * data[1]

class Net:
    # композиция
    n0 = Neuron([-1.5, 0.75])
    n1 = Neuron([0.5, 1.7])
    n2 = Neuron([-1.0, -0.5])

    def __call__(self, *data):
        res = []
        res.append(self.n0(data))
        res.append(self.n1(data))

        print(self.n2(res))

nn = Net()

nn(0.1, 0.7)