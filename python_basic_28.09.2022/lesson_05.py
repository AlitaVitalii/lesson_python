text = 'Привіт світ!'

print(text.find('і'))
print(text.find('і', 5))
print(text.find('і', 10))

print()

template = "{0} is capital of {1}. {0} is a big city.".format('London', 'Great Britain')

print(template)
print()


capital_name = 'London'
country_name = 'Great Britain'
population = 17.5

template = (
    f"{capital_name} is capital of {country_name}. {capital_name} is a big city. "
    f"It's population is {population} millions of people."
)

print(template)
print()

for i in range(1, 11):
    print(f"{i}. {i * 2}")


for i in range(1, 11):
    # print(f"{i}. {i * 2}")
    print(str(i) + '. ' + str(i * 2))

print()
list_01 = [1, 2, 3, 5, 8, 13, 21, True, "Whoa"]

list_01[1] = "Hey"

print(list_01)
print()

list_01 = [1, 2, 3, 5, 8, 13, 21, True, "Whoa"]
list_01.append(42)
print(list_01)

list_01.insert(0, "New")
print(list_01)
print()

text = "Привіт, Світ!"
print(list(text))
print(''.join(list(text)))
print()

list01 = [1, 3, 5, 8, 13]
list01.clear()
print(list01)
print()

text = "Розум це здатність адаптуватися до змін."
text_as_list = list(text)
for i in range(len(text_as_list)):
    c = text_as_list[i]
    if i % 2 == 0:
        text_as_list[i] = c.upper()
    else:
        text_as_list[i] = c.lower()
print(''.join(text_as_list))
print()

table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(table)
print()

list_01 = [1, 2, 3, 4, 5, 6]
# list_02 = []
# for i in list_01:
#     list_02.append(i * 2)
list_02 = [i * 2 for i in list_01]
print(list_02)

text = "Привіт, Світ!"
print(''.join([c * 2 for c in text]))
print()

list_01 = [1, 2, 3, 4, 5, 6]
# list_02 = []
# for i in list_01:
#     if i % 2 != 0:
#         list_02.append(i)
list_02 = [i for i in list_01 if i % 2 != 0]
print(list_02)
