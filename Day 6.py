"""
This program is to learn how to manipulate tuples
"""


myTuple = ("Jan", "Fev", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec")
print(myTuple)

#print the lenth of my tuple
print(len(myTuple))


#A tuple with one element always has the commas
newTuple = ("Potatoes", )
print(type(newTuple))
notTuple = ("Potatoe")
print(type(notTuple))


#Access elements in a tuple through a loop
for i in range(len(myTuple)):
    print(myTuple[i])


#determine if a specific element is in a tuple
if "Mar" in myTuple:
    print("Yes Mar is in the tuple")

#As tuple are unchangeable, use list to update a tuple
lyst = list(myTuple)
lyst[2] = "March"
lyst.remove("Dec")
myTuple = tuple(lyst)
print(myTuple)


#add a tuple to another tuple
decTuple = ("December", )
myTuple += decTuple
print(myTuple)
