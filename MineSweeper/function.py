import random


#globals so I dont need to define them just declare the variables


#creeates a new board and populates it with mines
#true for master board, false for player board
def blankBoard(length):
    boardNew = [[9 for i in range(length)] for j in range(length)]
    return boardNew

def newBoard(length,mines):
    boardNew = [[0 for i in range(length)] for j in range(length)]
    #finding a random location for mine
    placed = 0
    random.seed(0)
    while placed < mines:
        r = random.randint(0,length) - 1
        c = random.randint(0,length) - 1

        if boardNew[r][c] != -1:
            placed += 1
            boardNew[r][c] = -1

    #checks for mines next to spaces
    for row in range(length):
        for colm in range(length):
            if boardNew[row][colm] == -1:
                continue
    #checks cardional directions
            if row > 0 and boardNew[row - 1][colm] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
              
            if row < length - 1 and boardNew[row + 1][colm] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
            
            if colm > 0 and boardNew[row][colm - 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
            
            if colm < length - 1 and boardNew[row][colm + 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
    #checks diagonals
            if row > 0 and colm > 0 and boardNew[row - 1][colm - 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
            
            if row > 0 and colm < length - 1 and boardNew[row - 1][colm + 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
              
            if row < length - 1 and colm > 0 and boardNew[row + 1][colm - 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
            
            if row < length - 1 and colm < length - 1 and boardNew[row + 1][colm + 1] == -1:
                boardNew[row][colm] = boardNew[row][colm] + 1
   
    return boardNew

def savedBoard(choice):
    with open("savegame.txt","r") as savedgame:
        #creates a board with the length stored
        length = int(savedgame.readline())
        UserBoard = blankBoard(length)
        #populates the created board
        for row in range(length):
            for colm in range(length):
                UserBoard[row][colm] = int(savedgame.readline()) 

        #creates a board with the length stored
        MasterBoard = blankBoard(length)
        #populates the created board
        for row in range(length):
            for colm in range(length):
                MasterBoard[row][colm] = int(savedgame.readline())
    if choice == 0:
        return UserBoard
    elif choice == 1:
        return MasterBoard
    else:
        return length

def guess(row,colm,UserBoard,MasterBoard, length):
    UserBoard[row][colm] = MasterBoard[row][colm]
    for row in range(length):
        for colm in range(length):
            if MasterBoard[row][colm] == 0:
        #checks cardional directions
                if row > 0 and MasterBoard[row - 1][colm] != -1:
                    UserBoard[row - 1][colm] = MasterBoard[row - 1][colm]
              
                if row < length - 1 and MasterBoard[row + 1][colm] != -1:
                    UserBoard[row + 1][colm] = MasterBoard[row][colm]
            
                if colm > 0 and MasterBoard[row][colm - 1] != -1:
                    UserBoard[row][colm - 1] = MasterBoard[row][colm - 1]
            
                if colm < length - 1 and MasterBoard[row][colm + 1] != -1:
                    UserBoard[row][colm + 1] = MasterBoard[row][colm + 1]
        #checks diagonals
                if row > 0 and colm > 0 and MasterBoard[row - 1][colm - 1] != -1:
                    UserBoard[row - 1][colm - 1] = MasterBoard[row - 1][colm - 1]
            
                if row > 0 and colm < length - 1 and MasterBoard[row - 1][colm + 1] != -1:
                    UserBoard[row - 1][colm + 1] = MasterBoard[row - 1][colm + 1]
              
                if row < length - 1 and colm > 0 and MasterBoard[row + 1][colm - 1] != -1:
                    UserBoard[row + 1][colm - 1] = MasterBoard[row + 1][colm - 1]
            
                if row < length - 1 and colm < - 1 and MasterBoard[row + 1][colm + 1] != -1:
                    UserBoard[row + 1][colm + 1] = MasterBoard[row + 1][colm + 1]
            
            if UserBoard[row][colm] == -1:
                print("You Lost!")
                return UserBoard,True
            else:
                counter = 0
                for i in range(length):
                    for j in range(length):
                        if UserBoard[i][j] == 9 or UserBoard == 11:
                            counter += 1
                if counter == 0:
                    print("Winner!")
                    quit(0)
    return UserBoard,False



def flag(row,colm,UserBoard):
    if UserBoard[row][colm] == 11:
        UserBoard[row][colm] = 9
    else:
        UserBoard[row][colm] = 11
    return UserBoard

def save(UserBoard,MasterBoard, length):
    print("saving...")
    with open("savegame.txt","w") as savegame:
        savegame.write(str(length) + '\n')
        for rElement in UserBoard:
            for cElement in rElement:
                savegame.write(str(cElement) + '\n')
        for rElement in MasterBoard:
            for cElement in rElement:
                savegame.write(str(cElement) + '\n')
    print("Good Bye!")
    quit(0)

