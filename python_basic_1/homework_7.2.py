text = 'Hello! helloword! python, hello python ithillel python'
mylist = text.lower().split()
mylist2 = []
for word in mylist:
    mylist2.append(word.strip("!,.?:;"))

word_dict = dict.fromkeys(mylist2)

for key in word_dict.keys():
    word_dict[key] = mylist2.count(key)

for k, v in word_dict.items():
    print(f'{k} из текста "text": количество повторов {v}')

