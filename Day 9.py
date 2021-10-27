#create a set and print its items
mySet = {"banana", "apple", "avocado"}
print(mySet)

mySet = {"banana", "apple", "avocado", "banana"}
print(mySet) # as set doesn't allow duplicate values, banana will appear only once


# Get the length of the set
print(len(mySet))


# set can contains different data types
mySet = {"banana", "apple", "avocado", "banana", "false", "65"}
print(mySet)


# use the set constructor (always with double round-brackets) to make a set
mySet = set(("banana", "apple", "avocado"))
print(mySet)


# Access the item in my set through a loop
for x in mySet:
    print(x)

# add an item in my set
mySet.add("cherry")
print(mySet)


# add another set to my set
otherSet = {"false", "65"} # otherSet can also be a list
mySet.update(otherSet)
print(mySet)

# join two sets together into a third one using union()
otherSet = {"true", "96"}
newSet = mySet.union(otherSet)
print(newSet)


# remove an element from my set
mySet.remove("apple")
print(mySet)
