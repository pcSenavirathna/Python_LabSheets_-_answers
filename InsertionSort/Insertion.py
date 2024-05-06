a = []

for v in range(10,20):
    a.append(int(input("Enter a number : ")))

print(a)

def insertion(a):
    for j in range(0,len(a)):
        key = a[j]
        i = j-1
        while i>0 and a[i] > key:
            a[i+1] = a[i]
            i=i-1
        a[i+1] = key

insertion(a)

print("sorted array : ",a)
