from statistics import median, mean

with open("input-7.txt", "r") as f:
  crabPos = list(map(int,f.readline().split(',')))

distancesToMedian = [abs(d - median(crabPos)) for d in crabPos]

print(int(sum(distancesToMedian)))

distancesToMean = [abs(d - int(mean(crabPos))) for d in crabPos]
fuelCost = sum([sum(list(range(d + 1))) for d in distancesToMean])

print(fuelCost)