favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}

user_name = ['vitalii', 'andrew', 'phil', 'edward', 'jen']

for user in user_name:
    print(f'\nHi {user.title()}!')
    if user in favorite_languages.keys():
        print(f'Спасибо за участие в опросе.')
    else:
        print(f'{user.title()} пройдите пожалуйста опрос.')
