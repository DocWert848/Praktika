notebook = {}
proverka = False
while not proverka:
    print(
        "[1]- сделать заметку. [2] - посмотреть заметки. [3] -удалить заметку. [4] -выход."
    )
    deustvue = int(input("введите действие которое хотите выполнить:"))
    if deustvue > 0 and deustvue < 5:
        proverka = False
        if deustvue == 1:
            pynkt = input("введите пункт цели:")
            cell = input("введите цель:")
            notebook[pynkt] = cell
            print(notebook)
        elif deustvue == 2:
            print("ваши заметки:")
            print(notebook)
        elif deustvue == 3:
            delite = input("введите пункт который хотите удалить:")
            notebook.pop(delite)
            print(notebook)
        elif deustvue == 4:
            print("вы вышли из заметок")
            proverka = True
    else:
        proverka = False
