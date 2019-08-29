qcount = 0
def partition(arr,l,h): 
    i = ( l-1 )       
    pi = arr[h]    
  
    for j in range(l , h): 
        global qcount
        qcount += 1
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
print("Number of comparisions:", qcount)


'''

OUTPUT

Enter the array: 8 5 6 3 4 2
Sorted array is: 
2 3 4 5 6 8 
Number of comparisions: 13

'''