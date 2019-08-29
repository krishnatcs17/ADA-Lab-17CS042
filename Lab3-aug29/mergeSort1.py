def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
  
    L = [0] * n1
    R = [0] * n2
  
     
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
     
    i = 0      
    j = 0    
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  

    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
 
def mergeSort(arr,l,n): 
    if l < n: 
        m = (l+(n-1))//2
  
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, n) 
        merge(arr, l, m, n) 
  
  
arr = list(map(int, input("Enter the numbers: ").split()))
n = len(arr)

mergeSort(arr,0,n-1) 
print ("\n\nSorted array is: ") 
print(*arr, end=' ')
print()


'''
OUTPUT

Enter the numbers: 4 6 78 4 2 


Sorted array is: 
2 4 4 6 78 

'''