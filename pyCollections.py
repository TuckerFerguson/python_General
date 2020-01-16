#@author Tucker Ferguson
#12/30/2019
#***********************************************
#* Comparison: List and Sets                   *
#***********************************************

"""
List: Ordered, nmutable, Slower to iterate, Varying Datatypes allowed
"""

listExample = [1,"two",3,"four",5]
print("Starting List: {0}\n".format(listExample))

#Using built-in 'enumerate()' a list can be traveresed by value and index
for i, vals in enumerate(listExample) :
    print("{0} has the index: {1}".format(vals,i))
print("\n")

#Values contained in lists are mutable (can be modified)
for i,vals in enumerate(listExample) :
    if listExample[i] == "two" :
        print("%s is now %d "%(vals,2))
        listExample[i] = 2
    elif listExample[i] == "four" :
        print("%s is now %d "%(vals,4))
        listExample[i] = 4
print("\nNewly Created 'fixed' list: {0}\n".format(listExample))



"""
Set: Unordered, No Duplicates, Inmutable
"""
setExample = {'a','b','c','d'}

#Demonstrates that sets are not ordered immediately upon initialiazation
print("Starting Set: {0}\n".format(setExample))

#No duplicate values can exist in a set
for char in 'abcdef' :
    print("adding: {0}\n".format(char))
    setExample.add(char)
print("See no duplicates: {0}\n".format(setExample))

#***********************************************
#* Comparison: List, Set, Dictionaries, Tuples. *
#***********************************************

"""
List: Ordered, nmutable, Slower to iterate, Varying Datatypes allowed
"""

listExample = [1,"two",3,"four",5]
print("Starting List: {0}\n".format(listExample))

#Using built-in 'enumerate()' a list can be traveresed by value and index
for i, vals in enumerate(listExample) :
    print("{0} has the index: {1}".format(vals,i))

#Values contained in lists are mutable (can be modified)
for i,vals in enumerate(listExample) :
    if listExample[i] == "two" :
        print("%s is now %d "%(vals,2))
        listExample[i] = 2
    elif listExample[i] == "four" :
        print("%s is now %d "%(vals,4))
        listExample[i] = 4
print("Newly Created 'fixed' list: {0}\n".format(listExample))






