# alien_color = 'red'
# if alien_color == 'green':
#     print("+5$")
# elif alien_color == "yellow":
#     print("+10$")
# elif alien_color == "red":
#     print("+15$")

##

age = int(input("How old are you? - "))

if age < 2:
    print("младенец")
elif 4 > age >= 2:
    print("малыш")
elif 13 > age >= 4:
    print("ребенок")
elif 20 > age >= 13:
    print("подросток")
elif 65 > age >= 20:
    print("взрослій")
else:
    print("пожилой человек")
