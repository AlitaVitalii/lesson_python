# morse_cod = '--. --- -..    ... .- ...- .    - .... .    --.- ..- . . -.'
morse_cod = '.-    .-..... --- -    --- ..-.    -. --- .. -.-. .    --- -.    - .... .. .......    ..-. .-. . --.- ..- . -. -.-. -.-- '

morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}
morse_dict_revers = {v: k for k, v in morse_dict.items()}

list_01 = morse_cod.split('  ')

list_word = []
for cod_word in list_01:
    symbol_list = cod_word.split()
    word = ''
    for s in symbol_list:
        if s in morse_dict_revers.keys():
            word += morse_dict_revers[s]
        else:
            word += '~'

    list_word.append(word)

print(' '.join(list_word))