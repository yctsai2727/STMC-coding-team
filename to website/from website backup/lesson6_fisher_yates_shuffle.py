import random

letters = [1,2,3,4]
N = len(letters)

for i in range(0,N-1):
    k = random.randint(i,N-1)
    print(i,'th round')
    print('Picked ',k)
    print('Before: ',letters)
    temp = letters[k]
    letters[k] = letters[i]
    letters[i] = temp
    print('After: ',letters)

print('Fianlly:', letters)
