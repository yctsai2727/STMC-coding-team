# Sum of first N integers (i.e. 1+2+3+...+N = ?)

N = int(input('Enter N: '))
S = 0
i = 1
# Just to see what a loop do
while i<=N:
    S = S + i
    i = i + 1
print('Final sum: ',S)