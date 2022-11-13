my_dict = {}
# word = ''
with open('bible.txt', encoding='utf-8') as f:
    for line in f.readlines():
        for word in line.split():
            correct_word = "".join([i for i in word if i.isalpha()]).lower()
            if len(correct_word) >= 5:
                if my_dict.get(correct_word):
                    my_dict[correct_word] += 1
                else:
                    my_dict[correct_word] = 1
            # print(correct_word)
# sorted(my_dict.values())
# print(sorted(my_dict.items(), key=lambda row: row[1], reverse=True))

count = 0
for k, v in enumerate(sorted(my_dict.items(), key=lambda row: row[1], reverse=True)):
    if count < 5:
        count += 1
        print(*v)

# f = open('bible.txt')
#
# for line in f.readlines():
#     print(line.rstrip('\n'))

# file = open('bible.txt', encoding='utf-8')
# for row in file:
#     print(row)

