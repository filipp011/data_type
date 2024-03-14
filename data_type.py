import math
import random

# Периметр и площадь
def test_perimetr_and_S():
    a = 10
    b = 20
    P = 2 * (a + b)
    S = a * b
    assert P == 60
    assert S == 200

# Вывод приветствия
def test_hello():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    assert output == "Привет, Анна! Тебе 25 лет."

    #Длина окружности
def test_circle():
    math.pi = 3.14
    r = 23
    C = 2 * math.pi * r
    assert C == 144.44

    #Сортировка по возрастнию
def test():
    a = random.randint(0,100)
    l=[1,5,6,2,10,4,9,3,7,8]
    l.sort()
    print(l,a)

# Вывод уникальных значений
def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    print(list(set(l)))





