# text = "Для того, щоби грибок відступив назавжди, назавждитреба взяти простий радянський..."
text = input("Введіть текст: ")


print(text.replace('З', '3')
      .replace('О', '0')
      .replace('и', 'u')
      .replace('т', 'm')
      .replace('к', 'k')
      .replace('д', 'g'))