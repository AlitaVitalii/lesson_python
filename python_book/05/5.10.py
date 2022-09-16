current_users = ['admin', 'vitalii', 'andrew', 'fed', 'gena', 'inna']
new_users = ['Vitalii', 'andrew', 'tanya', 'sofiya']

for name in new_users:
    if name.lower() in current_users:
        print(f"выбери новое имя, {name} занято")
    else:
        print(f"{name} имя доступно")