import random

class Dice:

    # rolling from 1-6 and converting it to 1-4 valuse keeping the occurance 
    def Roll (self) -> int:
      nVal = random.randint(1, 6)        
      match nVal:
         case 1: 
            return 1
         case 2:
            return 2
         case 3: 
            return 2 
         case 4: 
            return 3
         case 5: 
            return 3
         case 6: 
            return 4
         case _ :
            return -1 
         
    def RollTest(self):
      lTestThrows = 4* [0]
      for i in range(10000):
        nRoll = self.Roll()
        lTestThrows[nRoll-1] += 1


         
         
