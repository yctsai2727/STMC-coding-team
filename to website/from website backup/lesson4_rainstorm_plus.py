# Rain storm signal issuing

rainfall = float(input('Enter rainfall: '))

if rainfall < 0:
    print('ERROR: Rainfall cannot be < 0')
elif rainfall < 30:
    print('NO SIGNAL!')
elif rainfall < 50:
    print('AMBER')
elif rainfall < 70:
    print('RED')
else:
    print('BLACK')
    
print('End of program')