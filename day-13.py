with open("input-13.txt", "r") as f:
  input = f.readlines()

dots = [list(map(int, l.split(','))) for line in input if not (l := line.strip ()).startswith("fold") and l != '']
folds = [line.strip().removeprefix('fold along ').split('=') for line in input if line.startswith("fold")]

def performFold (dots, fold):
  afterFold = list()
  foldCoordinate = int(fold[1])
  for dot in dots:
    foldedDot = []
    if fold[0] == 'x' and dot[0] > foldCoordinate:
      foldedDot = [2 * foldCoordinate - dot[0], dot[1]]
    elif fold[0] == 'y' and dot[1] > foldCoordinate:
      foldedDot = [dot[0], 2 * foldCoordinate - dot[1]]
    else:
      if dot not in afterFold: afterFold.append(dot)
    
    if len(foldedDot) > 0:
      if foldedDot not in afterFold: afterFold.append(foldedDot)

  return afterFold

def printDots (dots):
  Xs = [p[0] for p in dots]
  Ys = [p[1] for p in dots]
  minX, maxX = min(Xs), max(Xs)
  minY, maxY = min(Ys), max(Ys)

  for y in range(minY, maxY + 1, 1):
    for x in range(minX, maxX + 1, 1):
      if [x, y] in dots:
        print('#', end='')
      else:
        print(' ', end='')
    print('')

dots = performFold(dots, folds[0])
print(f"{len(dots)} dots are visible after first fold.")

for fold in folds[1:]:
  dots = performFold(dots, fold)
print('After fold:')
printDots(dots)