my_list = ['Andrew', 'Fedor', 'gennadii']
print(f'Wellcome on the bee-garden: {my_list[0]}, {my_list[1]}, {my_list[2].title()} ')
#print(f'Wellcome on the bee-garden {my_list[1]}')
#print(f'Wellcome on the bee-garden {my_list[2].title()}')

popedname = my_list.pop(0)
my_list.append('valik')
print(f'Wellcome on the bee-garden: {my_list[0]}, {my_list[1].title()}, {my_list[2].title()}')
print(f'{popedname.title()} not on the meeting')

my_list.insert(0, "Tanya")
my_list.insert(1, 'Masha')
my_list.append('Oksana')
print(my_list)
print(f'всего гостей - {len(my_list)}')