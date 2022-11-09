myString = 'Information HAHA 1;Information2;Information3;'

start = 0
currentString = myString

while len(currentString) != 0:
    end = currentString.find(';')
    targetStr = currentString[:end]
    #print(end)
    print(targetStr)
    start = end+1
    currentString = currentString[start:]
    #print(currentString)
    #input()
