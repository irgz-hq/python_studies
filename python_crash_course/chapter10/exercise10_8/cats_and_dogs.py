from pathlib import Path

path_dog = Path("python_crash_course/chapter10/exercise10_8/dog_names.txt")
path_cat = Path("python_crash_course/chapter10/exercise10_8/cat_names.txt")

try:
    dog_names = path_dog.read_text(encoding="utf-8")
    
except FileNotFoundError:
    print(f"The file path {path_dog} doesn't exist")

else:

    try:
        cat_names = path_cat.read_text(encoding="utf-8")

    except FileNotFoundError:
        print(f"The file path {path_cat} doesn't exist")

    else:
        
        print(f"The dogs contents is {dog_names}\n")
        print(f"The cats contents is {cat_names}")