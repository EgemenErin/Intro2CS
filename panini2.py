city = ('Poznan, Poland; 52,41; 16,93', 'Warsaw, Poland; 52,23; 21,01', 'Krakow, Poland; 50,06; 19,94', 'Gdansk, Poland; 54,35; 18,65')
print(city[1])
print(city[-1])
print(type(city))
poznan, warsaw, krakow, gdansk = city
print(poznan)
print(warsaw)
city_list = list(city)
new_country = "Brazil"  # whatever you want

s = city_list[0]
before_semi, rest = s.split(";", 1)
city_name, _old = before_semi.rsplit(", ", 1)
city_list[0] = f"{city_name}, {new_country};{rest}"

city = tuple(city_list)
print(city)