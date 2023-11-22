from pathlib import Path

list_name = []
while True:
    name = input("Say your name or q to exit the program: ")
    if name == 'q':
        break
    list_name.append(name)


path = Path("python_crash_course/chapter10/exercise10_5/guest.txt")
names = ""
for name in list_name:
    names += name+"\n"

path.write_text(names.strip())
