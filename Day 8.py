myDict = {
    "FirstName": "John Peterson",
    "LastName": "Valcourt",
    "Age": "22",
    "Nationality": "Haitian"
}


# change a specific item in my dictionary
myDict["Nationality"] = "American"
print(myDict)


# Add a item in my dictionary
myDict["Residency"] = "Taiwan"
print("myDict")


# use pop to remove a specific item in my dictionary
myDict.pop("Nationality")
print(myDict)


# use popittem to remove the last item in my dictionary
myDict.popitem()
print(myDict)


# use del keyword to remove a specific item in my dictionary
del myDict["Age"]
print(myDict)


# loop through my dictionary
for x in myDict:
    print(myDict[x])


# use the function keys() to return all the keys in my dictionary
for x in myDict.keys():
    print(x)

# use the function keys() to return all the keys in my dictionary
for x,y in myDict.items():
    print(x,y)


# Create 2 new dictionary
sisDict = {
    "FirstName": "Wilberte",
    "LastName": "Valcourt",
}

lilSisDict = {
    "FirstName": "Stephie",
    "LastName": "Desir",
}

# create a nested dictionary with my 3 dictionaries
myfamily = {
    "me" : myDict,
    "sister" : sisDict,
    "lilSis" : lilSisDict
}
print(myfamily)