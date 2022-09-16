# my_list = ['admin', 'vitalii', 'andrew', 'fed', 'gena', 'inna']
my_list = []
if my_list:
    for name in my_list:
        if name == 'admin':
            print(f'Hello admin, would like to see status report?')
        else:
            print(f'Hello {name.title()}, thank you for logging in again')
else:
    print("We need to ind some users")
