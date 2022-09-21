prompt = '\nPlease enter the name of citi you have visited:'
prompt += '\n(Enter "quit" when you are finished.)'

while True:
    citi = input(prompt)
    if citi == 'quit':
        break
    else:
        print(f"I'd love to go to {citi.title()}!")

print("the end")