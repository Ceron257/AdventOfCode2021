input = [int(line) for line in open("input-1-1.txt",'r').readlines()]
increases = [x1 > x0 for x1, x0 in zip (input[1:], input)].count(True)
print(increases)

slidingSum = [sum(v) for v in (input[index:index + 3] for index in range(len(input) - 3 + 1))]
increases2 = [x1 > x0 for x1, x0 in zip (slidingSum[1:], slidingSum)].count(True)
print(increases2)