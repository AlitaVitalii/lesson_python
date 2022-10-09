# for i in range(10, 0, -1):
#     print(i)
#
# love = '💞'
#
# print(ord(love))
#
# print(chr(128158))
#
# for c in range(ord(love), ord(love) + 100):
#     print(chr(c))


text = 'Hellow world'
print(text.split(' '))

words = ["hey", "ho", "lalaley"]
print(' - '.join(words))

print("_____".join(["hey", "ho", "lalaley"]))

separator = "+++"
print(separator.join(words))

#isdigit / isalpha / isalnum / isascii / islower / isupper / isspace

text = "___привіт світ_____"

print('>' + text.strip('_') + '<')


text = "          привіт світ    "
print(text.strip().replace('т', 'д').upper())



lower / upper / title / capitalize

isdigit / isalpha / isalnum / isascii / islower / isupper / isspace

strip / lstrip / rstrip

ljust / rjust / center / zfill
"""

text = "          привіт світ    "

result = (
    text
    .strip()
    .replace('т', 'д')
    .upper()
)

print(result)

