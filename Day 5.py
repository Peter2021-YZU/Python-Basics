import random

size = 10 #set the size of the list
lyst = [] #Create an empty list


#input element to the list from the computer
for count in range(size):
    lyst.append(random.randint(1,size+1))

print(lyst)


lyst.append(5) #Add five to the end of the list
print(lyst) #List contains 5 in the end


lyst.extend([6, 2, 5]) #add two elements to the end of the list
print(lyst) #list contains 5, 6, 2 in the end


lyst.index(6) #return the primary appearance of the 6 in the list


listMax = max(lyst) #Assign the highest value in the list to listMax
print(listMax)


lyst.insert(3, 7) #Insert 7 in the third position of the list


x = lyst.count(2) #Assign how many times the the number of time 2 appears in the list to x
print(x)


lyst.pop() #remove the last element in the list
print(lyst)


lyst.reverse() #Reverse all the element in the list
print(lyst)


lyst.clear() #Convert the list back to an empty list
print(lyst)

