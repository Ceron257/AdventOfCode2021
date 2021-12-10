with open("input-8.txt","r") as f:
  input = [line.split("|") for line in f.readlines()]

class Signals:
  def __init__(self, signals) -> None:
    self.active = {s : True for s in signals.strip()}
    pass

  def activeSegments (self):
    return len(self.active)

displays =     [[Signals(signal) for signal in signals[1].split()] for signals in input]

uniqueSignals = {
  2 : 1,
  3 : 7,
  4 : 4,
  7 : 8
}

uniqueCount = 0
for displayList in displays:
  uniqueCount += sum([1 if display.activeSegments() in uniqueSignals else 0 for display in displayList])

print(uniqueCount)