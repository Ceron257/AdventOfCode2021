with open("input-5.txt", "r") as f:
  points = [line.split('->') for line in f.readlines()]

X = 0
Y = 1

class Point:
  def __init__(self, coordinates):
    self.x = coordinates[X]
    self.y = coordinates[Y]

  def __add__(self, other):
    return Point ([self.x + other.x, self.y + other.y])

  def __sub__(self, other):
    return Point ([self.x - other.x, self.y - other.y])

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def toList(self):
    return [self.x, self.y]

class Line:
  def __init__(self, points : list[str]):
    self.p1, self.p2 = [p.split() for p in points]
    self.p1 = Point(list(map(int, self.p1[0].split(','))))
    self.p2 = Point(list(map(int, self.p2[0].split(','))))

  def __str__(self) -> str:
      return f"({self.p1.x}, {self.p1.y}) -> ({self.p2.x}, {self.p2.y})"
  
  def isHorizontal(self):
    return self.p1.y == self.p2.y

  def isVertical(self):
    return self.p1.x == self.p2.x
  
  def points(self):
    dXY = self.p2 - self.p1
    if dXY.x != 0: dXY.x /= abs(dXY.x)
    if dXY.y != 0: dXY.y /= abs(dXY.y)
    dXY.x = int(dXY.x)
    dXY.y = int(dXY.y)
    result = []
    current = self.p1 - dXY
    while (current := current + dXY) != self.p2 + dXY:
      result.append(current)
    return result

def countDangerousPoints(lines):
  coveredPoints = {}
  for line in lines:
    for point in line.points():
      if point.x not in coveredPoints: coveredPoints[point.x] = {}
      coveredYs = coveredPoints[point.x]
      if point.y not in coveredYs: coveredYs[point.y] = 0
      coveredYs[point.y] += 1

  dangerousPositions = 0

  for coveredY in coveredPoints:
    dangerousPositions += sum(value > 1 for value in coveredPoints[coveredY].values())
  return dangerousPositions

allLines = [Line(line) for line in points]
filteredLines = [l for line in allLines if (l := line).isHorizontal() or l.isVertical()]

print(countDangerousPoints(filteredLines))
print(countDangerousPoints(allLines))