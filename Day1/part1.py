prevNum = 0
largerMeasures = 0

with open('part1input') as input_file:
  for line in input_file:
    if int(line) > prevNum:
      largerMeasures += 1

    prevNum = int(line)

largerMeasures -= 1
print(largerMeasures)