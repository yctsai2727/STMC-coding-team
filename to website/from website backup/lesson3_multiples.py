# Multiples of 3 from 1 to 100

count3 = 0 # No. of multiples of 3
for i in range(100):
    # Make i range becomes 1 to 100 instead of 0 to 99
    n = i+1 
    if n % 3 == 0: # If n is multiple of 3
        count3 = count3 + 1
        #print(f'{n} is the {count3}th multiple of 3')
print('There are total ',count3,' multiples of 3')


print('\n\n')
count15 = 0
for i in range(100):
    n = i+1
    if n % 3 == 0 and n % 5 == 0:
        count15 = count15 + 1
        print(f'{n} is the {count15}th multiple of 15')
        
print('There are total ',count15,' multiples of 15')


print('\n\n')

