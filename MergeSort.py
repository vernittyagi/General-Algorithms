#Program  for Merge Sort 

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2 
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        #Now copy the data in the temp Lists
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k] = R[j] 
                j+=1 
            k+=1
        #Now checking for any element wont left
        while i<len(L):
            arr[k]=L[i]
            i+=1 
            k+=1
                
        while j<len(R):
            arr[k]=R[j]
            j+=1 
            k+=1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end="")
#Driver Function for the program
if __name__ == '__main__':
    arr = [5,1,9,7,3,4,6,8,2]
    printList(arr)
    print()
    mergeSort(arr)
    printList(arr)
