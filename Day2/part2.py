distance = 0
depth = 0
aim = 0

with open('part1input') as input_file:
  for line in input_file:
    command = line.split()
    if command[0] == 'forward':
      distance += int(command[1])
      depth += aim * int(command[1])
    elif command[0] == 'down':
      aim += int(command[1])
    else:
      aim -= int(command[1])

print('You have a horizontal position of:', distance)
print('You have a vertical position of:', depth)
print('Multiplied together:', depth * distance)