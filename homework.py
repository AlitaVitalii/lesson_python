a = 123
b = a % 10 * 100
c = a % 100 - a % 10
d = (a - a % 100)/100

print(int(b+c+d))