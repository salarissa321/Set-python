


#---------------
#----Set-----
#-----------------
# [1] Set Items Are enclosed in curly Braces
# [2] Set Items Are not Orederd and not Indexed
# [3] Set Indexing and Slicing cant be Done
# [4] Set has Only Immutable Data Types (List, Strings, Tuples) List and Dict Are Not 
# [5] Set Items Is Unique
#------------------



# not Orederd and not Indexed

mySetOne= {"Salar" , "Issa", 100}
print(mySetOne) # {'Salar', 'Issa', 100} # {'Issa', 100, 'Salar'} # {'Salar', 100, 'Issa'} # {100, 'Salar', 'Issa'}
# print(mySetOne[0]) # TypeError: 'set' object is not subscriptable


# Slicing cant be Done

mySetTwo = {1,2,3,4,5,6,7}
# print(mySetTwo[0:3]) # TypeError: 'set' object is not subscriptable



# Set has Only Immutable Data Types

# mySetThree = {1, "Salar" , 23.87 , True , [1,2,3]} # TypeError: unhashable type: 'list'
# mySetThree = {1, "Salar" , 23.87 , True , {1,2,3}} # unhashable type: 'set'
mySetThree = {1, "Salar" , 23.87 , True , (1,2,3)} # {1, 'Salar', (1, 2, 3), 23.87}
print(mySetThree) 


# Set Items Is Unique

mySetFour = {1, 2, "Salar" , "One" , "Salar" , 1}
print(mySetFour) # {1, 2, 'Salar', 'One'}



