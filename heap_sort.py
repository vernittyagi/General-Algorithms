def heapify(arr,n,i):
    largest = i
    l=2*i+1
    r=2*i+2
    if l<n and arr[i]<arr[l]:
        largest = l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    #building a max heap
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)
    #now after heapifying just extract the elements
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)  
#Driver Code
if __name__ == '__main__':

    arr = [3,2,6,1,5,9,4,8,7]
    heapsort(arr)
    print('sorted array is: ')
    for i in range(len(arr)):
                   print(arr[i],end=" ")
