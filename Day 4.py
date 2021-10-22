"""
This program helps to search an element in an ordered list (binary search)
"""

def binarySearch(lyst, element, left, right):#take the list, the element we want to find and the first and the last index
    while left <= right:#divide the list into the grop and serch from the left to the right until they become the same element
        middle = (left + right) // 2 #verify if the element in the middle of list is the element that we are searching
        if(lyst[middle] == element):
            return middle
        elif(lyst[middle] < element): #if it's not and the middle is less than the element, search in the right side of the list
            left = middle+1
        else:
            right = middle-1 #if the middle is greater than the element, search in the left side of the list
    return -1 #return -1 if the element is not found


lyst = [1,2,3,4,5,6,7,8,10,17,20]
left = 0
right = len(lyst)-1
element = 10

index = binarySearch(lyst, element, left, right)
if index == -1:
    print("Not in it")
else:
    print("in it")
