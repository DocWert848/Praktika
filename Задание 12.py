#Задание 1
x = lambda a, b: a * b
print(x(2, 3))
#Задание 2
count = int(input("Всего чисел будет: "))
numbers_list = []
for i in range(count):
    num = int(input())
    numbers_list.append(num)
filtered_numbers = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers_list))
print(filtered_numbers)
