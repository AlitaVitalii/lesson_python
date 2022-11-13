my_dict = {}
word = ''
with open(input("Введіть ім’я файлу: ")) as f:
    for line in f.readlines():
        for symbol in line:
            if symbol.isalpha():
                word += symbol.lower()
            else:
                if len(word) >= 5:
                    if my_dict.get(word):
                        my_dict[word] += 1
                        word = ''
                    else:
                        my_dict[word] = 1
                        word = ''
                else:
                    word = ''


print('Найпопулярніші слова:')

for i, kv in enumerate(sorted(my_dict.items(), key=lambda row: row[1], reverse=True)):
    if i < 5:
        print(*kv)
