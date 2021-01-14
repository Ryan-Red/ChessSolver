import chessPlayer_setup


board = chessPlayer_setup.init()

printBoard = chessPlayer_setup.printBoard
printBoard(board)
contains = chessPlayer_setup.contains
GetLegalMoves = chessPlayer_setup.GetPieceLegalMoves

while True:
   while True:
      inx = input("Player 1 enter a piece to move: ")
      iny = input("Move to? ")
      x = int(inx)
      y = int(iny)
 
      if(contains(GetLegalMoves(board,x),y) == True):
         board[y] = board[x]
         board[x] = 0
         break
      else:
         print("Invalid Move")

   printBoard(board)
   while True:
      inx = input("Player 2 enter a piece to move: ")
      iny = input("Move to? ")
      x = int(inx)
      y = int(iny)
      if(contains(GetLegalMoves(board,x),y) == True):
         board[y] = board[x]
         board[x] = 0
         break
      else:
         print("Invalid Move")

   printBoard(board)

  
   
