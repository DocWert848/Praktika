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


create_cube(5, 3)

print("-" * 10)

create_cube(8, 4)

print("-" * 10)

create_cube(10, 10)
