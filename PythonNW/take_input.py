#!/usr/bin/python

answer = ''

while len(answer) == 0:
    answer = input('Enter yes/y or no/n: ').lower()

if answer == 'yes' or answer == 'y':
    print("Agreed")
elif answer == 'no' or answer == 'n':
    print('Disagreed')
else:
    print('Provided valid input!')