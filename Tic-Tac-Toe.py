from random import randrange
b = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
used = [5]
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {b[0][0]}   |   {b[0][1]}   |   {b[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {b[1][0]}   |   {b[1][1]}   |   {b[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {b[2][0]}   |   {b[2][1]}   |   {b[2][2]}   | 
|       |       |       |
+-------+-------+-------+
    """)
    return 

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    user_input = int(input("Enter your move: "))
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == user_input:
                used.append(user_input)
                board[i][j] = "O"
                break   
            # elif board[i][j] == "X": 
            #     print("Enter a valid Input")
            #     user_input = int(input("Enter your move: "))
            #     break
    return 

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    used = []
    free = []
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                new = (i, j)
                used.append(new)
            else:
                new = (i, j)
                free.append(new)
    return used

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for check in board:
        pass
    pass

def draw_move(board):
    # The function draws the computer's move and updates the board.
    computer_input = randrange(1, 10)
    # while computer_input in used:
    while computer_input in used:
        computer_input = randrange(1, 10)
        if len(used) == 9:
            break
    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == computer_input:
                used.append(computer_input)
                board[i][j] = "X"
                break    
    return
move = 1
display_board(b)
while move < 5:
    enter_move(b)
    draw_move(b)
    display_board(b)
    move += 1
# make_list_of_free_fields(b)