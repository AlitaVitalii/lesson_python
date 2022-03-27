
book = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
        [98762, 'Programming Python, Mark Lutz', 5, 56.80],
        [77226, 'Head First Python, Paul Barry', 3, 32.95],
        [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

book_tuple = []

for i in book:
    n = i[0]
    if i[2] * i[3] < 100:
        s = (i[3] + 10) * i[2]
    else:
        s = i[2] * i[3]
    s = round(s, 2)
    book_tuple.append((n, s))

print(book_tuple)