ScoreList = []

n = int(input('How many entries you want to enter:'))

for i in range(n):
  score = float(input('Enter a score: '))
  ScoreList.append(score)
  print(ScoreList)

sum = 0
for i in range(0,len(ScoreList)):
  sum = sum + ScoreList[i]

print(sum)

