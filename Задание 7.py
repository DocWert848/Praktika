#Задание 1 
table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]


print("1. Исходный массив:")
for row in table:
    print(row)
print()


modified_table = []
for row in table:
    new_row = []
    for item in row:
        if item != 'folder':
            if item == 'data.accdb':
                new_row.append('data.sql')
            else:
                new_row.append(item)
    modified_table.append(new_row)

print("2. Массив после удаления папок и замены data.accdb:")
for row in modified_table:
    print(row)
print()


py_files = []
for row in table:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

print("3. Файлы с расширением .py:")
print(py_files)
print()


js_files = []
for row in table:
    for item in row:
        if item.endswith('.js'):
            js_files.append('new_' + item)

print("4. Файлы с расширением .js с префиксом 'new_':")
print(js_files)
#Задание 2
word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

n = int(input("Введите число от 0 до 9: "))

if 0 <= n <= 9:
  for i in range(n + 1):
        print(word_numb[i])
else:
    print('Введите число <= 9')
#Задание 3
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
decimal_numbers = []
print("Элементы списка в десятичной системе счисления:")
for binary in bin_sy:
    decimal = int(binary, 2)  
    decimal_numbers.append(decimal)
    print(f"{binary} = {decimal}")
max_number = max(decimal_numbers)
min_number = min(decimal_numbers)
print(f"\nМаксимальное число: {max_number}")
print(f"Минимальное число: {min_number}")
#Задание 4
matrix = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, 'error', 8]
]

print("Исходная матрица:")
for row in matrix:
    print(row)


for row_idx, row in enumerate(matrix):
    for col_idx, element in enumerate(row):
        if isinstance(element, str):
            print(f"Найден строковый элемент '{element}' на позиции [{row_idx}][{col_idx}]")
            matrix[row_idx][col_idx] = len(element)

print("\nИсправленная матрица:")
for row in matrix:
    print(row)

total_sum = sum(sum(row) for row in matrix)
print(f"\nСумма всех элементов матрицы: {total_sum}")
#Задание 5
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Матрица 3x3:")
for row in matrix:
    print(row)
main_diagonal_sum = 0
for i in range(3):
    main_diagonal_sum += matrix[i][i]

print(f"\nСумма главной диагонали (слева направо): {main_diagonal_sum}")
print(f"Элементы: {matrix[0][0]} + {matrix[1][1]} + {matrix[2][2]} = {main_diagonal_sum}")
secondary_diagonal_sum = 0
for i in range(3):
    secondary_diagonal_sum += matrix[i][2 - i]

print(f"\nСумма побочной диагонали (справа налево): {secondary_diagonal_sum}")
print(f"Элементы: {matrix[0][2]} + {matrix[1][1]} + {matrix[2][0]} = {secondary_diagonal_sum}")

print("\n" + "="*50)
print("Пример с другой матрицей:")

import random
random_matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

print("\nСлучайная матрица:")
for row in random_matrix:
    print(row)

random_main_sum = sum(random_matrix[i][i] for i in range(3))
print(f"\nСумма главной диагонали: {random_main_sum}")
random_secondary_sum = sum(random_matrix[i][2 - i] for i in range(3))
print(f"Сумма побочной диагонали: {random_secondary_sum}")
