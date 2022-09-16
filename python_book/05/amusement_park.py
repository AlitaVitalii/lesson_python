age = int(input("How old are you?  "))

# if age <= 4:
#     print('Вход беплатный!')
# elif age < 18:
#     print("Вход 25грн")
# else:
    # print("Вход 40 грн")

if age<=4:
    price = 0
elif age<18:
    price = 25
elif age < 60:
    price = 40
elif age >= 60:
    price = 20
# else:
#     price = 20
print(f'Your admission cost is ${price}.')