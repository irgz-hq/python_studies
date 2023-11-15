list_usernames = ['RAVENA', 'luigui', 'ADMIN', 'weza', 'patas']

for username in list_usernames:
    if username.lower() != 'admin':
        print(f'Hello {username}, thank you for logging in again')
    else:
        print(f'Hello admin, would you like to see a status report?')
