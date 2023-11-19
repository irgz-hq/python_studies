def items(*args):
    for item in args:
        print(f"- {item}")

items("onion", "chicken", "cheese")
print()
items("ham")
print()
items("chesse", "picles")