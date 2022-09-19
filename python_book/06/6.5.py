my_river = {
    'nile': 'egypt',
    'dnepr': 'ukrainian',
    'amazonka': 'eqador'

}

for k, v in my_river.items():
    print(f'Tne {k.title()} runs through {v.title()}.')
print()

print('Rivers:')
for river in my_river.keys():
    print(river.title())
print()
print("Uneted:")
for un in my_river.values():
    print(un.title())
