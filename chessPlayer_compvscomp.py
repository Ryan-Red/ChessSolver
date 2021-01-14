from chessPlayer import *
import time


board = init()
printBoard(board)
maximum = -1
for i in range(0,100,1):
   print("------------------------------------------------------------")
   print("White's Move")
   timeA = time.time()
   white = chessPlayer(board,10)
   delta = time.time()-timeA
   if delta > maximum:
      maximum = delta

   print(delta, "process Time")
   if white[0] == False:
      print("Game Over")
      break

  
   moveW = white[1]
   board[moveW[1]] = board[moveW[0]]
   board[moveW[0]] = 0
   print(moveW)
   printBoard(board)
   print(white[0:3])

   print(maximum, "Maximum")
   print("------------------------------------------------------------")
   print("Black's Move")
   timeB = time.time()
   black = chessPlayer(board,20)
   delta = time.time()-timeB

   if delta > maximum:
      maximum = delta
   print(delta,"process Time")
   if black[0] == False:
      print("Game Over")
      break 
  
   moveB = black[1]
   board[moveB[1]] = board[moveB[0]]
   board[moveB[0]] = 0
   print(moveB)
   printBoard(board)
   print(maximum, "Maximum")
   print(black[0:3])
print("Maximum Time is of:",maximum) 
