#@author: Tucker Ferguson
#1/3/2020
"""
***********************************
This is an example of a 'dunder'  *
or 'magic method' use case        *
***********************************
"""


#delcare class "vector
class vector :
#magic method or dunder used to initialize objects data values
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        
#magic method or duner used to add objects datafields together
    def __add__(self,other) :
        return vector(self.x - other.x, self.y - other.y)
        
        
#create two 'vector' objects
vector1 = vector(16,38)
vector2 = vector(3,1)

#preform an overloaded subtraction method on two different vector objects
outputVector = vector1 + vector2
print("""
    Vector Subtraction: ({0},{1}) - ({2},{3})
    
       ********************************      
      *                                *
     **                                **
    ***    Resulting vector : {4},{5}    ***
     **                                **
      *                                *
       ********************************
      """.format(vector1.x,vector1.y,vector2.x,vector2.y,outputVector.x,outputVector.y))
