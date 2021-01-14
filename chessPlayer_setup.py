

class tree:

   def __init__(self, move,score):
      self.candidateMove = [move] + [score] 
      self.children = []
   
   def addChild(self,child):
      self.children = self.children + child
      return True

   def getChildren(self):
      return self.children


def init():
   board = []
   w = 10
   b = 20
   pawn = 0
   knight = 1
   bishop = 2
   rook = 3
   queen = 4
   king = 5
  
   row7 = [b+ rook, b+ knight, b+ bishop, b+king, b+queen,b+bishop,b+knight,b+rook]
   row6 = [b,b,b,b,b,b,b,b]
   row2to5 = [0,0,0,0,0,0,0,0]
   row1 = [w,w,w,w,w,w,w,w]
   row0 = [w+rook,w+knight,w+bishop,w+king,w+queen,w+bishop,w+knight,w+rook]
   board = row0 + row1 + row2to5 + row2to5 + row2to5 + row2to5 + row6 + row7

   return board

def GetPlayerPositions(board,player):
   
   accum = []
   for i in range(0,64,1):
      if board[i] ==0:
         continue
      elif (board[i] - player)>-1:
         if (board[i]-player) < 6:
            accum = accum + [i]
 
   return accum


def isPresent(board,pos):
   if (pos > 63):
      return [False,True]
   elif (pos < 0):
      return [False,True]
   elif(board[pos] == 0):
      return [False,False]
   elif (board[pos] >=10) & (board[pos]<=15):
      return [True,False]
   else:
      return [True,True]  
  
      

def posIsLegal(board,pos,isBlack):
   if pos > 63:
       return []
   elif pos < 0:
       return []
   elif board[pos] == 0:
       return [pos]
   else:
       if board[pos] < 16:
          if isBlack:
             return [pos]
          else:
             return []
       else:
          if isBlack:
             return []
          else:
             return [pos]

def max(x,y):
   if(x >y):
      return x
   return y

def min(x,y):
   if(x >y):
      return y
   return x

def isPositionUnderThreat(board,pos,player):
   opp = 10
   testBoard = list(board)  
   if player == 10:
      opp = 20
      testBoard[pos] = 10
   else:
      testBoard[pos] = 20
   
   oppPos = GetPlayerPositions(testBoard,opp)
   oppMoves = []
 

   for piece in oppPos:
      oppMoves = oppMoves  + GetPieceLegalMoves(testBoard,piece)
   oppMoves.sort() 
 
   if pos in oppMoves == True:
      return True
   else:
      return False

def GetPoints(board):
   accum = 0
   heatMapKing = [3,2,0,0,0,0,2,3,
                  2,2,1,1,1,1,2,2,
                  2,1,2,5,5,2,1,2,
                  2,1,2,5,5,2,1,2,
                  2,1,2,5,5,2,1,2,
                  2,1,2,5,5,2,1,2,
                  2,2,1,1,1,1,2,2,
                  3,2,0,0,0,0,2,3]

   heatMapWP =[0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,
               1,1,1,1,1,1,1,1,
               2,2,2,2,2,2,2,2,
               3,3,3,3,3,3,3,3,
               5,5,5,5,5,5,5,5,
               9,9,9,9,9,9,9,9,
               20,20,20,20,20,20,20,20]

   heatMapBP =[20,20,20,20,20,20,20,20,
               9,9,9,9,9,9,9,9,
               5,5,5,5,5,5,5,5,
               3,3,3,3,3,3,3,3,
               2,2,2,2,2,2,2,2,
               1,1,1,1,1,1,1,1,
               0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,]


   heatMapW = [0,0,0,0,0,0,0,0,
               -1,1,1,1,1,1,1,-1,
               0,2,2,2,2,2,2,0,
               2,5,5,5,5,5,5,2,
               2,5,5,5,5,5,5,2,
               2,5,5,5,5,5,5,2,
               1,4,4,4,4,4,4,1,
               2,2,2,2,2,2,2,2]


   heatMapB = [2,2,2,2,2,2,2,2,
               1,4,4,4,4,4,4,1,
               2,5,5,5,5,5,5,2,
               2,5,5,5,5,5,5,2,
               2,5,5,5,5,5,5,2,
               0,2,2,2,2,2,2,0,
               -1,1,1,1,1,1,1,-1,
               0,0,0,0,0,0,0,0]


   for i in range(0,64,1):
      piece = board[i]
      if piece == 0:
         continue
      elif piece == 20:
         accum = accum -30 - heatMapBP[i]*0.02
      elif (piece == 21):
         accum = accum -50 - heatMapB[i]*0.03
      elif (piece == 22):
         accum = accum - 50 - heatMapB[i]*0.025
      elif piece == 23:
         accum = accum -90 - heatMapB[i]*0.05
      elif piece == 24:
         accum = accum -130 -heatMapB[i]*0.035
      elif piece == 25:
         accum = accum - 100000 + heatMapKing[i]*0.5
        # if isPositionUnderThreat(board,i,20):
        #    accum = accum + 1000
      elif piece == 10:
         accum = accum + 30 + heatMapWP[i]*0.02
      elif (piece == 11):
         accum = accum + 50 + heatMapW[i]*0.03
      elif (piece == 12):
         accum = accum + 50 + heatMapW[i]*0.025
      elif piece == 13:
         accum = accum + 90 + heatMapW[i]*0.05
      elif piece == 14:
         accum = accum + 130 + heatMapW[i]*0.035
      elif piece == 15:
         accum = accum + 100000 - heatMapKing[i]*0.5 
         #if isPositionUnderThreat(board,i,10):
         #   accum = accum - 1000
   if accum > 80000.0:
      return 100000.0
   elif accum < -80000.0:
      return -100000.0

   return accum

def GetPieceLegalMoves(board,pos):
   accum = []
   isBlack = False 
   if(board[pos] >= 20):
      isBlack = True
      piece = board[pos]-20
   elif (board[pos] >= 10):
      piece = board[pos]-10
   else:
      return []

   if piece == 0:
      #Pawn
      if isBlack == False:
         tempPos = pos + 8
         if pos + 8 < 63:
            present = isPresent(board,pos + 8)
            if (present[0] == False):      
               accum = accum + posIsLegal(board,pos+8,isBlack)

            present = isPresent(board,pos + 7)         
            if (pos % 8 != 0):
               if(present[0]):
                  if(present[1] != isBlack):
                     accum = accum + [pos + 7] 
            present = isPresent(board,pos+ 9)
            if pos%8 != 7:
               if (present[0] == True):
                  if (present[1] != isBlack):
                     accum = accum + [tempPos]   

      else:
         tempPos = pos - 8
         if isPresent(board,tempPos) == [False,False]:      
            accum = accum + [tempPos]         
  
         tempPos = pos - 7
         present = (isPresent(board,tempPos))
   
         if (present[0] == True) & (present[1] != isBlack) & (pos % 8 != 7):
            accum = accum + [tempPos]   
 
         tempPos = pos - 9
         present = (isPresent(board,tempPos))
   
         if (present[0] == True) & (present[1] != isBlack) & (pos %8 != 0):
            accum = accum + [tempPos]   
     

   elif piece == 1:
      #Knight
      if(pos%8 !=0):
         accum = accum + posIsLegal(board,pos-17, isBlack)
         if (pos <48):
            accum = accum + posIsLegal(board,pos+15, isBlack)

      if(pos%8 !=7):
         accum = accum + posIsLegal(board,pos+17, isBlack)
         if(pos > 15):
            accum = accum + posIsLegal(board,pos-15, isBlack)

      if(pos%8 > 1):
         if(pos > 9):
            accum = accum + posIsLegal(board,pos-10, isBlack)
         if(pos < 56):
            accum = accum + posIsLegal(board,pos+6, isBlack)

      if (pos%8 < 6):
         if(pos < 54):
            accum = accum + posIsLegal(board,pos+10, isBlack)
         if(pos > 7):
            accum = accum + posIsLegal(board,pos-6, isBlack)
 
   elif piece == 2: 
      #Bishop

      nextA = True
      nextB = True
      nextC = True
      nextD = True

      right = pos%8
      left = 7-pos%8
    
      maximum = max(left,right)

      for i in range(1,maximum+1,1):

         if ((pos+9*i) % 8) == 0:
            nextA = False
         if (nextA != False):
            accum = accum + posIsLegal(board,(pos + 9*i),isBlack)
            if pos + 9*i < 64:
               if(board[pos+9*i] !=0):
                  nextA = False


         if ((pos + 7*i)%8) == 7:
            nextB = False
         if (nextB != False):  
            accum = accum + posIsLegal(board,pos + 7*i,isBlack)  
            if pos + 7*i < 64:
               if(board[pos+7*i] != 0):
                  nextB = False


         if ((pos -9*i)%8) ==7:
            nextC = False
         if nextC != False:  
            accum = accum + posIsLegal(board,pos + -9*i,isBlack)
         #if(isPresent(board,pos - 9*i)[0] == True):
            if pos -9*i > -1:
               if board[pos-9*i] != 0:
                  nextC = False


         if (pos -7*i)%8 == 0:
            nextD = False
         if nextD != False :  
            accum = accum + posIsLegal(board,pos + -7*i,isBlack) 
         #if(isPresent(board,pos - 7*i)[0] == True):
            if pos -7*i > -1:
               if board[pos-7*i] != 0:
                  nextD = False      
                          
   elif piece == 3:
      #Rook
      top = (int)(8 - (pos + pos%8)/8)
      bottom = 7-top
      maximumA = max(top,bottom)

      left = 7-pos%8
      right = pos%8
      maximumB = max(right,left)
  
      maximum = max(maximumA,maximumB)


      nextA = True
      nextB = True
      nextC = True
      nextD = True
      for i in range(1,maximum+1,1):
         if ( i<= maximumA + 1):
            if (pos + 8*i) > 63:
               nextA = False       
            if (nextA != False):
               accum = accum + posIsLegal(board,pos+i*8,isBlack)
          #  if (isPresent(board,pos+8*i)[0] == True):
               if pos + i*8 < 64:
                 if board[pos+i*8] != 0:
                     nextA = False

            if (pos -8*i) < 0:
               nextB = False       
            if (nextB != False):
               accum = accum + posIsLegal(board,pos-8*i,isBlack)
               if pos -8*i > -1:
                  if board[pos-i*8] != 0:
             #if (isPresent(board,pos-8*i)[0] == True):
                     nextB = False

         if (i <= maximumB+1):        
            if (pos + i)%8 == 0:
               nextC = False       
            if (nextC != False):
               accum = accum + posIsLegal(board,pos+i,isBlack)
               if board[pos+i] != 0: #if (isPresent(board,pos+i)[0] == True):
                  nextC = False

            if (pos - i)%8 == 7:
               nextD = False       
            if (nextD != False):
               accum = accum + posIsLegal(board,pos-i,isBlack)
               if board[pos-i] != 0:#if (isPresent(board,pos-i)[0] == True):
                  nextD = False

   elif piece == 4:
      #Queen
    
      top = (int)(8 - (pos + pos%8)/8)
      bottom = 7-top
      maximumA = max(top,bottom)

      left = 7-pos%8
      right = pos%8
      maximumB = max(right,left)
  
      maximum = max(maximumA,maximumB)


      nextA = True
      nextB = True
      nextC = True
      nextD = True
      diagR = True
      diagL = True
      diagr = True
      diagl = True
      for i in range(1,maximum+1,1):
       if ( i <= maximumA + 1):
         if (pos + 8*i) > 63:
            nextA = False       
         if (nextA != False):
            accum = accum + posIsLegal(board,pos+i*8,isBlack)
            if board[pos+i*8] != 0:#if (isPresent(board,pos+8*i)[0] == True):
               nextA = False

         if (pos -8*i) < 0:
            nextB = False       
         if (nextB != False):
            accum = accum + posIsLegal(board,pos-8*i,isBlack)
            if board[pos-i*8] != 0:#if (isPresent(board,pos-8*i)[0] == True):
               nextB = False


       if (i <= maximumB+1):    
    
         if (pos + i)%8 == 0:
            nextC = False       
         if (nextC != False):
            accum = accum + posIsLegal(board,pos+i,isBlack)
            if diagR:
               if pos + 9*i < 64:
                  accum = accum + posIsLegal(board,(pos + 9*i),isBlack)
                  if board[pos+i*9] != 0: #if(isPresent(board,pos + 9*i)[0]):
                     diagR = False 
            if diagl:
               if pos -7*i > -1:
                  accum = accum + posIsLegal(board,pos + -7*i,isBlack)
                  if board[pos-i*7] != 0:#if(isPresent(board,pos -7*i)[0]):
                     diagl = False
           

            if board[pos+i] != 0: #(isPresent(board,pos+i)[0] == True):
               nextC = False

         if (pos - i)%8 == 7:
            nextD = False       
         if (nextD != False):
            accum = accum + posIsLegal(board,pos-i,isBlack)
            if diagr:
               if pos -9*i > -1:
                  accum = accum + posIsLegal(board,(pos - 9*i),isBlack)
                  if board[pos-i*9] != 0: #if(isPresent(board,pos - 9*i)[0] == True):
                     diagr = False
            if diagL:
               if pos + 7*i < 64:
                  accum = accum + posIsLegal(board,pos + 7*i,isBlack)
                  if board[pos+i*7] != 0: #if(isPresent(board,pos +7*i)[0] == True):
                     diagL = False
            
            if board[pos-i] != 0:#if (isPresent(board,pos-i)[0] == True):
               nextD = False
   elif piece == 5:
      #King
      if (pos%8 !=7):
         if posIsLegal(board,pos+9,isBlack) == [pos+9]:
            accum = accum + [pos+9]
         if posIsLegal(board,pos-7,isBlack) == [pos-7]:
            accum = accum + [pos-7]
         if posIsLegal(board,pos+1,isBlack) == [pos+1]:
            accum = accum + [pos+1]

      if(pos%8 !=0):
         if posIsLegal(board,pos-9,isBlack) == [pos-9]:
            accum = accum + [pos-9]
         if posIsLegal(board,pos+7,isBlack) == [pos+7]:
            accum = accum + [pos+7]
         if posIsLegal(board,pos-1,isBlack) == [pos-1]:
            accum = accum + [pos-1]

      if ((pos + 8) < 64):
         if posIsLegal(board,pos+8,isBlack) == [pos+8]:
           accum = accum + [pos+8]

      if ((pos -8) > -1):
        if posIsLegal(board,pos-8,isBlack) == [pos-8]:
           accum = accum + [pos-8]
  
   return accum

def GenMoves(board,player,depth):
   opp = 10
   if player == 10:
      opp = 20

   if depth == 3:
      return []
   curScore = GetPoints(board)
   if curScore%100000 == 0:
      if curScore != 0:
         return []
 
   children = [] 
   
   playerPositions = GetPlayerPositions(board,player)
   testBoard = list(board)
   for pos in playerPositions:
      moves = GetPieceLegalMoves(board,pos)
      for move in moves:
         previous = testBoard[move]
         testBoard[move] = testBoard[pos]
         testBoard[pos] = 0
         score = GetPoints(testBoard)
           
         child = tree([pos,move],score)
         child.children = GenMoves(testBoard,opp,depth + 1)
         children = children + [child]
       
         testBoard[pos] = testBoard[move]
         testBoard[move] = previous
         
   return children



def minMax(node,depth,maximizing):
   if depth == 0:# | checkmate(board,10) == True| checkmate(board,20) == True:
      return [node.candidateMove[0],node.candidateMove[1]]
   elif (node.candidateMove[1])%1000000 == 0:
      if node.candidateMove[1] != 0:
         return [node.candidateMove[0],node.candidateMove[1]]

   bestMove = []
   if maximizing:
      maxEval = - 1000000
      for child in node.children:
         curEval = minMax(child,depth-1,False)
         if maxEval < curEval[1]:
            bestMove = child.candidateMove[0]
            maxEval = curEval[1]
    #     alpha = max(alpha,maxEval)
    #     if beta <= alpha:
    #        break
      return [bestMove,maxEval]
   else:
      minEval = 1000000
      for child in node.children:
         curEval = minMax(child,depth-1,True)   
         if minEval > curEval[1]:
            bestMove = child.candidateMove[0]
            minEval = curEval[1]
   #      beta = min(beta,minEval)
   #      if beta <= alpha:
   #         break
      return [bestMove,minEval]


def brain(node):
#   accum = []

#   maximum = -100000
#   for child in node.children:
#      accum = accum + [minMax(child,2,-100000,1000000,False)] 
#   for i in range(0,len(accum),1):
#      if maximum <= accum[i][0]:
#         maximum = accum[i][0]
#         best = accum[i]
#   return best
   return minMax(node,3,True) 



def printBoard(board):
   msg = ""
   for i in range(7,-1,-1):
      for j in range(7,-1,-1):
        # msg = msg + " " +str(j + i*8)
         if(board[j+i*8] == 0):
            msg = msg +" 00"
         else:
            msg = msg +" "+ str(board[j + i*8])
      print(msg)
      msg = ""
   return True

def getCandidates(moves):
 accum = []
 for move in moves:
      accum = accum + [move.candidateMove]
 return accum
     
def test():
   board = init()
   board[36] = 14
   board[7] = 0
   board[4] = 23
   board[12] = 0
   board[11] = 0
   board[51] = 24
   board[60] = 0
   board[52] = 0
   printBoard(board)
   
   print(GetPoints(board))

   print("Player White")
   print(GetPlayerPositions(board,10))
   print("Player Black")
   print(GetPlayerPositions(board,20))
   print(GetPieceLegalMoves(board,51))
   print("Genned Moves for white")
   moves = GenMoves(board,10,0)
   node = tree([],0)
   node.children = moves
   print(getCandidates(moves))
   print(brain(node))

