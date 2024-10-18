# Python3 code to implement iterative Binary Search.

# This function returns the index of x in the array arr if present, otherwise -1
def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2  # Find the mid index

        # Check if x is present at mid
        if arr[mid] == x:
            return mid  # Element found

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1

# Driver code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binary_search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in the array")
