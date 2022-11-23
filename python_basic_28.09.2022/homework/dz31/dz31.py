my_dict = {}

# with open('111.txt', encoding='utf-8') as f:
#     for line in f.readlines():
#         for word in line.split():
#             correct_word = "".join([i for i in word if i.isalpha()]).lower()
#             if len(correct_word) >= 5:
#                 try:
#                     my_dict[correct_word] += 1
#                 except KeyError:
#                     my_dict[correct_word] = 1
#             # print(correct_word)
# # sorted(my_dict.values())
# print(sorted(my_dict.items(), key=lambda row: row[1], reverse=True))

# f = open('bible.txt')
#
# for line in f.readlines():
#     print(line.rstrip('\n'))

import numpy as np

print(np.fromfile('test'))

#
# file = open('test', 'br')
# for row in file:
#     print(row)
#
