def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm."""
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1

        arr[j + 1] = key  # Insert the key in the correct position

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)
