import random

def bubble(arr, n):
    bcount = 0
    for i in range(n-1):
        for j in range(n-1-i):
            bcount += 1
            if(arr[j] > arr[j+1])
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



n = int(input("Enter n: "))
print("Initializing", n, "random elements..")
arr = []
for i in range(n):
    arr.append(random.randint(0, n))

print()
print("Comparisions for: ")
print("Bubble sort:", bubble(arr, len(arr)))
print("Selection sort:", selection(arr, len(arr)))
