#Program for Binary Search
pos = -1
def bSearch(num,target):
    sorted(num)
    lower=0
    upper=len(num)-1
    while lower<=upper:
        mid = (lower+upper)//2  
        if num[mid]== target:
            globals()['pos'] = mid
            return True
        else:
            if(num[mid]<target):
                lower=mid
            else:
                upper=mid
    return False
num=[2,5,4,6,7,8,9]
target = int(input())
if bSearch(num,target):
    print('Found @ ', pos+1)
else:
    print("Not Found!!")
    
