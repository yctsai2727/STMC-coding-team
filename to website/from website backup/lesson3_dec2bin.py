# Decimal to binary

num = int(input('Enter number: '))

digits = []
bi = num

while bi != 0:
    ai = bi % 2
    bi = (bi-ai)//2
    digits.append(ai)

# Print the digits in reverse
for i in range(len(digits)-1,-1,-1):
    print(digits[i],end='')
