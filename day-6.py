with open("input-6.txt","r") as f:
  input = [list(map(int, line.split(','))) for line in f.readlines()][0]

state = { }

for i in range(9):
  state[i] = input.count(i)

for day in range(256):
  newState = { }
  for i in range(8):
    newState[i] = state[i + 1]
  newState[6] += state[0]
  newState[8] = state[0]
  state = newState
  if day == 79:
    print(sum(state.values()))

print(sum(state.values()))