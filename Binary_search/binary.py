arr = []

for v in range(4):
    arr.append(int(input("Enter a number : ")))

print(arr)

x = int(input("Enter a search value : "))


def binary_search(arr,min,max,x):
    if(max<min):
        return False
    else:
        mid = (min+max)//2
        if(arr[mid] > x):
            return binary_search(arr,min,mid-1,x)
        elif arr[mid] < x:
            return binary_search(arr,mid+1,max,x)
        else:
            return mid

#binary_search funtion call
q = binary_search(arr,0,len(arr)-1,x)

print("Element is presant at : ",q)
