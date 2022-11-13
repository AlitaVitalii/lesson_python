text = input('Введіть дату народження (у форматі YYYY-MM-DD): ')

from datetime import datetime


dt = datetime.strptime(text, '%Y-%m-%d')
now = datetime.now()

result = now - dt

print(f'Сьогодні вам виповнилося {result.days} днів.')
