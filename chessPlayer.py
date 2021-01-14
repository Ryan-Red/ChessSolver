from chessPlayer_setup import *
def getLevelOrder(node):
    q = [node]
    accum = []
    while True:
       val = q.pop()
       accum = accum + [val]
       for i in range(0,32,1):
          if i == len(val.children):
             break
          q.insert(0,val.children[i])

       if q == []:
          break
    return accum


def chessPlayer(board, player):

   if player == 10:
      maximizing = True
   elif player == 20:
      maximizing = False
   else:
      return [False,[],[],[]]
   
   if type(board)!= list:
      return [False,[],[],[]]


   check = GetPoints(board)
   if check%100000 == 0:
      if check != 0:
            return[False,[],[],[]]
    
   node = tree([],0)
   moves = GenMoves(board,player,0)
   node.children = moves
   if moves == []:
      return [False,[],[],[]]
   candidateMoves = getCandidates(moves)

   [move,score] = minMax(node,3,maximizing)
   if move == []:
      return [False,[],[],[]]
   
  
   status = True

   evalTree= getLevelOrder(node)

#Status is true if succeeded
#move is a 2 list, move[0] location to move from
#                  move[1] is location to move to
#Candidate moves: candidateMove[i][0] is the move
                 #candidateMove[i][1] is the rating of the move
#Evaltree is the level order traversal of the tree used to evaluate the move
   return [status,move,candidateMoves,evalTree]


#board = init()
#printBoard(board)
#print(chessPlayer(board,10))
