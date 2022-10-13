# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from cmath import sqrt


def InputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"В6ведите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a

def calculateLengthSegment(a, b):
    lengthSegment = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    return lengthSegment


print('Введите координаты первой точки')
pointA = InputNumbers(2)
print('Введите координаты второй точки')
pointB = InputNumbers(2)

print(f"Длина отрезка: {calculateLengthSegment(pointA, pointB)}")




