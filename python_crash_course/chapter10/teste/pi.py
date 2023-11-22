from pathlib import Path

path = Path("python_crash_course/chapter10/teste/pi_digits.txt")
print(path)
contents = path.read_text() + "\n"
contents = contents.rstrip().splitlines()
print(contents)
