def section_sort(arr):
    n = len(arr)
    for j in range(n-1):
        smallest = j
        for i in range(j+1,n):
            if arr[i]<arr[smallest]:
                smallest = i
        arr[j],arr[smallest] = arr[smallest],arr[j]


arr = [64,25,12,22,11]
section_sort(arr)
print("Sorted array is : ", arr)
