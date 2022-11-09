def Square(x):
    return x*x

def IsBigger(x,y):
    return x > y

def SumAll(num_list):
    total = 0
    for i in range(len(num_list)):
        total = total + num_list[i]
    return total

def MinMax(num_list):
    Min, Max = num_list[0], num_list[0]
    for i in range(len(num_list)):
        if num_list[i] < Min:
            Min = num_list[i]
        if num_list[i] > Max:
            Max = num_list[i]
    return Min,Max

def Max(a,b):
    if a > b:
        return a
    else:
        return b
    
def UnableToPrint():
    return 0
    print('This will not be printed because its after return')

