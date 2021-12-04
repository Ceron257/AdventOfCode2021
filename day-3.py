import operator as op

with open("input-3.txt", "r") as file:
  input = [v for v in (line.strip() for line in file.readlines())]

def count (input : list[str], position : int) -> dict:
  counts = {'0' : 0, '1' : 0}
  for line in input:
    counts[line[position]] += 1
  return counts

def mostCommonCharacter (input : list[str], position : int) -> str:
  return max(count(input, position).items(), key=op.itemgetter(1))[0]

gammaStr = ''.join ([mostCommonCharacter(input, p) for p in range(len(input[0]))])
gamma = int(''.join(gammaStr), 2)
allBits = 2 ** len(gammaStr) - 1
epsilon = gamma ^ allBits
print(gamma * epsilon)

def filterNumbers (input : list[str], position : int, selection, tied) -> list[str]:
  counts = count(input, position)
  candidate = selection(counts.items(), key=op.itemgetter(1))[0]
  keepStr = candidate if counts['0'] != counts['1'] else tied
  return [keep for keep in input if keep[position] == keepStr]

generatorRatings = input
for position in range (len(generatorRatings[0])):
  generatorRatings = filterNumbers (generatorRatings, position, max, '1')

scrubberRatings = input
for position in range (len(scrubberRatings[0])):
  if len(scrubberRatings) == 1:
    break
  scrubberRatings = filterNumbers (scrubberRatings, position, min, '0')

print(int(generatorRatings[0], 2) * int(scrubberRatings[0], 2))