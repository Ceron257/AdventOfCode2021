input = [(dir,int(val)) for dir,val in (line.split(' ') for line in open("input-2.txt",'r').readlines())]

pos = [0, 0]

POS = 0
DEPTH = 1

for dir, val in input:
    if (dir == 'down'):
      pos[DEPTH] += val
    elif (dir == 'up'):
      pos[DEPTH] -= val
    elif (dir == 'forward'):
      pos[POS] += val

print (pos[POS] * pos[DEPTH])

# part 2:

pos = [0, 0, 0]

AIM = 2

for dir, val in input:
    if (dir == 'down'):
      pos[AIM] += val
    elif (dir == 'up'):
      pos[AIM] -= val
    elif (dir == 'forward'):
      pos[POS] += val
      pos[DEPTH] += val * pos[AIM]

print (pos[POS] * pos[DEPTH])