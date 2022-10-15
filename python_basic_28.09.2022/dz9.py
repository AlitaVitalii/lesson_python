# text = '100,190,80,300,240,50,340,550,200,210'
text = input('Введіть інформацію про статки мешканців вулиці (через кому): ')
my_list = [int(i) for i in text.split(',')]

print("Мажори:")
for index in range(1, len(my_list)-1):
    if my_list[index] > my_list[index-1] + my_list[index+1]:
        print(f'{index+1}. {my_list[index]}')
