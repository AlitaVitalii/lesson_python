# f = open('.txt')
#
# for line in f.readlines():
#     print(line, end='')
#
# f.close()

print('---------------------1')

with open('xo.txt') as f:
    for line in f.readlines():
        print(line.encode(), end='')

# print('----------------------2')
#
# with open('output.txt', 'w') as f:
#     f.write("Hello, World!\n")
#
# with open('output.txt', 'a') as f:
#     f.write("How are you?\n")
#
# print('----------------------3')
#
# with open('output.txt', 'w') as f:
#     f.writelines(["Hello, World!\n", "How are you?\n"])
#
# print('-----------------------4')
#
import json

state = {
    'board': [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', 'x', 'o']
    ],
    'next_move': 'x',
    'game_over': False,
}

print(
    json.loads(
        json.dumps(state, indent=4)
    )
)

print('----------------------------5')

import os

print(os.listdir('C:\\'))
print(os.getcwd())

print('------------------------------6')

from datetime import datetime
import os

for name in os.listdir():
    print(
        name,                       # ім'я
        os.path.getsize(name),      # розмір
        'dir' if os.path.isdir(name) else 'file',
        datetime.fromtimestamp(os.path.getctime(name)),  # час створення
        datetime.fromtimestamp(os.path.getmtime(name)),  # час модифікації
    )


print('-----------------------------7')

import os

print(os.path.join('Users', 'ipomar', 'PycharmProjects'))

print(os.path.exists('lesson_13.py'))
print(os.path.exists('foo'))

print('-----------------------------8')

import os

os.remove('output.txt')  # del

print('----------------------------9')

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Ouch!")

print('-----------------10')

try:
    a = 1 / 0
    b = [][42]
except ZeroDivisionError:
    print("Ouch!")
except IndexError:
    print("Whoa!")

print('-------------------11')

try:
    a = 1 / 0
    b = [][42]
except (ZeroDivisionError, IndexError):
    print("Ouch! (or Whoa!?)")

print('--------------------12')
try:
    a = 1 / 0
    b = [][42]
except Exception:  # ACHTUNG! ATTENTION! NOT RECOMMENDED!!!
    print("Ouch! (or Whoa!?)")

print('--------------------13')

try:
    a = 1 / 0
    # b = [][42]
except (IndexError, ZeroDivisionError):
    print("Ouch! (or Whoa!?)")
else:
    print("Everytning is fine.")
finally:
    print("Finally, everything has ended.")

print('----------------------14')

try:
    a = 1 / 0
    # b = [][42]
except (IndexError, ZeroDivisionError) as e:
    print("Ouch! (or Whoa!?)", e)

print('----------------------15')

try:
    raise RuntimeError("Incorrect value")
except (IndexError, ZeroDivisionError, ValueError) as e:
    print("Ouch! (or Whoa!?)", e)

print('----------------------16')

# try:
#     raise RuntimeError("Incorrect value")
# except (IndexError, ZeroDivisionError, RuntimeError) as e:
#     print("Ouch! (or Whoa!?)", e)
#     raise

print('------------------17')


