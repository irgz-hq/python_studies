names = ["Weza", "Patas", "Taigaz"]
names[-1] = "Trailas"
print(f"Hey man, you, {names[0]}, were invited to dinner")
print(f"Hey man, you, {names[1]}, were invited to dinner")
print(f"Hey man, you, {names[-1]}, were invited to dinner")

names.insert(1, 'trilouca')
names.insert(2, 'treloso')
names.append('zé da manga')
print(f"Hey man, you, {names[1]}, were invited to dinner")
print(f"Hey man, you, {names[2]}, were invited to dinner")
print(f"Hey man, you, {names[-1]}, were invited to dinner")