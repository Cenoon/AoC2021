def check_num(board_list, num):
  winning_index = []
  removed_boards = 0
  board_index = 0
  last_num = ''
  for board in board_list:
    row_index = 0
    for row in board:
      if num in row:
        board[row_index][row.index(num)] = 'X'
        last_num = num
      row_index += 1

    winner = check_board(board)
    if len(board_list) == 1 and winner:
      return board_index, last_num
    elif winner:
      winning_index.append(board_index)

    board_index += 1

  for index in winning_index:
    board_list.remove(board_list[index-removed_boards])
    removed_boards += 1

  return -1, last_num

def check_board(board):
  winner = False
  # check horizontal
  for row in range(len(board)):
    winner = True
    for col in range(len(board[row])):
      if board[row][col] != 'X':
        winner = False
        break
    if winner:
      return winner
  # check vertical
  for row in range(len(board)):
    winner = True
    for col in range(len(board[row])):
      if board[col][row] != 'X':
        winner = False
        break
    if winner:
      return winner

  # check diagonals
  for diag in range(len(board)):
    winner = True
    if board[diag][diag] != 'X':
      winner = False
      break
  if winner:
    return winner

  for diag in range(len(board)):
    winner = True
    if board[len(board) - 1 - diag][len(board) - 1 - diag] != 'X':
      winner = False
      break
  if winner:
    return winner

  return False

def calc_score(board, last_num):
  sum = 0
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] != 'X':
        sum += int(board[row][col])

  return sum*int(last_num)

def main():
  call_nums = []
  board_list = []
  winning_board = -1

  with open('part1input') as input_file:
    call_nums = input_file.readline().rstrip().split(',')
    board = []
    for line in input_file:
      if line != '\n':
        curr_line = []
        curr_line = line.rstrip().split()
        board.append(curr_line)
      elif board != []:
        board_list.append(board)
        board = []
    board_list.append(board)

  for num in call_nums:
    winning_board, last_num = check_num(board_list, num)
    if winning_board != -1:
      print(calc_score(board_list[winning_board], last_num))
      break

if __name__ == "__main__":
  main()