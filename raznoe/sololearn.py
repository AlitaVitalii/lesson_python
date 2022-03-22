# total = 0
# s = 0
# while total < 5:
#     age = int(input())
#     if age > 3:
#         s += 100
#     total += 1
#
# print(s)
ves = float(input("vvedite ves: "))
rost = float(input("vvedite rost: "))
imt = ves/rost**2

if imt < 18.5:
    print("Underweight")
elif 18.5 <= imt < 25:
    print('Normal')
elif 25 <= imt < 30:
    print("Overweight")
else:
    print('Obesity')

# print(imt)