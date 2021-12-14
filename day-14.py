import copy
import operator
from collections import defaultdict

with open("input-14.txt", "r") as f:
  polymer = f.readline().strip ()
  f.readline()
  rules = {line[0] : line[1] for l in f.readlines() if (line := l.strip().split(' -> ')) != ''}

def growPolymer(polymerCounts):
  newCounts = defaultdict(int)
  for oldPair, oldCount in polymerCounts.items():
    newCounts[oldPair[0] + rules[oldPair]] += oldCount
    newCounts[rules[oldPair] + oldPair[1]] += oldCount
  return newCounts

def printSolution(pairCount):
  elementCounts = {e:0 for e in list(set(rules.values()))}
  for k,v in pairCount.items():
      elementCounts[k[0]] += v
  elementCounts[polymer[-1]] +=1
  mostCommon = max(elementCounts.items(), key=operator.itemgetter(1))[1]
  leastCommon = min(elementCounts.items(), key=operator.itemgetter(1))[1]
  print(mostCommon - leastCommon)

pairCounts = defaultdict(int)
for i in range(len(polymer) - 1):
  pairCounts[polymer[i] + polymer[i + 1]] += 1

for i in range(40):
  pairCounts = growPolymer(pairCounts)
  if i == 9:
    printSolution(pairCounts)

printSolution(pairCounts)