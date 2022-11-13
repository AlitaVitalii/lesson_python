def is_leap_year(year_):
    return True if year_ % 400 == 0 or year_ % 4 == 0 and year_ % 100 != 0 else False


years = [1900, 1904, 1905, 2000, 2001, 2004, 2100, 2024]

for year in years:
    print(year, "високосний" if is_leap_year(year) else "не високосний")

