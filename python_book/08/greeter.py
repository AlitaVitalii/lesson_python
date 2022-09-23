def greet_user(user):
    print((f'Hello, {user.title()}!'))

greet_user('vitalii')

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    l_name = input("Last name:")
    formatted_name = greet_user(f_name, l_name)
    print(f'\nHello, {formatted_name}')