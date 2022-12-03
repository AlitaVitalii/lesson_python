my_dikt = {}
with open('111.txt', encoding='utf-8') as f:
    for row in f.readlines():
        for i in ['.', ',', '!', ':', ';', '?']:
            s = row.lower().replace(i, '')
        mas = s.split()
        for x in mas:
            if len(x) >= 5:
                k = s.count(x)
                my_dikt[x] = k

# my_dikt = sorted(my_dikt.items(), key=lambda ind: ind[1], reverse=True)


print(my_dikt)
