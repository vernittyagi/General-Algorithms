# Second Largst element in an array 
        
def sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
    
def secondlargest(num):
    t =sort(num)
    return t[t.index(max(num))-1]

num=[5,4,6,7,8,9,1,10,1245]
result = secondlargest(num)
print(result)
