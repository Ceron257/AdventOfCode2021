with open("input-4.txt", "r") as f:
  input = list(map(int, f.readline().strip().split(',')))
  gridNumbers = [lineStripped for line in f.readlines() if (lineStripped := line.strip()) != '']

class Grid:
  def __init__(self, grid):
    self.grid = []
    for line in grid:
      elements = [l for l in line.split()]
      self.grid.append(list(map(int, elements)))
    self.marked = []
    self.last = None
  
  def mark(self, number : int):
    for l in range(5):
      if number in self.grid[l]:
        if(marked := [l, self.grid[l].index(number)]) not in self.marked:
          self.marked.append(marked)
          self.last = number

  def won(self):
    for i in range(5):
      rows = [j for ii,j in self.marked if ii == i]
      if len(rows) == 5: return True
      cols = [ii for ii,j in self.marked if j == i]
      if len(cols) == 5: return True
    return False

  def score(self):
    sum = 0
    for i in range(5):
      for j in range(5):
        if [i,j] in self.marked:
          continue
        sum += self.grid[i][j]
    return sum * self.last

def determineWinner(first):
  grids = [Grid(gridNumbers[index:index+5]) for index in range(0, len(gridNumbers) - 5 + 1, 5)]
  winner = None
  for number in input:
    for grid in grids:
      if grid.won(): continue
      grid.mark(number)
      if grid.won():
        if first: return grid
        winner = grid
  return winner

print(determineWinner(True).score())
print(determineWinner(False).score())