print("Exemples of conditional tests:")
car = "BMW"
print(f"{car} == BMW?", car == "BMW")
print(f"{car} == bmw?", car == "bmw")

print(f"{car.lower()} == BMW?", car.lower() == "BMW")
print(f"{car.lower()} == bmw?", car.lower() == "bmw")

print("1 == 1.0?", 1 == 1.0)
print("1.0 == 2?", 1.0 == 2)

print("1 != 1.0?", 1 != 1.0)
print("1.0 != 2?", 1.0 != 2)

print("1 != 1.0 and 1.0 != 2?", 1 != 1.0 and 1.0 != 2)
print("1 == 1.0 and 2.0 == 2?", 1 == 1.0 and 2.0 == 2)

list_number = [1,2,3,4]

print(f"1 in {list_number}?", 1 in list_number)
print(f"5 in {list_number}?", 5 in list_number)

print(f"1 not in {list_number}?", 1 not in list_number)
print(f"5 not in {list_number}?", 5 not in list_number)