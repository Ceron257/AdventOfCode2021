with open("input-5.txt", "r") as f:
  pointPairs = [list(map(lambda v: v.strip(), line.split('->'))) for line in f.readlines()]

X = 0
Y = 1

class Point:
  def __init__(self, coordinates : list[int]):
    self.x = coordinates[X]
    self.y = coordinates[Y]

  def normalized(self):
    x = int(self.x / abs(self.x)) if self.x != 0 else 0
    y = int(self.y / abs(self.y)) if self.y != 0 else 0
    return Point([x, y])

  def __add__(self, other):
    return Point([self.x + other.x, self.y + other.y])

  def __sub__(self, other):
    return Point([self.x - other.x, self.y - other.y])

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((self.x, self.y))

class Line:
  def __init__(self, points : list[str]):
    self.p1, self.p2 = list(map(Point, [list(map(int, p.split(','))) for p in points]))

  def isHorizontal(self):
    return self.p1.y == self.p2.y

  def isVertical(self):
    return self.p1.x == self.p2.x

  def points(self):
    dXY = (self.p2 - self.p1).normalized()
    result = [self.p1, self.p2]
    current = self.p1
    while (current := current + dXY) != self.p2:
      result.append(current)
    return result

def countDangerousPoints(lines):
  coveredPoints = {}
  for line in lines:
    for point in line.points():
      if point not in coveredPoints: coveredPoints[point] = 0
      coveredPoints[point] += 1

  return sum(value > 1 for value in coveredPoints.values())

allLines = [Line(line) for line in pointPairs]
filteredLines = [l for line in allLines if (l := line).isHorizontal() or l.isVertical()]

print(countDangerousPoints(filteredLines))
print(countDangerousPoints(allLines))