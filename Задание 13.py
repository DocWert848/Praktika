#Задание 1
def alpha(user_string):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    print(" ".join(alphabet))
    used = []
    for char in user_string.lower():
        if char in alphabet and char not in used:
            used.append(char)
    unused = [char for char in alphabet if char not in used]
    print(" ".join(used + unused))


alpha("пайтон")


#Задание 2
def create_calendar(month_name, year, days_count):
    print(f"calendar: {month_name} {year}")
    for i in range(1, days_count + 1):
        print(i, end=" ")
        if i % 7 == 0:
            print()
    print()


create_calendar("Randomner", 2045, 23)


#Задание 3
def bin_sys(start, end):
    total_sum = 0
    for i in range(start, end + 1):
        print(bin(i)[2:])
        total_sum += i
    print(f"сумма: {bin(total_sum)[2:]}")


bin_sys(3, 6)
#Задание 4
field = [["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]"]]


def begin(arr, row, col):
    arr[row][col] = "*"
    for line in arr:
        print(" ".join(line))


begin(field, 1, 2)


#Задание 5
def _numbers(n1, step=1):
    print(f"[{n1}] [{n1 + 1*step}]\n[{n1 + 2*step}] [{n1 + 3*step}]")


print("Вход 1:")
_numbers(1)
print("Вход 2:")
_numbers(1, 2)


#Задание 6
def exam(text, letter):
    count = text.lower().count(letter.lower())
    print(count)


exam("My name is Sara.", "s")
