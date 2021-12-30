from copy import deepcopy
from math import ceil, floor
from typing import List, Union, Tuple, cast

Number = Union[int, List['Number']]
Index = List[int]

with open("input-18.txt", "r") as f:
  input : List[Number] = [eval(line) for line in f.readlines()] # major security risk!

def isPair(number : Number):
  return isinstance(number, list) and isinstance(number[0], int) and isinstance(number[1], int)

def assignAt(number : Number, idx : Index, value : Number) -> None:
  if len(idx) == 1:
    cast(List[Number], number)[idx[0]] = value
    return
  return assignAt(cast(List[Number], number)[idx[0]], idx[1:], value)

def valueAt(number : Number, idx : Index) -> Number:
  if len(idx) == 1:
    return cast(List[Number], number)[idx[0]]
  return valueAt(cast(List[Number], number)[idx[0]], idx[1:])

def rightMostValue(number : Union[int, Number], idx : Index) -> Tuple[int, Index]:
  if isinstance(number, int):
    return number, idx
  return rightMostValue(number[1], idx + [1])

def leftMostValue(number : Union[int, Number], idx : Index) -> Tuple[int, Index]:
  if isinstance(number, int):
    return number, idx
  return leftMostValue(number[0], idx + [0])

def findExploding(number : Number, index : Index) -> Tuple[Index, Number]:
  if len(index) > 3:
    return (index if isPair(number) else []), number
  
  if isinstance(number, int):
    return [], number

  for i in range(2):
    idx, num = findExploding(number[i], index + [i])
    if len(idx) > 0:
      return idx, num
  return [], number

def findSplit(number : Number, index : Index) -> Tuple[Index, int]:
  if isinstance(number, int):
    return (index if number > 9 else []), number

  for i in range(2):
    idx, num = findSplit(number[i], index + [i])
    if len(idx) > 0:
      return idx, num
  return [], cast(int, number)

def doSplit(number : Number, index : Index, numberToSplit : int) -> None:
  assignAt(number, index, [floor(numberToSplit / 2), ceil(numberToSplit / 2)])

def doExplode(number : Number, index : Index, numberToExplode : Number) -> None:
  if not isinstance(numberToExplode, list) or not isinstance(numberToExplode[0], int) or not isinstance(numberToExplode[1], int):
    raise ValueError("only pairs of regular numbers can explode!")
  idxSum = sum(index)
  if idxSum > 0:
    reverseIndex = index[::-1]
    reverseIndex = [0] + reverseIndex[reverseIndex.index(1) + 1:]
    leftvalue, leftIndex = rightMostValue(valueAt(number, reverseIndex[::-1]), reverseIndex[::-1])
    assignAt(number, leftIndex, leftvalue + cast(List[int], numberToExplode)[0])
  if idxSum < len(index):
    reverseIndex = index[::-1]
    reverseIndex = [1] + reverseIndex[reverseIndex.index(0) + 1:]
    rightValue, leftIndex = leftMostValue(valueAt(number, reverseIndex[::-1]), reverseIndex[::-1])
    assignAt(number, leftIndex, rightValue + cast(List[int], numberToExplode)[1])
  assignAt(number, index, 0)

def reduce(number : Number) -> Number:
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

def add(a : Number, b : Number) -> Number:
  return reduce([a, b])

def magnitude(number : Number) -> int:
  if isinstance(number, int):
    return number
  return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def partOne(input : List[Number]) -> None:
  result : Number = add(input[0], input[1])
  for i in range(2, len(input)):
    result = add(result, input[i])

  print(magnitude(result))

def partTwo(input : List[Number]) -> None:
  maximumMagnitude : int = 0
  for i in range(len(input)):
    for j in range(len(input)):
      m = magnitude(add(deepcopy(input[i]), deepcopy(input[j])))
      if m > maximumMagnitude:
        maximumMagnitude = m
  print(maximumMagnitude)
  pass

partOne(deepcopy(input))
partTwo(input)