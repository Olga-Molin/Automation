def bank(X, Y):
     
    for i in range(Y):
        X += (X / 10)
    return X
X = int(input("Введите сумму вклада: "))
Y = int (input ("На какой срок в годах: "))
result = bank(X, Y)
print("Сумма на счету за", Y, "года/лет составляет", result, "руб.")
 # написать функцию bank, принимающую аргументы X и Y, и возвращающую сумму, которая будет на счету пользователя спустя Y лет.   
