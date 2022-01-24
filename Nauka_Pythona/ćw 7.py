#slicing

name = "Karolina Wychocka"

first_name = name[0:8]
last_name = name[9:17]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website = "http://google.com"
website2 = "http://facebook.com"

slice = slice(7,-4)

print(website[slice])
print(website2[slice])
