from pathlib import Path

path_dog = Path("spython_crash_course/chapter10/exercise10_8/dog_names.txt")
path_cat = Path("python_crash_course/chapter10/exercise10_8/cat_names.txt")

try:
    dog_names = path_dog.read_text(encoding="utf-8")
    
except FileNotFoundError:
    pass

else:

    print(f"The dogs contents is: \n{dog_names}\n")

    try:
        cat_names = path_cat.read_text(encoding="utf-8")

    except FileNotFoundError:
        pass

    else:
        
        print(f"The cats contents is: \n{cat_names}")