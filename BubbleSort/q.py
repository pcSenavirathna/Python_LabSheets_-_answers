A = []

for v in range(0,8):
    A.append(int(input("Enter the number : ")))

print()
print("Array is : ",A)

def bubblesort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
            

bubblesort(A)
print("Sorted Array : ",A)
