import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£%$^&*().,?0123456789'
number = input('Amount of password to generate: ')

number = int(number)

length =  input('Input your password length:')
length = int(length)

print('\n here are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
