# Program for Selection sort 
def sort(num):
    for i in range(4):
        min_pos = i
        for j in range(i,5):
            if num[j]<num[min_pos]:
                min_pos = j 
        temp = num[i]
        num[i]=num[min_pos]
        num[min_pos]=temp
        print(num)
num = [45,98,26,45,79]
sort(num)
