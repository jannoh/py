#!/usr/bin/python

answer = input('Enter yes/y or no/n: ')

if answer.lower() == 'yes' or answer.lower() == 'y':
    print("Agreed")
elif answer == 'no' or answer.lower() == 'n':
    print('Disagreed')
else:
    print('Provided valid input!')