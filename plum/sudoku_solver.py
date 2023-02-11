# pick empty square
# try all numbers (for loop)
# find one that works
# repeat
# backtrack (when solution cannot be completed

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#print out board

def print_board(brd) :
    for i in range(len(brd)):
        if i % 3 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

                if j == 8:
                    print(brd[i][j])
                else:
                    print(str(brd[i][j]) + " ")



