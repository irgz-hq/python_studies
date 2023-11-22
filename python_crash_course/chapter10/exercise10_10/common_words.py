from pathlib import Path

path = Path("python_crash_course/chapter10/exercise10_10/dracula.txt")

contents = path.read_text()
counter = contents.lower().count("the")
counter2 = contents.lower().count("the ")

print(counter, counter2)