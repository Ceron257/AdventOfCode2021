with open("input-11.txt", "r") as f:
  input = [[int(digit) for digit in line.strip()] for line in f.readlines()]

class Grid:
  def __init__(self, data : list[list[object]]):
    self.xDim = len(data)
    self.yDim = len(data[0]) if self.xDim != 0 else 0
    self.data = data

  def count(self) -> int:
    return self.xDim * self.yDim

  def at(self, pos : list[int]) -> object:
    return self.data[pos[0]][pos[1]]

  def containsPosition(self, pos : list[int]) -> bool:
    return (pos[0] >= 0 and pos[0] < self.xDim and 
            pos[1] >= 0 and pos[1] < self.yDim)

  def neighbours(self, pos : list[int]) -> list[list[int]]:
    neighbours = list()
    for dX in range(-1, 2):
      for dY in range(-1, 2):
        checkPos = [pos[0] + dX, pos[1] + dY]
        if self.containsPosition(checkPos): neighbours.append(checkPos)
    return [n for n in neighbours if n != pos]

class Octopus:
  def __init__(self, energy) -> None:
    self.energy = energy

  def startCycle(self) -> bool:
    if self.energy > 9: self.energy = 0
    return self.increaseEnergy()

  def increaseEnergy(self) -> bool:
    self.energy += 1
    return self.energy > 9

def simulateStep(grid : Grid) -> int:
  toIncrease = list()
  flashCount = 0
  addNeighbours = lambda pos: [toIncrease.append([neighbour, grid.at(neighbour)]) for neighbour in grid.neighbours(pos)]
  for x in range(0, grid.xDim):
    for y in range(0, grid.yDim):
      if grid.at([x, y]).startCycle():
        flashCount += 1
        addNeighbours([x, y])

  while len(toIncrease) > 0:
    position, octopus = toIncrease.pop()
    if (octopus.energy > 9): continue # flashed already. Skip
    if octopus.increaseEnergy():
      flashCount += 1
      addNeighbours(position)
  return flashCount

octopuses = [list(map(Octopus, line)) for line in input]

grid = Grid(octopuses)
totalFlashes = 0
stepCount = 0
lastFlashes = 0

while lastFlashes != grid.count():
  lastFlashes = simulateStep(grid)
  stepCount += 1
  totalFlashes += lastFlashes
  if stepCount == 100:
    print(f"After 100 steps: {totalFlashes} flashes")
print(f"All octopuses flash after {stepCount} steps")