#Defining the function for partition process
def partition(arr,low,high):
    i = low-1  
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
#defining the function for quicksort
def quicksort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
#defining the function for printLst
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
#Driver code
if __name__=='__main__':
    arr = [3,2,6,1,5,9,4,8,7]
    printList(arr)
    print()
    n = len(arr)
    quicksort(arr,0,n-1)
    printList(arr)
