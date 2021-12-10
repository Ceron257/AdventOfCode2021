from statistics import median

with open("input-10.txt", "r") as f:
  input = [l.strip() for l in f.readlines ()]

openToCloseBrace = {
  "<" : ">",
  "(" : ")",
  "[" : "]",
  "{" : "}"
}

points = {
  "(" : 3,     ")" : 3,
  "[" : 57,    "]" : 57,
  "{" : 1197,  "}" : 1197,
  "<" : 25137, ">" : 25137
}

autoCompleteScores = {
  ")" : 1,
  "]" : 2,
  "}" : 3,
  ">" : 4
}

def checkLine(line):
  openBraces = []
  for character in line:
    if character not in openToCloseBrace:
      if len(openBraces) == 0 or openToCloseBrace[openBraces[-1]] != character:
        return (points[character], openBraces)
      openBraces.pop ()
    else:
      openBraces.append(character)
  return (0, openBraces)

def autoCompleteScore(autoCompletion):
  score = 0
  for character in autoCompletion:
    score = 5 * score + autoCompleteScores[openToCloseBrace[character]]
  return score

score = sum([checkLine(line)[0] for line in input])
print(score)

incompleteLines = [result[1] for l in input if (result := checkLine(l)) != None and result[0] == 0]
scores = [autoCompleteScore(autoCompletion[::-1]) for autoCompletion in incompleteLines]
print(median(scores))