class queue:
   def __init__(self):
      self.x = []

   def enqueue(self,val):
      self.x = self.x + [val]
      return True

   def dequeue(self):
      if self.x != []:
         val = self.x[0]
         self.x = self.x[1:]
         return val
      return []


