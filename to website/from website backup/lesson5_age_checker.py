age = int(input('Enter your age: '))

# Check age >0 and < 120
while not( age > 0 and age < 500):
    print('Age should be 0 < x < 500')
    age = int(input('Re-enter your age: '))

print('Ok. You age is: ',age)

    