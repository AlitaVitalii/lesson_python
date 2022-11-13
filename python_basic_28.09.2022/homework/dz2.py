num_apl = int(input("Введіть кількість яблук: "))
num_user = int(input("Введіть кількість дітей: "))

apl_user = num_apl // num_user
ost = num_apl % num_user

print("Кожна дитина отримає яблук: ", apl_user)
print("Залишиться яблук: ", ost)
