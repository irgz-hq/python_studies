cubes = [i**3 for i in range (1, 11)]
first_cubes = cubes[:3]
mid = int(len(cubes)/2)
mid_cubes = cubes[mid-1:mid+2]
last_cubes = cubes[-3:]

print(cubes)
print(f"The first three items in the list are: {first_cubes}")
print(f"Three items from the middle of the list are {mid_cubes}")
print(f"The last three items in the list are: {last_cubes}")