notebook = {}
proverka = False
while not proverka:
    deustvue = int(input("введите действие которое хотите выполнить:"))
    print ("[1]- сделать заметку. [2] - посмотреть заметки. [3] -удалить заметку. [4] -выход.")
    if deustvue > 0 and deustvue < 5:
        proverka = True
    else:
        proverka = False
if deustvue == 1:
    pynkt = (input("введите пункт цели:"))
    cell = (input("введите цель:"))
    notebook[pynkt] = cell
    print (notebook)
