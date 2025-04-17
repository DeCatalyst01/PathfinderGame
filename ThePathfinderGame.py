import random

#create game grid/board
def create_board(size, num_of_obstacles):
    
    board = [['.' for _ in range(size)] for _ in range(size)]

    board[0][0] = 'S'
    board[size - 1][size - 1] = 'T'

    

    obstacles = 0

    while obstacles < num_of_obstacles:
        r = random.randint(0, size - 1)
        c = random.randint(0, size -1)
        if board[r][c] == '.' :
            board[r][c] = '#'

            obstacles += 1

    board[0][0] = 'P'  

    return board

#Player move mapping
def move_player(board, position, direction):

    DIRECTIONS = { 'up' : (-1, 0),
                   'down' : (1, 0),
                   'left' : (0, -1),
                   'right' : (0, 1)
                 }

    row, col = position
    d_row, d_col = DIRECTIONS.get(direction, (0, 0))
     
    new_row = row + d_row
    new_col = col + d_col

    # check if move is out of bounds
    if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(board[0]):
        print('⚠ Your move is out of bounds!\nTry again!')
        return  position
    
    #check if player collides with an obstacle
    if board[new_row][new_col] == '#':
        print('💥 Oops! You collided against an obstacle.\nGame Over!')
        exit()
        
    #check if player arrives at target    
    if board[new_row][new_col] == 'T':
        print('🎉🎉Congratulations, You win!')
        exit()  


    board[row][col] = '.'
    board[new_row][new_col] = 'P'

    return (new_row, new_col) 

#The  main game loop
def display_board(board):

    for row in board:
        print(' '.join(row))

board = create_board(6, 10)
position = (0, 0)

board[position[0]][position[1]] = 'P'

while True:
    display_board(board)
    direction = input("Enter your move('up/down/left/right') : ").lower()
    position = move_player(board, position, direction)


        
        