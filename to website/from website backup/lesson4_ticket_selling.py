# Ticket selling system

money = float(input('How much you have: '))
print('Originally the user have: ',money)
age = int(input('How old are you: '))
print('The age of the user: ',age)

if age >=0 and age <= 120: # Check if age make sense
    if 15 < age and age < 60:
        money = money - 50 # Ticket price $50
    if age >= 60:
        money = money - 20 # Ticket price $20
    if age <= 15:
        money = money - 16 # Ticket price $15
    print('Change: ',money) # Output change
else:
    print('Invalid age!')
