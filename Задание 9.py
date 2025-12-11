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
            pynkt = input("введите пункт заметки:")
            cell = input("введите заметку:")
            notebook[pynkt] = cell
            print(notebook)
        elif deustvue == 2:
            if notebook == {}:
                print("Заметок нет")
            else:
                for pynkt, cell in notebook.items():
                    print(f"Заметка {pynkt}")
                pynkt = input("введите пункт заметки:")
                if pynkt in notebook:
                    print(f"заметка {pynkt}: {notebook[pynkt]}")
                elif pynkt not in notebook:
                    print(f"пункта {pynkt} нет")
        elif deustvue == 3:
            for pynkt, cell in notebook.items():
                print(f"Заметка {pynkt}")
            delite = input("введите пункт который хотите удалить:")
            notebook.pop(delite)
            print(notebook)
        elif deustvue == 4:
            print("вы вышли из заметок")
            proverka = True
    else:
        proverka = False
