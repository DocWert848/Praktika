#Задание 1
while True:
    x = input("число: ")
    if x.isdigit():
        x = int(x)
        print(*(range(x + 1)))
        break
    else:
        print(f"{x} - не число. Повторите ввод.")
#Задание 2
any_list = [4, 3.2, 16, 9, 13.5, 67]
for i, val in enumerate(any_list):
    try:
        result = val / i
        print(f"{val} / {i} = {result}")
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {val}")
#Задание 3
numbers = []
while len(numbers) < 5:
    val = input(">>> ")
    try:
        num = float(val)
        if num.is_integer():
            num = int(num)
        numbers.append(num)
    except ValueError:
        continue
print(f"Числа в списке: {numbers}")
