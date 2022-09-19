favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',

}
#
# languages = favorite_languages['sarah'].title()
# print(f"Sarah's favorite languages is {languages}.")
# print()
#
# for name, lang in favorite_languages.items():
#     print(f"{name.title()}'s favorite languages is {lang.title()}.")
# print()

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f'Hi {name.title()}')

    if name in friends:
        langg = favorite_languages[name]
        print(f'\t{name.title()}, I see you love {langg}')
print()

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
print()

print('группа знает такие языки программировнаия:')
for lang in set(favorite_languages.values()):
    print(lang.title())

