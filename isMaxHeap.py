def isMaxHeap(arr):
    n = len(arr)
    for i in range(1, n // 2):
        if (2*i + 1) < n:
            if arr[i] < max(arr[2 * i], arr[i*2 + 1]):
                return False
        else:
            if arr[i] < arr[2*i]:
                return False
    return True


if __name__ == "__main__":
    arr = [0]
    arr1 = list(map(int, input("Enter array: ").split()))
    for a in arr1:
        arr.append(a)
    print(isMaxHeap(arr))


"""
OUTPUT

Enter array: 90 15 10 7 12 2
True

Enter array: 9 15 10 7 12 11
False
"""