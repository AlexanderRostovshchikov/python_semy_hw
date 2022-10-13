# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def InputNumbers(x):
    nameNum = ["X","Y","Z"]
    arr = []
    for i in range(x):
        arr.append(input(f"Введите значение {nameNum[i]}: "))
    return arr

def TruthCheck(arr):
    first = not(arr[0] or arr[1] or arr[2])
    second = not arr[0]and not arr[1] and not arr[2]
    truth = first == second
    return truth

statement = InputNumbers(3)

if TruthCheck(statement) == True:
    print(f'Утверждение верно')
else:
    print(f'Утверждение ложно')
