A = []

for v in range(5):
    A.append(int(input("Enter a number : ")))

print("Array is : ",A)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r-1):
        if A[j]<=x:
            i = i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return (i+1)


partition(A, 0, len(A) - 1)
print("Array after partitioning:", A)


def quicksort(A,p,r):
    if p < r:
        q = partition(A, 0, len(A) - 1)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)


quicksort(A, 0, len(A) - 1)
print("Array after quicksort : ",A)
