text = input("Введіть текст: ")

count = 0
half_len = int(len(text) / 2)

for i in range(half_len + 1):
    count += 1
    if len(text) % 2 == 0 and count <= half_len:
        print(" " * (half_len - count), text[half_len - count: half_len + count])
    elif len(text) % 2 > 0:
        if count == 1:
            print(" " * (half_len - count + 1), text[half_len])
        else:
            print(" " * (half_len - count + 1), text[half_len - count + 1: half_len + count])




