# Binary to decimal

binary = input('Enter in binary: ')

decimal = 0
n = len(binary)
for i in range(n):
    if binary[i] == '1':
        decimal = decimal + 1*(2**(n-1-i))
    elif binary[i] == '0':
        decimal = decimal + 0 * (2**(n-1-i)) # Can omit
    else:
        print('Error: Digits can only be 0 or 1')

print(decimal)
