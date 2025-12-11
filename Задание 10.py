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
