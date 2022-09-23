def greet_users(names):
    for name in names:
        msg = f"Hello , {name.title()}"
        print(msg)


username = ['sofiya', 'anna', 'duo']
greet_users(username)
