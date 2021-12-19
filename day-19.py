with open("input-19.txt", "r") as f:
  input = [line.strip () for line in f.readlines()]

def splitScanners(input):
  scannerInput = []
  while '' in input:
    idx = input.index('')
    scannerInput.append(input[:idx])
    input = input[idx + 1:]
  scannerInput.append(input)
  return scannerInput

def orderKey(x):
  return tuple(x)

def subtract(a,b):
  result = list(map(abs, [v1 - v2 for v1,v2 in zip(a,b)]))
  result.sort ()
  return result

scannerInput = splitScanners(input)
for scanner in scannerInput:
  values = [list(map(int, data.split(','))) for data in scanner[1:]]
  values.sort(key=orderKey)
  print(f"{scanner[0]}:")
  print(f" {subtract(values[0], values[1])}")
  print(f" {subtract(values[1], values[2])}")
  print(f" {subtract(values[2], values[3])}")