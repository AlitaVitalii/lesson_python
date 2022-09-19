user_1 = {
    'first_name': 'vitalii',
    'last_name': 'alita',
    'age': '39',
    'citi': 'kyiv'
}
user_2 = {
    'first_name': 'fed',
    'last_name': 'zabkin',
    'age': '39',
    'citi': 'zaporizhzhya'
}
user_3 = {
    'first_name': 'andrew',
    'last_name': 'bondarev',
    'age': '39',
    'citi': 'kherson'
}

users = [user_1, user_2, user_3]

for user in users:
    print(f"\nFull name: {user['first_name'].title()} {user['last_name'].title()}")
    print(f"\tLocation: {user['citi'].title()},  age: {user['age']}")

