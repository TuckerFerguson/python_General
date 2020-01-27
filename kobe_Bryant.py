#
# @author: Tucker Ferguson
# 1/26/2020
#
# Using software as my media to express mourning the passing of an athlete, father pop - culture legend.
#

"""                  Click Run                """

def hidden(legend) :
    kobj = Kobe(legend)
    kobj.printString()
    

class Kobe :
    def __init__(self, legacy):
        self.legacy = legacy
    def printString(self) :
        print(self.legacy)




legend = """
           ________
     o    |   __   |
     \_ O |  |__|  |
  ____/ \ |___WW___|  Kobe Bryant
  __/   /     ||      1978 - 2020 
              ||             
              || "Five rings, never forgotten"
______________||________________________________

 
"""
hidden(legend)


