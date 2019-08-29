def partition(arr,l,h): 
    i = ( l-1 )       
    pi = arr[h]    
  
    for j in range(l , h): 
        if   arr[j] < pi: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,l,h): 
    if l < h: 

        pi = partition(arr,l,h) 
  
        quickSort(arr, l, pi-1) 
        quickSort(arr, pi+1, h) 


arr = list(map(int, input("Enter the array: ").split())) 
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is: ") 
print(*arr, end=' ')
print()
