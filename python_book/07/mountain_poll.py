responses = {}
active = True

while active:
    name = input('\nWhat is you name?')
    response = input('How old are you')
    responses[name] = response

    repeat  = input('Would you like to let another person respond? (yes / no)')
    if repeat == 'no':
        active = False

print('\n--- Roll Results ---')
for name, response in responses.items():
    print(f"{name.title()} is {response} years old")