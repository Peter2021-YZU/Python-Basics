"""
this program is to sort the elements in a list in ascending order
"""

#write a function to swap two elements in a list
def swap(list, leftIndex, rightIndex):
    temp = list[leftIndex]
    list[leftIndex] = list[rightIndex]
    list[rightIndex] = temp



list = [1,2,4,3,67,5,4,7,2,13, 93,2, -1]


#compare each single element in the list to the rest of the elements in the list insert it in its proper place 
for i in range(len(list)):
    for j in (range(i, len(list))):
        if( list[i] > list[j]): #
            swap(list, i, j)

print(list)