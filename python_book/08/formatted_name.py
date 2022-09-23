def get_formatted_name(first_name, last_name, age=''):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#     # age = None
#     person = {'first': first_name, 'last': last_name, }
#     if age:
#         person['age'] = age
#     return person
#
#
# name = get_formatted_name("vitalii", "alita", age=39)
# print(name)

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == q:
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")