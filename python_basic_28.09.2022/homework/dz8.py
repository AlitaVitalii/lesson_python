text = "Для того, щоби грибок відступив назавжди, треба взяти простий радянський..."
# text = input("Введіть текст: ")
# for t in text:
#     if t == "З":
#         print("3", end="")
#     elif t == "О":
#         print("0", end="")
#     elif t == "и":
#         print("u", end="")
#     elif t == "т":
#         print("m", end="")
#     elif t == "к":
#         print("k", end="")
#     elif t == "д":
#         print("g", end="")
#     else:
#         print(t, end="")

print(text.replace('З', '3').replace('О', '0').replace('и', 'u').replace('т', 'm').replace('к', 'k').replace('д', 'g'))