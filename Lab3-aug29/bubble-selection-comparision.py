import random

mcount = 0

def bubble(arr, n):
    bcount = 0
    for i in range(n-1):
        for j in range(n-1-i):
            bcount += 1
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return bcount


def selection(arr, n):
    scount = 0
    for i in range(n-1):
        small = i
        for j in range(i+1, n):
            scount += 1
            if(arr[j] < small):
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return scount


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
        global mcount
        mcount += 1
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


n = int(input("Enter n: "))
print("Initializing", n, "random elements..")
arr = []
for i in range(n):
    arr.append(random.randint(0, n))

print()
print("No. of comparisions for: ")
print("Bubble sort:", bubble(arr, len(arr)))
print("Selection sort:", selection(arr, len(arr)))
mergeSort(arr, 0, len(arr)-1)
print("Merge sort:", mcount)
