from pathlib import Path

path = Path("python_crash_course/chapter10/exercise10_3/learning_python.txt")
contents = path.read_text()

for lines in contents.splitlines():
    print(lines)