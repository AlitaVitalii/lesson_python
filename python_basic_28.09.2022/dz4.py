num_ = int(input("vvedite chislo: "))
i = 1
s = 0
while i <= num_:
    a = 1
    while a <= num_:
        if i % a == 0:
            s += 1
        a += 1
    if s == 2:
        print(i)
    s = 0
    i += 1
