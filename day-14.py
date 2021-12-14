import copy
import operator
from collections import defaultdict

with open("input-14.txt", "r") as f:
  polymer = f.readline().strip ()
  f.readline()
  rules = {line[0] : line[1] for l in f.readlines() if (line := l.strip().split(' -> ')) != ''}

def growPolymer(polymerCounts, elementCounts):
  newCounts = copy.deepcopy(polymerCounts)
  for oldPair, oldCount in polymerCounts.items():
    newCounts[oldPair] -= oldCount
    newCounts[oldPair[0] + rules[oldPair]] += oldCount
    newCounts[rules[oldPair] + oldPair[1]] += oldCount
    elementCounts[rules[oldPair]] += oldCount
  return newCounts

def printSolution(elementCounts):
  mostCommon = max(elementCounts.items(), key=operator.itemgetter(1))[1]
  leastCommon = min(elementCounts.items(), key=operator.itemgetter(1))[1]
  print(mostCommon - leastCommon)

pairCounts = defaultdict(int)
for i in range(len(polymer) - 1):
  pairCounts[polymer[i] + polymer[i + 1]] += 1

elementCounts = defaultdict(int)
for element in set(polymer):
  elementCounts[element] = polymer.count(element)

for i in range(40):
  pairCounts = growPolymer(pairCounts, elementCounts)
  if i == 9:
    printSolution(elementCounts)

printSolution(elementCounts)