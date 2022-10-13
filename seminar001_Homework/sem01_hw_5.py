# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).


qarterNumber = int(input(f'Введите номер  четверти: '))
if qarterNumber == 1:
    text = 'x > 0 и y > 0'
if qarterNumber == 2:
    text = 'x < 0 и y > 0' 
if qarterNumber == 3:
    text = 'x < 0 и y < 0'
if qarterNumber == 4:
    text = 'x > 0 и y < 0'

print(f'для номера четвери {qarterNumber} диапазон координат {text}')
