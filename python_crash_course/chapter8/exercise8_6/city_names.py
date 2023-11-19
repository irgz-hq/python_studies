def city_country(city, country):
    return f"{city}, {country}"

maceio = city_country("Maceió", "Brasil")
pequim = city_country("Pequim", "China")
nova_york = city_country("Nova York", "EUA")

cities = [maceio, pequim, nova_york]

for city in cities:
    print(city)