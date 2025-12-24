#Задание 1
def upper(t):
    bukvu = []
    for simvol in t:
        if simvol.isupper():
            bukvu.append(simvol)
    if bukvu:
        print(" ".join(bukvu))


upper("PriVet")
upper("Яхта паРУС аЛьпА Н")

#Задание 2
def punct(txt):
    znaku = []
    for simvol in txt:
        if (
            simvol == "("
            or simvol == ")"
            or simvol == "!"
            or simvol == "?"
            or simvol == ","
            or simvol == "."
        ):
            znaku.append(simvol)
    if znaku:
        print(len(znaku))


punct("(Как дела?)")

#Задание 3
def create_cube(x: int, y: int):
    row = "*" * x
    for _ in range(y):
        print(row)

#Задание 4
create_cube(5, 3)

print("-" * 10)

create_cube(8, 4)

print("-" * 10)

create_cube(10, 10)

def double(s):
    saaas = []
    for simvol in s:
        saaas.append(2 * simvol)
    if saaas:
        print("".join(saaas))


double("stroka")

#Задание 5
def Constructor(details, people, cars, trees):
    required_details = 72
    required_people = 4
    required_cars = 2
    required_trees = 7
    max_sets = min(
        details // required_details,
        people // required_people,
        cars // required_cars,
        trees // required_trees,
    )
    print(max_sets)


print(">>> Constructor(144, 8, 4, 14)")
Constructor(144, 8, 4, 14)
print(">>> Constructor(10000, 16, 6, 2)")
Constructor(10000, 16, 6, 2)


#Задание 6
def Constructor(details, people, cars, trees):
    required_details = 72
    required_people = 4
    required_cars = 2
    required_trees = 7
    max_sets = min(
        details // required_details,
        people // required_people,
        cars // required_cars,
        trees // required_trees,
    )
    print(max_sets)


print(">>> Constructor(144, 8, 4, 14)")
Constructor(144, 8, 4, 14)
print(">>> Constructor(10000, 16, 6, 2)")
Constructor(10000, 16, 6, 2)


#Задание 7
def custom_filter(data_list):
    total_sum = 0
    for item in data_list:
        if isinstance(item, int) and not isinstance(item, bool):
            if item % 7 == 0:
                total_sum += item
    print(f">>> сумма: {total_sum}")
    print(total_sum <= 83)


print(">>> print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))")
custom_filter([7, 10.5, "txt", 14, 2, 56])
print(">>> print(custom_filter([70, 21]))")
custom_filter([70, 21])


#Задание 8
def square(x, y):
    top_border = "_" * (len(str(x)) + len(str(y)) + 3)
    print(top_border)
    middle = f"| {x} {y} |"
    print(middle)
    bottom_border = "¯" * (len(str(x)) + len(str(y)) + 3)
    print(bottom_border)


print(">>> square(2, 3)")
square(2, 3)
print(">>> square(100, 5000)")
square(100, 5000)
