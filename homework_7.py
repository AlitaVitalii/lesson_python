text = 'Hello! helloword! python, hello python ithillel python'
mylist = text.lower().split()
mylist2 = []
for word in mylist:
    mylist2.append(word.strip("!,.?:;"))

word_dict = dict.fromkeys(mylist2)

# for key in word_dict.keys():
#     word_dict[key] = mylist2.count(key)


num = 0
for i in range(len(mylist2)):
    if mylist2[i] == word_dict[mylist2[i]]:
        word_dict[mylist2[i]] = num
        num += 1

print(word_dict)
