def bank(X, Y):
    vklad = X
    for i in range(Y):
        vklad += (vklad / 10)
    return vklad
X = int(input("Введите сумму вклада: "))
Y = int (input ("На какой срок в годах: "))
result = bank(X, Y)
print("Сумма на счету за", Y, "года/лет составляет", result, "руб.")
       
