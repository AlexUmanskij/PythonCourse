def day_converter(years, months):
    days = years*365+months*29
    return days

year1 = 1
month1 = 5
print(day_converter(year1,month1))