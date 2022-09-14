motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'zaz')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_mot = motorcycles.pop()
print(motorcycles)
print(popped_mot)

motorcycles.remove('suzuki')
print(motorcycles)