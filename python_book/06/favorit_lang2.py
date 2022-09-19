favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],

}
for name, lang in favorite_languages.items():
    if len(lang) > 1:
        print(f'\n{name.title()}"s favorite languages are:')
        for lan in lang:
            print(f'\t{lan.title()}')
    else:
        print(f"\n{name.title()}'s favorite language is {lang.title()}")