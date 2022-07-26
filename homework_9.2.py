book = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
        [98762, 'Programming Python, Mark Lutz', 5, 56.80],
        [77226, 'Head First Python, Paul Barry', 3, 32.95],
        [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

# book_tuple = []
#
# for i in book:
#     n = i[0]
#     if i[2] * i[3] < 100:
#         s = (i[3] + 10) * i[2]
#     else:
#         s = i[2] * i[3]
#     s = round(s, 2)
#     book_tuple.append((n, s))
#
# print(book_tuple)

book_1 = list(map(lambda x: (x[3] + 10) * x[2] if x[2]*x[3] < 100 else x[2]*x[3], book))
book_2 = list(map(lambda x: round(x, 2), book_1))
book_3 = list(map(lambda x, y: (x[0], y), book, book_2))

print(book_3)

# еще один вариант
book_tuple = []

list(map(lambda x: book_tuple.append((x[0], round((x[3] + 10) * x[2], 2))) if x[2] * x[3] < 100
else book_tuple.append((x[0], round(x[2] * x[3], 2))), book ))

print(book_tuple)