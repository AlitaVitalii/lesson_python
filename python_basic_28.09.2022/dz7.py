# text = "Розум ЦЕ здатність адаптуватися до змін."
text = input("Введіть текст: ")
counter = 0
# new_text = ""
for t in text:
    counter += 1
    if counter % 2 == 0:
        print(t.lower(), end="")
    else:
        print(t.upper(), end="")
