list_of_depths = []
prevSum = 0
largerMeasures = 0

with open('part1input') as input_file:
  for line in input_file:
    list_of_depths.append(int(line))

for index, depth in enumerate(list_of_depths):
  if index+2 < len(list_of_depths):
    currSum = int(list_of_depths[index]) + int(list_of_depths[index+1]) + int(list_of_depths[index+2])
    if currSum > prevSum:
      largerMeasures += 1
    prevSum = currSum

largerMeasures -= 1
print(largerMeasures)