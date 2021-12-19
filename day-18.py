from copy import deepcopy
from math import ceil, floor
with open("input-18.txt", "r") as f:
  input = [eval(line) for line in f.readlines()] # major security risk!

def isPair(number):
  return type(number) is list and type(number[0]) is int and type(number[1]) is int

def assignAt(number, idx, value):
  if len(idx) == 1:
    number[idx[0]] = value
    return
  return assignAt(number[idx[0]], idx[1:], value)

def valueAt(number, idx):
  if len(idx) == 1:
    return number[idx[0]]
  return valueAt(number[idx[0]], idx[1:])

def rightMostValue(number, idx):
  if type(number) is int:
    return number, idx
  return rightMostValue(number[1], idx + [1])

def leftMostValue(number, idx):
  if type(number) is int:
    return number, idx
  return leftMostValue(number[0], idx + [0])

def findExploding(number, index):
  if len(index) > 3:
    return (index if isPair(number) else []), number
  
  if type(number) is int:
    return [], number

  for i in range(2):
    idx, num = findExploding(number[i], index + [i])
    if len(idx) > 0:
      return idx, num
  return [], number

def findSplit(number, index):
  if type(number) is int:
    return (index if number > 9 else []), number

  for i in range(2):
    idx, num = findSplit(number[i], index + [i])
    if len(idx) > 0:
      return idx, num
  return [], number

def doSplit(number, index, numberToSplit):
  assignAt(number, index, [floor(numberToSplit / 2), ceil(numberToSplit / 2)])

def doExplode(number, index, numberToExplode):
  if not type(numberToExplode) is list or type(numberToExplode[0]) is not int or type(numberToExplode[1]) is not int:
    raise ValueError("only pairs of regular numbers can explode!")
  idxSum = sum(index)
  if idxSum > 0:
    reverseIndex = index[::-1]
    reverseIndex = [0] + reverseIndex[reverseIndex.index(1) + 1:]
    leftvalue, leftIndex = rightMostValue(valueAt(number, reverseIndex[::-1]), reverseIndex[::-1])
    assignAt(number, leftIndex, leftvalue + numberToExplode[0])
  if idxSum < len(index):
    reverseIndex = index[::-1]
    reverseIndex = [1] + reverseIndex[reverseIndex.index(0) + 1:]
    rightValue, leftIndex = leftMostValue(valueAt(number, reverseIndex[::-1]), reverseIndex[::-1])
    assignAt(number, leftIndex, rightValue + numberToExplode[1])
  assignAt(number, index, 0)

def reduce(number):
  while True:
    idx, num = findExploding(number, [])
    if len(idx) > 0:
      doExplode(number, idx, num)
      continue
    idx, num = findSplit(number, [])
    if len(idx) > 0:
      doSplit(number, idx, num)
      continue
    break
  return number

def add(a, b):
  return reduce([a, b])

def magnitude(number):
  if type(number) is int:
    return number
  return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def partOne(input):
  result = add(input[0], input[1])
  for i in range(2, len(input)):
    result = add(result, input[i])

  print(magnitude(result))

def partTwo(input):
  maximumMagnitude = 0
  for i in range(len(input)):
    for j in range(len(input)):
      m = magnitude(add(deepcopy(input[i]), deepcopy(input[j])))
      if m > maximumMagnitude:
        maximumMagnitude = m
  print(maximumMagnitude)
  pass

partOne(deepcopy(input))
partTwo(input)