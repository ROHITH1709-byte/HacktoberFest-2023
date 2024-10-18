def insertion_sort(arr):
    n = len(arr)
    
    # Return if the array is empty or has only one element
    if n <= 1:
        return
    
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]  # The element to be positioned correctly
        j = i - 1  # Index of the last sorted element
        
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        arr[j + 1] = key  # Place the key in its correct position

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

