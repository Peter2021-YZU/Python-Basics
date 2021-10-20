'''
this program takes an integer less than 1000 and output the least power of 2 that is greater than n
'''


#create a list and add all power of 2 from 2 to 1000 in it
list = []
for i in range(1, 1001):
    list.append(pow(2, i))


#input the number of cases from keyboard
testcases = int(input("how many time do you want to play? "))
count = 0  #initialize the couter of number of time user plays to 0
while( count < testcases ):
    numb = int(input()) #input number from keyboard
    for i in range(1000): #search in the list the least power of 2 grader than the number input by keyboard
        if numb < list[i]:
            print(list[i])
            break

    count += 1
