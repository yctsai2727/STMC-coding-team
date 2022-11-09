count3 = 0
count5 = 0
count15 = 0

for i in range(20):
    n = i+1
    if n % 3 == 0: # If n is multiple of 3
        count3 = count3 + 1
        print(f'{n} is the {count3}th multiple of 3')
    if n % 5 == 0: # If n is multiple of 5
        count5 = count5 + 1
        print(f'{n} is the {count5}th multiple of 5')
    if n % 15 == 0: # If n is multiple of 15
        count15 = count15 +1

print(count3+count5-count15)
