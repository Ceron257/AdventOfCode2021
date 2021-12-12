with open("input-12.txt","r") as f:
  input = [line.strip().split('-') for line in f.readlines()]

edges = dict()

def addEdge (a, b):
  if a in edges:
    edges[a].append(b)
  else:
    edges[a] = [b]

for edge in input:
  addEdge(edge[0], edge[1])
  addEdge(edge[1], edge[0])

def constructPaths(currentPath, nextNode, visitedLowerCaseTwice = None, allowTwice = False):
  newPath = [p for p in currentPath]
  newPath.append(nextNode)

  if nextNode == 'end':
    paths.append(newPath)

  if allowTwice and visitedLowerCaseTwice == None and nextNode.islower() and nextNode in currentPath:
    visitedLowerCaseTwice = nextNode

  for next in edges[nextNode]:
    if allowTwice:
      if next == 'start': continue
      if next == 'end' and next in currentPath: continue
    if (visitedLowerCaseTwice != None or not allowTwice) and next.islower() and next in currentPath:
      continue
    constructPaths(newPath, next, visitedLowerCaseTwice, allowTwice)

paths = list()
constructPaths([], 'start')
print(len(paths))

paths = list()
constructPaths([], 'start', None, True)
print(len(paths))
