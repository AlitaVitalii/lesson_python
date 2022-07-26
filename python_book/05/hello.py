users = ['admin', 'fed', 'andrew', 'gena', 'vitalii', 'mon100r']
# # users = []
# if users:
#     for user in users:
#         if user == 'admin':
#             print('Hello admin, would you like to see a status report?')
#         else:
#             print(f"Hello {user.title()}, thank yot for logging in again")
# else:
#     print('We need to ind some users!')

new_users = ['fed', 'Vitalii', 'yurec', 'sashko', 'vova']

for user in new_users:
    if user.lower() in users:
        print(f'Имя {user.title()} уже занято, выберите новое имя.')
    else:
        print(f'Имя {user.title()} свободно!')