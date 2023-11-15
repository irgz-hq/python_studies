
list_usernames = ['RAVENA', 'luigui', 'ADMIN', 'weza', 'patas']
# list_usernames = []
if list_usernames:
    for username in list_usernames:
        if username.lower() != 'admin':
            print(f'Hello {username}, thank you for logging in again')
        else:
            print(f'Hello admin, would you like to see a status report?')
else:
    print('We need to find some users!')