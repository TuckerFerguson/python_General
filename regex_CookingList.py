# @author Tucker Ferguson
# 1/27/2020
#
#         We are given a cooking recipe written by your grandmother.
#         This recipe is not only hard to read but it is torn into two pieces (oh great!..)
#
#         Lets extract some crucial information using regex! 
#

import re

# 1) lets apply concatination to combine the ripped recipe!
ugly_Directions = "1: crack eggs. 2: pour flour and milk in bowl. 3: pour in eggs and stir."
ugly_Directionsp2 = "4: put mixture in oven safe container. 5: bake for 30 minutes. 6: take out and let cool."
ugly_Directions = ugly_Directions + ugly_Directionsp2

print("We are given a cooking recipe written by your grandmother.\nThis recipe is not only hard to read..,\nbut it is torn into two pieces (oh great!)\n")
print("lets fix it with the help of python and regular expressions!\n")

print("\nWith concatination we can 'tape' the recipe back together!\n")
print("fixed_Recipe = ugly_Directions + ugly_Direectionsp2\n")
print("Next lets use regular expressions to find number of steps\n")
print('using re.findall "(\w:)"\n')

# 2) next I need to get some basic information about our recipe such as how many steps there are!

#Each step has a digit followed by a colon preceeding it, we can leverage this using regex
pattern = r"(\w:)"

#Find the total number of times this pattern appears in our list!
direction_List = re.findall(pattern,ugly_Directions)
print(direction_List)

print("\nOkay so the recipe has {} steps! That helps\n".format(len(direction_List)))

# 3) Lets associate the step number and the actual directions!
new_pattern = r"(\w:)\s([\w\s]*)"
direction_List = re.findall(new_pattern,ugly_Directions)

print("Great now I have a clean easy to read list!!\n")
for verb in direction_List :
    print("{} {}".format(verb[0],verb[1]))
    
