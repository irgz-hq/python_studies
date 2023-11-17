rivers = {
    'nile': 'egypt',
    'são francisco': 'brasil',
    'yangtzé': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
print()
for river in rivers.keys():
    print(river)
print()
for country in rivers.values():
    print(country)