lista = ['jen', 'sarah', 'edward', 'phil', 'johnny']


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in lista:
    if name in favorite_languages.keys():
        print(f"Thank you, {name}")
    else:
        print(f"Take the pool, {name}")



