#author: Tucker Ferguson
#the first try except will not result in exeption

listA = [1,2,3,4,5] 
numA = 3;


try :
    for x in listA :
        if(int(x) == 3): 
            print('good type');
except TypeError :
    print("bad type")
    
    
#this throws exception error however    
    
    
try: 
    for x in listA :
        if(x / 0 == 1):
            print("wont get here")
except ZeroDivisionError :
    print("exception occurred")