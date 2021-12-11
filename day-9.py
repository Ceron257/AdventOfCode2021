with open("input-9.txt", "r") as f:
  input = [list(map(int, line.strip())) for line in f.readlines()]

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
        if abs(dX) + abs(dY) != 1: continue
        checkPos = [pos[0] + dX, pos[1] + dY]
        if self.containsPosition(checkPos): neighbours.append(checkPos)
    return [n for n in neighbours if n != pos]


grid = Grid(input)

count = 0
lowPoints = list()
for x in range(grid.xDim):
  for y in range(grid.yDim):
    current = grid.at ([x, y])
    score = 1
    for neighbour in grid.neighbours([x, y]):
      if (o := grid.at (neighbour)) <= current:
        score = 0
        break
    if score == 1:
      count += 1 + current
      lowPoints.append([x, y])

print(f"Answer for part 1: {count}")

lowPointSizes = {}

for lowPoint in lowPoints:
  toVisit = [lowPoint]
  positions = list()
  while len(toVisit) > 0:
    current = toVisit.pop()
    if current in positions: continue
    positions.append(current)
    for neighbour in grid.neighbours(current):
      if grid.at(neighbour) != 9:
        toVisit.append(neighbour)
  lowPointSizes[str(lowPoint)] = len(positions)

sizes = list(lowPointSizes.values())
sizes.sort(reverse = True)

print(sizes[0] * sizes[1] * sizes[2])
