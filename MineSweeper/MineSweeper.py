import function


#Globals
global MasterBoard
global UserBoard,flag
global length

#prints the game board
def printBoard(board):
    print('    ',end='')
    for i in range(length):
        print(i + 1, '', sep= ' ', end = '')
    print() 
    for i in range(length):
        if i < 9:
            print(i + 1, '|', sep = '  ', end='')
        else:
            print(i + 1, '|', sep = ' ', end='')
        for j in range(length):
            if board[i][j] == -1:
                print('X', end = '|')
            elif board[i][j] == 9:
                print('-', end = '|')
            elif board[i][j] == 11:
                print('F', end = '|')
            else:
                print(str(board[i][j]).rstrip('\n'), end = '|')
            

        print()

"""
Prints out a basic display
asks player for new game or continue
and
a way to set the board max size, and how many mines
populates a board with mines
"""

while True:
    print("Weclome to Mine Sweeper!")
    choice = str(input("New game\nContinue\n :")).upper()
    if choice == 'N':
        length = abs(int(input("Enter number for board: ")))
        if length > 10:
            length = 10
        mines = abs(int(input("Enter number of mines: ")))
        if mines > length * length:
            mines = int(length * length / 2)
        MasterBoard = function.newBoard(length, mines)
        UserBoard = function.blankBoard(length)
        break
    elif choice == 'C':
        UserBoard = function.savedBoard(0)
        MasterBoard = function.savedBoard(1)
        length = function.savedBoard(2)
        break


"""
while have not landed on a mine or all non mines are shown 
    prints out the blank board 
    asks if want to save or promots the user for a (x,y) cordanant and if wants to flag a space (x,y,f)
    takes the guess and checks if it is empty, a number, or a mine
"""
flag = False
while True:
    printBoard(UserBoard)
    choice = str(input("Guess a space\nFlag a space\nSave\nQuit\n :")).upper()
   
    if choice == 'G':
        row = 21
        while row > length or type(row) != int or row == 0:
            try:
                row = abs(int(input("Enter a Row: ")))
            except:
                print("Try Again!")

        colm = 21
        while colm > length or type(colm) != int or row == 0:
            try:
                colm = abs(int(input("Enter a Column: ")))
            except:
                print("Try Again")
 
        UserBoard,flag = function.guess(row - 1,colm - 1,UserBoard,MasterBoard, length)

    elif choice == 'F':
        row = 21
        while row > length or type(row) != int or row == 0:
            try:
                row = abs(int(input("Enter a Row: ")))
            except:
                print("Try Again!")
                
        colm = 21
        while colm > length or type(colm) != int or row == 0:
            try:
                colm = abs(int(input("Enter a Column: ")))
            except:
                print("Try Again")

        UserBoard = function.flag(row - 1,colm - 1,UserBoard)

    elif choice == 'S':
        function.save(UserBoard,MasterBoard, length)

    elif choice == 'Q':
        print("Good Bye")
        quit(0)

    elif choice == 'A':
        printBoard(MasterBoard)

    if flag == True:
        printBoard(MasterBoard)
        quit(0)
    
