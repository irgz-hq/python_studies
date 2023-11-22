from pathlib import Path

path = Path("python_crash_course/chapter10/exercise10_2/learning_python.txt")
contents_all = path.read_text()
contents_all = contents_all.replace('Python', 'C')
print(contents_all)
print('-->fic<--')
