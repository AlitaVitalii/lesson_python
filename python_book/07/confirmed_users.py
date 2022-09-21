unconfirmed_users = ['alica', 'brian', 'fed']
confirmed_users = []

while unconfirmed_users:
    concurrent_user = unconfirmed_users.pop()
    print(f"Verifying user: {concurrent_user.title()}")
    confirmed_users.append(concurrent_user)

print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())