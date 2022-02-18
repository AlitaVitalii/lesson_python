mylist = [1, 3, 5, 10, 7, 9]
k = 3
for i in range(k+1, len(mylist)):
    b = i - 1
    mylist[b] = mylist[i]
mylist.pop()
print(mylist)
