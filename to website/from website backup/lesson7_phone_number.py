phoneNumber = input()

start = phoneNumber[0]

if start == '2' or start == '3':
    print('Fixed')
elif start == '5' or start == '6' or start == '9':
    print('Mobile')
