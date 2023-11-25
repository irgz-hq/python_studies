from city_functions import city_country

def test_city_country_population():
    string = city_country("santiago", "chile", 5000000)
    assert string == "Santiago, Chile - population 5000000"