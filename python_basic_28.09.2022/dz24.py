text = input("Введіть набір цілих чисел, розділених комою: ")

my_list = [int(i) for i in text.split(',')]


print('- суму введених чисел: ', sum(my_list))
print('- середнє арифметичне введених: ', sum(my_list)/len(my_list))
print('- кількість парних чисел: ',
      len([i for i in my_list if i % 2 == 0]))
print('- кількість непарних чисел: ',
      len([i for i in my_list if i % 2 != 0]))
print('- найбільше число: ', max(my_list))
print('- найменше число: ', min(my_list))
