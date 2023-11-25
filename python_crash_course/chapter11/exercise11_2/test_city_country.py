from city_functions import city_country

def test_city_country():
    string = city_country("santiago", "chile")
    assert string == "Santiago, Chile"