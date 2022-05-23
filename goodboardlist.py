# Write your code here :-)
boardlist=[6,6,5,5,5,2,2,2,2,3,3,3]
leftover=0
boardnum=0
stockboard=8
#------------
for board in boardlist:
    if board<=leftover:
        lengthprecut=leftover
        leftover=leftover-board
    else:
        leftover=stockboard-board
        lengthprecut=stockboard
        boardnum=boardnum+1

    print(board, boardnum,lengthprecut,leftover)

