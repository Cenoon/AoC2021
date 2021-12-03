def findoxygen(numbers, x):
  if len(numbers) == 1:
    return numbers

  templist1 = []
  templist0 = []
  num1s = 0
  num0s = 0

  for number in numbers:
    if number[x] == '1':
      num1s += 1
      templist1.append(number)
    else:
      num0s += 1
      templist0.append(number)
  
  if num1s >= num0s:
    return findoxygen(templist1, x+1)
  else:
    return findoxygen(templist0, x+1)

def findco2(numbers, x):
  if len(numbers) == 1:
    return numbers

  templist1 = []
  templist0 = []
  num1s = 0
  num0s = 0

  for number in numbers:
    if number[x] == '1':
      num1s += 1
      templist1.append(number)
    else:
      num0s += 1
      templist0.append(number)
  
  if num1s < num0s:
    return findco2(templist1, x+1)
  else:
    return findco2(templist0, x+1)


numbers = []

with open('part1input') as input_file:
  for line in input_file:
    numbers.append(line)

numlen = len(numbers[0]) - 1

oxygen = findoxygen(numbers, 0)
co2 = findco2(numbers, 0)

oxygendec = int(oxygen[0], 2)
co2dec = int(co2[0], 2)

print('Oxygen generator rating is:', oxygendec)
print('CO2 scrubber rating is:', co2dec)
print('Life support rating is:', oxygendec * co2dec)