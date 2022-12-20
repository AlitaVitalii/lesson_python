def greet_user(user):
    return user.title()




while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = greet_user(f'{f_name} {l_name}')
    print(f'\nHello, {formatted_name}')