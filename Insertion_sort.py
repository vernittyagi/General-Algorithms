#code for insertion sort 
def sort(num):
    for i in range(1,len(num)):
        key = num[i]
        j = i-1
        while j>=0 and num[j] > key:
            num[j+1] = num[j]
            j-=1 
        num[j+1] = key
num= [4,6,2,3,5,9]
sort(num)
for i in range(len(num)):
    print("%d"%num[i])
