#The following code is for to find Maximum number from an given array

array = list(map(int, input().split()))

if not array:  # Check if the array is empty
    print("Array is empty.")
else:
    arr = array[0]  # Initialize arr with the first element
    for i in range(1, len(array)):
        if arr < array[i]:
            arr = array[i]
    
    print(arr)


