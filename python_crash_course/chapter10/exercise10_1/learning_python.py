from pathlib import Path

path = Path("python_crash_course/chapter10/exercise10_1/learning_python.txt")
contents_all = path.read_text()
contents_lines = path.read_text()
contents_lines = contents_lines.splitlines()
print(contents_all)
print("###################")
for lines in contents_lines:
    print(lines)