from datetime import datetime, date, timedelta

now = datetime.now()

tomorrow = datetime(2022, 11, 13)

print(tomorrow)
print(now.strftime('%Y-%m-%d'))

print(tomorrow + timedelta(days=134))



