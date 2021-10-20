'''
this program takes an integer less than 1000 and output the least power of 2 that is greater than n
'''



list = []

for i in range(1, 1001):
    list.append(pow(2, i))


# for i in range(10):
#     print(list[i])

testcases = int(input("how many time do you want to play? "))
count = 0
while( count < testcases ):
    numb = int(input())
    for i in range(1000):
        if numb < list[i]:
            print(list[i])
            break

    count += 1