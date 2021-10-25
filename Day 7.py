#Create a dictionary and print it
myDict = {
    "FirstName": "John Peterson",
    "LastName": "Valcourt",
    "Age": "22",
    "Nationality": "Haitian"
}
print(myDict)


#Use the key LastName to print the its value
print(myDict["LastName"])


#print the length of the dictionary
print(len(myDict))


#Access a value of a specific key in my dictionary
nation = myDict["Nationality"]
print(nation)

#use get to access the value of a key in my dictionary
nation = myDict.get("Nationality")
print(nation)


#get the list of the keys in my dictionary
lyst = myDict.keys()
print(lyst)


#get the list of the values in my dictionary
lyst = myDict.values()
print(lyst)


#get the items in my dictionary
lyst = myDict.items()
print(lyst)


#check if a certain key exist in my list
if "FirstName" in myDict:
    print("Yes it is in my dic")
