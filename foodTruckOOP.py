#@author Tucker Ferguson
#12/30/2019
#**************************************
#* Demonstration of OOP using classes *
#**************************************

#Creating class 'foodTruck' 
class foodTruck :
    def __init__(self,truckType,FoodItems) :
        self.truckType = truckType
        self.FoodItems = FoodItems

#Now lets create some foodTruck Objects
JohnsTruck = foodTruck("Italian",['pizza','spagetti,garlic bread'])
SarahsTruck = foodTruck("Salad",["Caesar", "House","Southwestern"])
RicksTruck = foodTruck("Mexican",['tacos','tortillas', 'nachos'])

#access data elements from these newly constructed objects
print("""
    I am hungry for something healthy..
    how about a {0}!
    
    * 5 minutes later... *
    
    Hello there can I order a {1} {0} !?
    Thank you this it looks delicious!
    
    """.format(SarahsTruck.truckType,SarahsTruck.FoodItems[1]))