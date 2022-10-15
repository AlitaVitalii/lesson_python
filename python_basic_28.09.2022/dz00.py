my_list = [1, 2, 3, 4, 5, 'why']

my_list.append('blah')
print(my_list)

my_list.insert(2, "two")
print(my_list)

my_list.extend(my_list)
print(my_list)

x = my_list.pop()
print(x)
print(my_list)

my_list.clear()
print(my_list)
my_list.append(x)
my_list.append(x)
print(my_list)
print(my_list.count(x))

print(my_list.index('blah', 1))
my_list.append(1)
my_list.append(2)
print(my_list)
print(my_list.index('blah'))

