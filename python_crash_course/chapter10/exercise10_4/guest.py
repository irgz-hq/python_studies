from pathlib import Path
name = input("Say your name: ")

path = Path("python_crash_course/chapter10/exercise10_4/guest.txt")
path.write_text(name)
