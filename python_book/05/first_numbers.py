for i in range(5):
    print(i)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for i in range(1,11):
    squares.append(i**2)
    # square = i**2
    # squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

sq = [i**2 for i in range(1, 11)]
print(sq)