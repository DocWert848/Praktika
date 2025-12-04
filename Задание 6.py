#Задание 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("matrix:")
for row in matrix:
    print(row)

print("\nнечётные числа matrix")
for row in matrix:
    for num in row:
        if num % 2 != 0:
            print(num, end=" ")

even_count = 0
for row in matrix:
    for num in row:
        if num % 2 == 0:
            even_count += 1

print(f"\n\nкол-во чётных: {even_count}")
#Задание 2
matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]
answer_matrix = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]
print(answer_matrix)
print()
for i in range(len(answer_matrix)):
    row_sum = sum(answer_matrix[i])
    print(f"{answer_matrix[i]} сумма строки: {row_sum}")
#Задание 3
fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
for row in fruits:
    for fruit in row:
        if fruit[0].isupper():
            print(fruit)
#Задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'], 
    [False, 'word', '0110110', 10], 
    ['happiness', '(J °?°)] ', 'luck', None], 
    ['car', '<- code ->', 4.7, True]]
for index, element in enumerate(random_elements):
    if index % 2 == 1: 
        print(element)
