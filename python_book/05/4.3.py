for num in range(1,21):
    print(num)
print('the end')
print()

# my_list = [num for num in range(1,1000001)]
# print(my_list)
my_list = []
for i in range(1, 1000001):
    my_list.append(i)
print(min(my_list))
print(max(my_list))
print(sum(my_list))

my_list2 = [num**3 for num in range(1, 10)]
for i in my_list2:
    print(i)
