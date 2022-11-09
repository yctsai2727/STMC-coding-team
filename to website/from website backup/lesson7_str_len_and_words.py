string = input()

# Python-specific ways
lengthStr = len(string)
lengthWord = len(string.split(' '))
print(lengthStr)
print(lengthWord)

# More general way:
lengthStr = len(string)
lengthWord = 1
for i in range(lengthStr):
    if string[i] == ' ':
        lengthWord = lengthWord + 1
print(lengthStr)
print(lengthWord)
