strFare = input()
floatFare = float(strFare[1:]) # Slice away $ and convert to float
intFare = int(floatFare*10) # Shift digit

if intFare % 2 == 0: # If intFare is even
    halfFare = intFare // 2
else: # If intFare is odd
    halfFare = intFare // 2 + 1
    
print(f'${halfFare/10}')
