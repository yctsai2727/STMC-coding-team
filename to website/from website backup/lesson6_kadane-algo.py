arr = [-2,-3,4,-1,-2,1,5,-3,1,3,1,-4,2]

endAtIBest = arr[0]
wholeArrBest = arr[0]

for i in range(1,len(arr)):
    if endAtIBest + arr[i] > arr[i]:
        endAtIBest = endAtIBest + arr[i]
    else:
        endAtIBest = arr[i]

    print(endAtIBest)

    if wholeArrBest < endAtIBest:
        wholeArrBest = endAtIBest

print('The largest sum ', wholeArrBest)
    
