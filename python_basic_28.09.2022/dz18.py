text = 'qwertyu'

count = 1
list_text = list(text)


for i in range(int(len(list_text)/2)):
    # if len(list_text) % 2 == 0:
    print(" " * (int(len(list_text)/2-count)), text[int(len(list_text)/2-count): int(len(list_text)/2+count)])
    count += 1




