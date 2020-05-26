# Program for Bubble sort 
#defining the function
def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
num= [55,58,69,35,147,25]
#To test this for random input array just replace above line by the following code 
'''
num = []
t  = int(input()) #This is the length of the array 
for k in range(t):
    num.append(int(input()))
'''
#print num in starting so that that we can easily compare on the console finally
print(num)
sort(num)
#printing the array after sorting
print(num)

