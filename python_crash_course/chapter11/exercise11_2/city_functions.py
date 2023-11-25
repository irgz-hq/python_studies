"""def city_country(city, country, population):
    string = f"{city.title()}, {country.title()} - population {population}"
    return string"""


def city_country(city, country, population=''):
    if population:
        string = f"{city.title()}, {country.title()} - population {population}"
    else:
        string = f"{city}, {country}".title()
    return string