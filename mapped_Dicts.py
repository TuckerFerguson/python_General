import collections

"""
@author Tucker Ferguson
2/14/2020

This program will explore maps (chain mapping) in python.
In order to do this we will utilize the ChainMap() function from 
collections module
"""

#First lets define/initialize 3 dictionaries
catDict = { "Charles":"Orange Tabby",
            "Bingo":"Grey Persian",
            "Patchy":"Black Siamese"
          }
          
dogDict = { "Rover":"Red Labrador",
            "Lulu":"Black Chihuahua",
            "Holly":"Black/White Kelpie"
          }
          
etcDict = { "Paul":"Green Chameleon",
            "Rover":"Blue Flamingo",
            "Stacy":"Yellow Mongoose"
          }
          
#Next lets club them together using collections ChainMap()
AnimalDict = collections.ChainMap(catDict,dogDict,etcDict)

#Lets view our new AnimalDictionary by utilizing maps
print(AnimalDict.maps,"\n\n")

#View our keys and values notice this removes any duplicate keys "Rover"
print("Keys: {}".format(list(AnimalDict.keys())))
print("\n")
print("Values: {}".format(list(AnimalDict.values())))
print("\n")
print("Lets clean it up :) \n")
print("\t   [Pet Table]")
print("\t=================")
#Beautiful compact code (this is why I love python)
for i,(keys,vals) in enumerate(AnimalDict.items()) :
    print("{}) {} : {}".format(i+1,keys,vals))



