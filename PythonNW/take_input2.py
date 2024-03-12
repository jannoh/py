import getpass, sys

username = input('Enter username: ')
password = getpass.getpass(stream=sys.stderr)

print(f'Your username is {username}\nYour password is hidden.')