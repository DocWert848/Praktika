def upper(t):
    bukvu = []
    for simvol in t:
        if simvol.isupper():
            bukvu.append(simvol)
    if bukvu:
        print(" ".join(bukvu))


upper("PriVet")
upper("Яхта паРУС аЛьпА Н")
