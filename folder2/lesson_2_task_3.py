def square(a):
    s = a ** 2
    return s
from math import ceil
a = float(input("Введите сторону квадрата: "))
result = ceil(square(a))
print(result)

