numbers = []
num1s = 0
num0s = 0
gamma = []
epsilon = []
gammadec = 0
epsilondec = 0

with open('part1input') as input_file:
  for line in input_file:
    numbers.append(line)

numlen = len(numbers[0]) - 1

for x in range(numlen):
  for number in numbers:
    if number[x] == '1':
      num1s += 1
    else:
      num0s += 1
  if num1s > num0s:
    gamma.append(1)
    epsilon.append(0)
  else:
    gamma.append(0)
    epsilon.append(1)
  num1s = 0
  num0s = 0

ind = numlen-1

for x in gamma:
  gammadec += x*(2**(ind))
  ind -= 1
print('Gamma is:', gammadec)
ind = numlen-1
for x in epsilon:
  epsilondec += x*(2**(ind))
  ind -= 1
print('Epsilon is:', epsilondec)
print('Solution is:', gammadec * epsilondec)