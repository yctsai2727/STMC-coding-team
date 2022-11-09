arr = [-1,2,4,-3,5,2,-5,2,19,2,4]
N = len(arr)

max_sum = arr[0] # Current largest sum
max_start = 0
max_end = 0 

for start in range(0,N):
    for end in range(start,N):
        total = sum(arr[start:end+1])
        if total > max_sum:
            max_sum = total
            max_start = start
            max_end = end

print('The maximum subarray sum is ',max_sum)
print('This subarray starts at ',max_start,' ends at ',max_end)
print(arr[max_start:max_end+1])
