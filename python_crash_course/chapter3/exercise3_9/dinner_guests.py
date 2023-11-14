names = ["Weza", "Patas", "Taigaz"]
names[-1] = "Trailas"
print(f"Hey man, you, {names[0]}, were invited to dinner")
print(f"Hey man, you, {names[1]}, were invited to dinner")
print(f"Hey man, you, {names[-1]}, were invited to dinner")
print(f"number of people invited {len(names)}")

names.insert(1, 'trilouca')
names.insert(2, 'treloso')
names.append('zé da manga')
print(f"Hey man, you, {names[1]}, were invited to dinner")
print(f"Hey man, you, {names[2]}, were invited to dinner")
print(f"Hey man, you, {names[-1]}, were invited to dinner")
print(f"number of people invited {len(names)}")

print("Sorry, i can only invite two people")

print(f'Sorry {names.pop()}.')
print(f'Sorry {names.pop()}.')
print(f'Sorry {names.pop()}.')
print(f'Sorry {names.pop()}.')
print(names)
print(f"number of people invited {len(names)}")
del names[0]
del names[0]
print(names)